#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>
#include "primitive.h"
#include "readinputs.h"
#include "writeconstraints_recharger.h"
#include "writeconstraints_workers.h"
#include "writeconstraints_recharger_optimal.h"
using namespace std;

string printTimeDifference(double wcts, double wcte)
{
  double duration;
  int hr, min;
  double sec;
  stringstream ss;

  duration = wcte - wcts;
  hr = duration / 3600; 
  min = (duration / 60) - (hr * 60) ;
  sec = duration - hr * 3600 - min * 60;
  cout << endl << hr << "h " << min << "m " << (((sec - int(sec)) > 0.5) ? (int(sec) + 1) : int(sec)) << "s" << endl;
  ss << hr << "h " << min << "m " << (((sec - int(sec)) > 0.5) ? (int(sec) + 1) : int(sec)) << "s";
  string t = ss.str();
  return t;
}


int is_sat (string filename)
{
 ifstream ifp;
 int flag = 2;
 string str;
 ifp.open(filename.c_str());

 string line, line1 = "CUT";
  
 if(ifp.is_open())
 {
   while (getline(ifp, line))
   {
     if (line.compare("sat")==0)
      flag=1;
     if (line.compare("unsat")==0)
     {
       flag=0;
       break;
     }
   }
 }
 ifp.close();
 return flag;
}


unsigned int get_max_intrech_timept (workerhalt_vec_t workerhalt)
{
  unsigned int max_intrech_timept = 0;
  
  for (unsigned int count = 0; count < workerhalt.size(); count++)
  {
    unsigned int d = workerhalt[count].timept;
    if (d > max_intrech_timept)
    {
      max_intrech_timept = d;
    }
  }
  return max_intrech_timept;
}


unsigned int get_max_intrech_duration (workerhalt_vec_t workerhalt)
{
  unsigned int max_intrech_duration = 0;
  
  for (unsigned int count = 0; count < workerhalt.size(); count++)
  {
    unsigned int d = workerhalt[count].duration;
    if (d > max_intrech_duration)
    {
      max_intrech_duration = d;
    }
  }
  return max_intrech_duration;
}

void generate_getModel (ofstream &ofp)
{
  ofp << endl << "from z3 import *" << endl << endl;
  ofp << "# geting interpretations from model" << endl;
  ofp << "def get_model (*argv):" << endl;
  ofp << "   print 'printing model--start'" << endl;
  ofp << "   for x in argv:" << endl;
  ofp << "      print x, '=', m.evaluate(x)" << endl;
  ofp << "   print 'printing model--end'" << endl;
  ofp << "   return m.evaluate(total_wait).as_long()" << endl << endl;
  return; 
}

// checking for satisfiability;
// this function is called from binarySearch_solving()
void generate_checkSat (ofstream &ofp)
{
  ofp << endl << "# incremental checking for sat" << endl;
  ofp << "def check_sat (mid):" << endl;
  ofp << "   print 'check total_wait <= %d --->' % mid," << endl;
  ofp << endl;
  ofp << "   s.push()" << endl;
  ofp << "   s.add(total_wait<=mid) # incremental constraint" << endl;
  ofp << "   s.set('timeout', 900000)" << endl;
  ofp << "   res=s.check()" << endl;
  ofp << "   print res, '\\n'" << endl << endl;

  ofp << "   if res==sat:" << endl;
  ofp << "      global m" << endl;
  ofp << "      m = s.model()" << endl;
  ofp << "      val = get_model(total_wait, total_rech)" << endl;
  ofp << "   else:"<< endl;
  ofp << "      val=0" << endl;
  ofp << "   print '---------------------'" << endl;
  ofp << "   s.pop()" << endl << endl;

  ofp << "   return val" << endl;
  return;
}

// binary search logic for solving;
// check_sat() is called from here.
void generate_binarySearch_solving (ofstream &ofp)
{
  ofp << endl << "# binary search for optimization";
  ofp << endl << "# this fn returns the val to which total_wait should be set";
  ofp << endl << "# to check satisfiability" << endl;

  ofp << "def binarySearch_solving (left, right):" << endl;
  ofp << "   val=-1" << endl;
  ofp << "   while right>=left:" << endl;
  ofp << "      mid = left+(right-left)//2" << endl;
  ofp << "      mid1 = check_sat(mid)" << endl;
  ofp << "      if mid1>=1:" << endl;
  ofp << "         right = mid1-1" << endl;
  ofp << "         val = mid1" << endl;
  ofp << "      else: left = mid+1" << endl;
  ofp << "   return val" << endl;
  return;
}

void generate_linearSearch_solving (ofstream &ofp)
{
  ofp << endl << "# linear search for optimization";
  ofp << "def linearSearch_solving (left, right):" << endl;
  ofp << "   val=r=right" << endl;
  ofp << "   while r>=left:" << endl;
  ofp << "      val = check_sat(--r)" << endl;
  ofp << "      if val>=1:" << endl;
  ofp << "         val = r" << endl;
  ofp << "         continue" << endl;
  ofp << "      else: break" << endl;
  ofp << "   return val" << endl;
 
  return;
}

// generate static constraints
void generate_constraints_static (ofstream &ofp, prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace, worker_vec_t workers, int max_timept)
{ 
  ofp << endl << "# initializing solver" << endl;
  ofp << "s = Solver()" << endl << endl;
  ofp << endl << "# adding static constraints" << endl;
  declareVariables_workers (ofp, workspace, workers);
  declareVariables_rechargers (ofp, workspace);

  instantiateVariables_workers (ofp , workspace, workers);
  writeTrajectoryToLoopMapping_workers (ofp, workspace, workers);
  writeMatchingConstraints (ofp, workspace, workers);
  writeTransition_workers (ofp, workspace, workers);

  writeTransitionConstraints_rechargers (ofp, primitives, obstacles, workspace, max_timept);

  // binary search to find the minimum value of total_wait
  get_counts_workers (ofp, workspace, workers);
  //writeOutputConstraints_rechargers (ofp, workspace);
  //writeOutputConstraints_workers (ofp, workspace, workers);
  return;
}

// driver code - terminate
void generate_driver (ofstream &ofp, int left, int right)
{
   ofp << endl << "# driver code -- terminate" << endl;
   ofp << "s.set('timeout', 7200000)" << endl;
   
   ofp << "print '\\n================='"<< endl;
   ofp << "print 'check static part ---> %s\\n' % s.check()" << endl;
   ofp << endl;
   ofp << "m = s.model()" << endl;
   ofp << "r = get_model(total_wait, total_rech)" << endl;
   ofp << "l = " << left << endl;
   ofp << "print '-----------------'"<< endl << endl;

   ofp << "x = binarySearch_solving (l, r)" << endl << endl;
   ofp << "#x = linearSearch_solving (l, r)" << endl << endl;

   ofp << "print '\\nmin(total_wait) = %s' % x" << endl;
   ofp << "if x==-1: print '--undefined--'" << endl;

   ofp << "print '\\n================='"<< endl;
   return;
}


void generateZ3File2 (prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace, worker_vec_t workers, rechinst_vec_t rechinstances, workerhalt_vec_t workerhalt, unsigned int max_timept, unsigned int ext_hyp_start)
{
  ofstream ofp;
  ofp.open("constraints2.smt2");

  declareVariables2 (ofp, workspace, max_timept);
  writeWaypointsConstraints2 (ofp, workspace, obstacles, workers, rechinstances, workerhalt, max_timept);
  writeTransitionConstraints_rechargers (ofp, primitives, obstacles, workspace, max_timept);
  //writeCollisionAvoidanceConstraints2 (ofp, workspace, workers, max_timept); omitted for better effic
  //minimize_rcost (ofp, max_timept, ext_hyp_start);
  writeOutputConstraints2 (ofp, max_timept, workspace, workerhalt, ext_hyp_start);
}


int limit_found (int* bound_flag, position* range, unsigned int rcost)
{
  unsigned int count1=-999, count2=999, found_down=0, found_up=0, found_flag=0;
  for(count1=1; count1<rcost; count1++)
  {
    if(bound_flag[count1]==1 && (bound_flag[count1+1]==3 || bound_flag[count1+1]==2))
    { 
      found_down=1;
      found_flag=1;
      break;
    }
  }
  for(count2=rcost; count2>1; count2--)
  {
    if(bound_flag[count2]==2 && (bound_flag[count2-1]==3 || bound_flag[count2-1]==1))
    {
      found_up=1;
      found_flag=2;
      break;
    }
  }
  if (found_up && found_down)
  {
    (*range).x=count2; (*range).y=count1;
    found_flag=3;
  }
  return found_flag;
}

/*
// optimization using linear search
position optimize_wait_linear (prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace, worker_vec_t workers, rechinst_vec_t rechinstances, workerhalt_vec_t workerhalt, unsigned int max_timept, unsigned int total_wait, string filename)
{
  stringstream ss;
  position range;

  * upper limit *
  ss.str("");
  ss << "timeout 60s z3 ../examples/constraints2.smt2 > ../examples/my_output/z3_output_" << workspace.number_of_wrobs << "_" << workspace.hlen << "_ext1";
  string cmdline = ss.str();

  cout << "Finding upper limit .." << endl;
  while(1)
  {
    rcost--;
    cout << "checking for : " << total_wait << endl;
    generateZ3File2 (primitives, obstacles, workspace, workers, rechinstances, workerhalt, max_timept, total_wait);
    system (cmdline.c_str());
    if(is_sat(filename)!=1) break;
  }
  range.x = total_wait+1;

  * lower limit *
  rcost=0;
  cout << "Finding lower limit .." << endl;
  while(++rcost <= (unsigned int)range.x)
  {
    cout << "checking for : " << total_wait << endl;
    generateZ3File (primitives, obstacles, workspace, workers, rechinstances, workerhalt, max_timept, total_wait);
    system (cmdline.c_str());
    if(is_sat(filename)!=0) break;
  }
  range.y = total_wait;

  generateZ3File (primitives, obstacles, workspace, workers, rechinstances, workerhalt, max_timept, range.x);
  system (cmdline.c_str());
  return range;
}
*/

/*
// optimization using binary search
position optimize_wait_binary (prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace, worker_vec_t workers, rechinst_vec_t rechinstances, workerhalt_vec_t workerhalt, unsigned int max_timept, unsigned int total_wait, string filename)
{
  stringstream ss;
  position range;
  unsigned int upper, middle, lower, sat_res, pivot;
  upper=middle=pivot=total_wait; lower=1;

  int bound_flag[total_wait+1];
  for(unsigned int count=1; count <=total_wait; count++)
  {
    bound_flag[count]=0;
  }
  ss.str("");
  ss << "timeout 30s python ../examples/constraints2.py > ../examples/my_output/z3_output_" << workspace.number_of_wrobs << "_" << workspace.hlen << "_ext1";
  string cmdline = ss.str();

  cout << "FINDING OPTIMAL RANGE OF RECHARGER COST :" << endl;
  for(int i=1; i<=2; i++)
  {
    while (upper-lower > 1) // loop binary search
    {
      generateZ3File (primitives, obstacles, workspace, workers, rechinstances, workerhalt, max_timept, middle);
      system (cmdline.c_str());
      sat_res = is_sat(filename);

      if(sat_res==0)
      {
        //cout << "Middle = " << middle << " is an UNSAT point." << endl;
        lower = middle;
        if(i==1) range.y = lower;
        bound_flag[middle] = 1;
        int found_flag = limit_found(bound_flag, &range, rcost);
        if (found_flag==3) break;
      }
      else if(sat_res==1)
      {
        //cout << "Middle = " << middle << " is a SAT point." << endl;
        upper = middle;
        if(i==2) range.x = upper;
        bound_flag[middle] = 2;
        int found_flag = limit_found(bound_flag, &range, rcost);
        if (found_flag==3) break;
      }
      else
      {
        //cout << "Middle = " << middle << " is an UNKNOWN point." << endl;
        bound_flag[middle] = 3;
        int found_flag = limit_found(bound_flag, &range, rcost);
        if (found_flag==0) 
        {
          upper=middle;
          if(i==1) pivot=middle;
        }
        else if (found_flag==1) lower=middle;
        else if (found_flag==2) upper=middle;
        else if (found_flag==3) break;
      }
      middle = (lower + upper)/2;
    }
    lower=pivot; upper=total_wait;
  }
  generateZ3File2 (primitives, obstacles, workspace, workers, rechinstances, workerhalt, max_timept, range.x);
  system (cmdline.c_str());

  return range;
}
*/

unsigned int total_ext_hyp (unsigned int ext_hyp, workerhalt_vec_t workerhalt)
{
  unsigned int ext_hyp_new = ext_hyp;
  for (unsigned int count=0; count<workerhalt.size(); count++)
  {
    if (workerhalt[count].duration > 1)
    {
      ext_hyp_new += workerhalt[count].duration - 1;
    }
  }
  return ext_hyp_new;
}

unsigned int get_total_lastrech_dur (workerhalt_vec_t workerhalt)
{
  unsigned int tot_dur=0;
  for (unsigned int count=0; count<workerhalt.size(); count++)
  {
    tot_dur = tot_dur + workerhalt[count].duration;
  }
  return tot_dur;
}

unsigned int get_tot_time_after_intrech (workerhalt_vec_t workerhalt, unsigned int tot_ext)
{
  unsigned int tot_dur=0;
  for (unsigned int count=0; count < workerhalt.size(); count++)
  {
    tot_dur = tot_dur + (tot_ext - workerhalt[count].timept + 1);
  }
  cout << endl << "tot time after int. rech " << tot_dur << endl;
  return tot_dur;
}

unsigned int get_total_extra_halt_time (workerhalt_vec_t workerhalt, unsigned int ext_hyp_init)
{
  unsigned int tot_dur = 0;
  for (unsigned int count=0; count < workerhalt.size(); count++)
  {
    tot_dur = tot_dur + (ext_hyp_init - workerhalt[count].timept);
  }
  return tot_dur;
}

void writeRobTrajectories (worker_vec_t workers, string filename1, string filename2, unsigned int nrechs, testcase_t &testcase)
{
  stringstream ss_wtrajs, ss_rtrajs;
  ss_wtrajs << "-----------------------Workers------------------------" << endl;
  ss_wtrajs << writeWorkingTraj(workers) << endl; //workers' trajectories
  testcase.consolid_wtrajs = ss_wtrajs.str();

  ss_rtrajs << "----------------------Rechargers-----------------------" << endl;
  for (unsigned int count = 1; count <= nrechs; count++)
  {
    ss_rtrajs << getRechargerTraj(filename2, count);
  }
  testcase.consolid_rtrajs = ss_rtrajs.str();
  cout << testcase.consolid_wtrajs << testcase.consolid_rtrajs << endl;
}


void create_latex_table (testcase_t testres)
{
  string str, ln;
  stringstream ss;
  ss << "       ";
  ss << testres.obs_name << "W=" << testres.wcount << " & R=" << testres.rcount << " & orig=" << testres.orig_hlen << " & ext=" << testres.ext_hlen << " & totrechs=" << testres.intrechcount+testres.lastrechcount << " & idle=" << testres.wait_idle << " & hardeffic=" << testres.hardeffic << " & softeffic=" << testres.softeffic << " & " << testres.elapsed_time << " \\\\";
  str = ss.str();

  ifstream ifp;
  ofstream ofp;

  //ifp.open("../examples/myres/table_2shot_pr_source.tex");
  //ofp.open("../examples/myres/table_2shot_pr_destin.tex");

  ifp.open("../examples/myres/table_nocollis_2shot_source.tex");
  ofp.open("../examples/myres/table_nocollis_2shot_destin.tex");

  while(getline(ifp,ln))
  {
    size_t loc = ln.find("end{tabular}");
    if(loc!=string::npos) break;
    ofp << ln << endl;
  }
  ofp << str << endl << ln << endl; //table entry and the flagged line to be written
  while(getline(ifp,ln))
    ofp << ln << endl;

  ifp.close();
  ofp.close();

  /* for keeping result backup in another file - start*/
  string filename;
  stringstream ss1;
  ss1 << "../examples/myres/"  << testres.dim+1 << "dim_" << testres.wcount << "W_"<< testres.rcount << "R_" <<  testres.orig_hlen << "H" << "_FINAL_2shot_pr.txt";
  filename = ss1.str();

  ofstream ofp1;
  ofp1.open(filename.c_str());

  ofp1 << testres.rechinstances << endl;
  ofp1 << testres.lastrechs << endl;
  ofp1 << testres.consolid_wtrajs << testres.consolid_rtrajs << endl << endl;
  
  ofp1 << "unitrech = " << testres.unitrech << endl;
  ofp1 << "orig_hyplen = " << testres.orig_hlen << endl;
  ofp1 << "ext_hyplen = " << testres.ext_hlen << endl << endl;

  ofp1 << "int.rechs = " << testres.intrechcount << endl;
  ofp1 << "last.rechs = " << testres.lastrechcount << endl << endl;
  ofp1 << "wait_idle = " << testres.wait_idle << endl;

  ofp1 << "hard effic. = " << testres.hardeffic << endl;
  ofp1 << "soft effic. = " << testres.softeffic << endl << endl;

  ofp1 << "elapsed time = " << testres.elapsed_time << endl;

  ofp1.close();
  /* for keeping result backup in another file - end*/
  system("cp ../examples/myres/table_nocollis_2shot_destin.tex ../examples/myres/table_nocollis_2shot_source.tex");

  return;
}

/*
// r and l represents values of total_wait. idea is to go down.
// initially, l->unsat, r->sat. check (l+r)/2 for satisfiability.
int binarySearch_satPt(int l, int r)
{
    int mid, val=r;
    while (r >= l) { 
        mid = l + (r - l) / 2;
        if (check_sat(mid)==1) // sat
	{
 	   r = mid - 1;
	   val = mid;
	}
	else  // unsat or undefined
	   l = mid + 1;
    } 
    return val;
} 
*/

int main ()
{
/*
  double wcts, wcte;
  struct timeval tm;
  gettimeofday( &tm, NULL );
  wcts = (double)tm.tv_sec + (double)tm.tv_usec * .000001;
*/
  prim_vec_t primitives;
  pos_vec_t obstacles;
  workspace_t workspace;
  worker_vec_t workers;
  rechinst_vec_t rechinstances;
  workerhalt_vec_t workerhalt;
  string filename, filename1, filename2, cmdline;
  stringstream ss;
  testcase_t testcase;

  cout << endl << "============================ TWO-SHOT approach ===========================" << endl;
  cout << "Reading inputs ..." << endl;
  readPrimitives (primitives);
  readObstacles (obstacles, testcase);
  readWorkspace (workspace, obstacles, workers);

  workspace.min_x = 0; workspace.min_y = 0; 

  cout << endl << "Processing, please wait ..." << endl;

  // FIRST phase, getting unoptimized value
  ///generateZ3File (primitives, obstacles, workspace, workers, workspace.hlen);
  ofstream ofp;
  ofp.open("constraints_z3py.py"); // python file

  int left=1; // setting left and right bounds for binary search
  int right=workspace.number_of_wrobs*workspace.hlen;
  generate_getModel (ofp);
  generate_checkSat (ofp);
  generate_binarySearch_solving (ofp);
  generate_constraints_static (ofp, primitives, obstacles, workspace, workers, workspace.hlen);
  generate_driver (ofp, left, right);
/*
  ss << "time timeout 15000s python ../examples/constraints_z3py.py > ../examples/my_output/z3_output_" << workspace.number_of_wrobs << "_" << workspace.hlen;
  cmdline = ss.str(); system (cmdline.c_str());
    
  filename = cmdline.substr (cmdline.find("../examples/my_output"));
  filename1 = filename; cout << "Filename is : " << filename1 << " --> ";
*/
  /*
  int sat_res = is_sat(filename1);
  if(sat_res==0)
  {  
     cout << " --> UNSAT" << endl;
     ss.str(""); ss.clear();
     ss << "rm " << filename1; system(ss.str().c_str());
  }
  else if(sat_res==1)
  {
     cout << " --> SAT" << endl;
  }
  else
  {
     cout << " --> UNKNOWN" << endl;
     exit(0);
  }
  cout << "SAT testing IS DONE ..." << endl << endl;
  cout << "-------------------------------------------------------" << endl;
  
  unsigned int wait_unopt = readGetValue ("total_wait ", filename1); // change needed
  cout << endl << "total UNOPTIMIZED wait = " << wait_unopt;

  range = optimize_wait_binary (primitives, obstacles, workspace, workers, rechinstances, workerhalt, ext_hyp, total_wait, filename1);
  */
/*
  // fetching outcomes from first phase to use them in the second phase
  for (unsigned int count=0; count<workers.size(); count++)
  {
    ss.str(""); ss << "((wx_" << count+1 << "_"; string robstrx = ss.str();
    ss.str(""); ss << "((wy_" << count+1 << "_"; string robstry = ss.str();
    workers[count].workingtraj = readWorkingTraj (filename1, robstrx, robstry, workspace.hlen);
  }

*========================================================================================================== *

  for (unsigned int count1 = 0; count1 <  workspace.number_of_rechs; count1++)
  {
    workspace.rpos_start.push_back(readRechargerPosition (filename1, count1+1 , 1));
    workspace.rpos_hlen.push_back(readRechargerPosition (filename1, count1+1, workspace.hlen));
  }
  testcase.rechinstances = readRechInstances (rechinstances, workers, filename1);
  testcase.lastrechs = readWorkerHaltDetails (workerhalt, workspace, workers, filename1);

  // SECOND phase
  unsigned int ext_hyp, upper = workspace.hlen + 50, result;
  ss.str("");
  ss << "timeout 4000s z3 ../examples/constraints2.smt2 > ../examples/my_output/z3_output_" << workspace.number_of_wrobs << "_" << workspace.hlen << "_ext1";
  cmdline = ss.str();
  filename = cmdline.substr (cmdline.find("../examples/my_output"));
  filename2 = filename;
  
  unsigned int ext_hyp_init = workspace.hlen;  // for calculation
  unsigned int ext_hyp_start = get_max_intrech_timept (workerhalt) + get_max_intrech_duration (workerhalt);
  ext_hyp = ext_hyp_start;
  // ext_hyp = workspace.hlen;
  
  for ( ; ext_hyp <= upper ; ext_hyp++)
  {
    generateZ3File2 (primitives, obstacles, workspace, workers, rechinstances, workerhalt, ext_hyp, ext_hyp_start);
    system (cmdline.c_str());
    result = is_sat(filename2);

    if(result==1) 
    {
      cout << " --> SAT !!" << endl;
      break;
    }
    else if(result==0)
    {
       cout << " --> UNSAT" << endl;
       ss.str(""); ss.clear();
       ss << "rm " << filename2;
       system(ss.str().c_str());
       continue;
    }
    else 
    {
       cout << " --> UNKNOWN" << endl;
    }
  }
  cout << endl;

*========================================================================================================== *

  // reading output
  writeRobTrajectories (workers, filename1, filename2, workspace.number_of_rechs, testcase);
  cout << endl << "EXTENDED HYPERLENGTH IS : " << ext_hyp << endl;
  //unsigned int rcost = readValue ("((total_rcost ", filename2); 
  //cout << endl << "Unoptimized cost of recharger: " << rcost << endl;
  unsigned int tot_wt_upto_halt = tot_wait_upto_halt ("((waitcount", filename1, ext_hyp_init, workspace.number_of_wrobs);
  testcase.ext_hlen = ext_hyp;
  testcase.intrechcount = rechinstances.size();
  testcase.lastrechcount = get_total_lastrech_dur (workerhalt);

  // wait
  unsigned int idle_upto_halt = tot_wt_upto_halt; // including intrechs
  unsigned int idle_after_halt = (ext_hyp-ext_hyp_init) * workspace.number_of_wrobs; // including lastrechs

  // hard effic  
  unsigned int tot_hard_wait = idle_upto_halt + idle_after_halt; // including recharge instances
  double hardeffic = 100*((workspace.number_of_wrobs*ext_hyp) - tot_hard_wait) / (double) (workspace.number_of_wrobs*ext_hyp);
  testcase.hardeffic = hardeffic;
  cout << "hard EFFICIENCY (recharging is counted as waiting) : " << hardeffic << endl;

  // soft effic
  unsigned int tot_soft_wait = idle_upto_halt + idle_after_halt - testcase.intrechcount - testcase.lastrechcount;
  double softeffic = 100*((workspace.number_of_wrobs*ext_hyp) - tot_soft_wait) / (double) (workspace.number_of_wrobs*ext_hyp);
  testcase.softeffic = softeffic;
  cout << "soft EFFICIENCY (recharging is NOT counted as waiting) : " << softeffic << endl << endl;

  testcase.wait_idle = tot_soft_wait;  // recharging not considered
  cout << "Wait_idle for workers : " << testcase.wait_idle << endl;
  cout << "Total recharge : " << testcase.intrechcount + testcase.lastrechcount << endl;
  testcase.dim = workspace.length_x;
  testcase.wcount = workspace.number_of_wrobs;
  testcase.rcount = workspace.number_of_rechs;
  testcase.unitrech = workspace.recharge;
  testcase.orig_hlen = workspace.hlen;

  cout << "-------------------------------------------------------";
 
  gettimeofday( &tm, NULL );
  wcte = (double)tm.tv_sec + (double)tm.tv_usec * .000001;
  testcase.elapsed_time = printTimeDifference(wcts, wcte); cout << endl;
  //create_latex_table (testcase);
  */
  return 0;
}
