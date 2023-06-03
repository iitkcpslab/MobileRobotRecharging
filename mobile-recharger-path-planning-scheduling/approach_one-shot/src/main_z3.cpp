
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
  //cout << endl << duration << "s" << endl;
  cout << endl << hr << "h " << min << "m " << (((sec - int(sec)) > 0.5) ? (int(sec) + 1) : int(sec)) << "s" << endl;
  ss << hr << "h " << min << "m " << (((sec - int(sec)) > 0.5) ? (int(sec) + 1) : int(sec)) << "s";
  string t = ss.str();
  return t;
  //ofstream ofp;
  //ofp.open("result", fstream::app);
  //ofp << hr << "h " << min << "m " << (((sec - int(sec)) > 0.5) ? (int(sec) + 1) : int(sec)) << "s" << endl << endl;
  //ofp.close();
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


void generateZ3File (prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace, worker_vec_t workers, unsigned int max_timept)
{ 
  ofstream ofp;
  ofp.open("constraints.smt2");

  declareVariables_workers (ofp, workspace, workers);
  declareVariables_rechargers (ofp, workspace);

  instantiateVariables_workers (ofp , workspace, workers);
  writeTrajectoryToLoopMapping_workers (ofp, workspace, workers);
  writeMatchingConstraints_workers (ofp, workspace, workers);
  writeTransition_workers (ofp, workspace, workers);

  writeTransitionConstraints_rechargers (ofp, primitives, obstacles, workspace, max_timept);
  writeMatchingConstraints_rechargers (ofp, workspace, workers);
  //writeCollisionAvoidanceConstraints (ofp, primitives, workspace);

  minimizeWaiting_workers (ofp, workspace, workers);
  writeOutputConstraints_rechargers (ofp, workspace);
  writeOutputConstraints_workers (ofp, workspace, workers);

  ofp.close();
}


/*
position optimize_rcost_binary (prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace, worker_vec_t workers, rechinst_vec_t rechinstances, workerhalt_vec_t workerhalt, unsigned int max_timept, unsigned int rcost, string filename)
{
  stringstream ss;
  position range;
  unsigned int upper, middle, lower, sat_res, pivot;
  upper=middle=pivot=rcost; lower=1;
  int bound_flag[rcost+1];
  for(unsigned int count=1; count <=rcost; count++)
  {
    bound_flag[count]=0;
  }
  ss.str("");
  ss << "timeout 30s z3 ../examples/constraints2.smt2 > ../examples/my_output/z3_output_" << workspace.number_of_wrobs << "_" << workspace.hlen << "_ext1";
  string cmdline = ss.str();

  cout << "FINDING OPTIMAL RANGE OF RECHARGER COST :" << endl;
  for(int i=1; i<=2; i++)
  {
    while (upper-lower > 1)
    {
      generateZ3File2 (primitives, obstacles, workspace, workers, rechinstances, workerhalt, max_timept, middle);
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
    lower=pivot; upper=rcost;
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


void writeRobTrajectories (worker_vec_t workers, string filename, unsigned int nrechs, testcase_t &testcase)
{
  stringstream ss_wtrajs, ss_rtrajs;
  ss_wtrajs << "-----------------------Workers------------------------" << endl;
  ss_wtrajs << writeWorkingTraj(workers) << endl; //workers' trajectories
  testcase.consolid_wtrajs = ss_wtrajs.str();
  
  ss_rtrajs << "----------------------Rechargers-----------------------" << endl;
  for (unsigned int count = 1; count <= nrechs; count++)
  {
    ss_rtrajs << getRechargerTraj(filename, count);
  }
  testcase.consolid_rtrajs = ss_rtrajs.str();
  cout << testcase.consolid_wtrajs << testcase.consolid_rtrajs << endl;
} 


void create_latex_table (testcase_t testres)
{
  string str, ln;
  stringstream ss;
  ss << "       ";
  ss << testres.obs_name << " & " << testres.wcount << " & " << testres.rcount << " & " << testres.orig_hlen << " & wt=" << testres.wait_idle << " & hard=" << testres.hardeffic << " & soft=" << testres.softeffic << " & " << testres.elapsed_time << " \\\\";
  str = ss.str();

  ifstream ifp;
  ofstream ofp;

  ifp.open("../examples/myres/table_1shot_pr_source.tex");
  ofp.open("../examples/myres/table_1shot_pr_destin.tex");

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
  ss1 << "../examples/myres/"  << testres.dim+1 << "dim_" << testres.wcount << "W_"<< testres.rcount << "R_" <<  testres.orig_hlen << "H" << "_1shot_pr.txt";
  filename = ss1.str();

  ofstream ofp1;
  ofp1.open(filename.c_str());

  ofp1 << testres.rechinstances << endl;
  ofp1 << testres.consolid_wtrajs << testres.consolid_rtrajs << endl;
  ofp1 << "orig_hyplen = " << testres.orig_hlen << endl;
  ofp1 << "wait_idle = " << testres.wait_idle << endl << endl;

  ofp1 << "hard efficiency = " << testres.hardeffic << endl;
  ofp1 << "soft efficiency = " << testres.softeffic << endl;
  ofp1 << "elapsed time = " << testres.elapsed_time << endl;

  ofp1.close();

  /* for keeping result backup in another file - end*/
  system("cp ../examples/myres/table_1shot_pr_destin.tex ../examples/myres/table_1shot_pr_source.tex");
  return;
}


int main ()
{
  double wcts, wcte;
  struct timeval tm;
  gettimeofday( &tm, NULL );
  wcts = (double)tm.tv_sec + (double)tm.tv_usec * .000001;

  prim_vec_t primitives;
  pos_vec_t obstacles;
  workspace_t workspace;
  worker_vec_t workers;
  rechinst_vec_t rechinstances;
  workerhalt_vec_t workerhalt;
  string filename, filename1, filename2, cmdline;
  stringstream ss;
  testcase_t testcase;

  cout << endl << "============================ ONE-SHOT approach ===========================" << endl;
  cout << "READING INPUTS ..." << endl;
  readPrimitives (primitives);
  readObstacles (obstacles, testcase);
  //writeObstacles (obstacles);
  readWorkspace (workspace, obstacles, workers);

  workspace.min_x = 0; 
  workspace.min_y = 0; 

  cout << endl << "PROCESSING, PLEASE WAIT ..." << endl;
  generateZ3File (primitives, obstacles, workspace, workers, workspace.hlen);
  ss << "time timeout 15000s z3 ../examples/constraints.smt2 > ../examples/my_output/z3_output_" << workspace.number_of_wrobs << "_" << workspace.hlen;

  cmdline = ss.str();
  system (cmdline.c_str());
    
  filename = cmdline.substr (cmdline.find("../examples/my_output"));
  filename1 = filename;
  cout << "Filename is : " << filename1 << " --> ";

  int sat_res = is_sat(filename1);
  if(sat_res==0)
  {  
     cout << " --> UNSAT" << endl;
     ss.str(""); ss.clear();
     ss << "rm " << filename1;
     system(ss.str().c_str());
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
  cout << "Recharging instances are as below :" << endl;
  cout << "=======================================================" << endl;

  for (unsigned int count=0; count<workers.size(); count++)
  {
    ss.str(""); ss << "((wx_" << count+1 << "_"; string robstrx = ss.str();
    ss.str(""); ss << "((wy_" << count+1 << "_"; string robstry = ss.str();
    workers[count].workingtraj = readWorkingTraj (filename1, robstrx, robstry, workspace.hlen);
  }

/*========================================================================================================== */

  testcase.rechinstances = readRechInstances (rechinstances, workers, filename1);
  writeRobTrajectories (workers, filename1, workspace.number_of_rechs, testcase);

  //unsigned int rcost = readValue ("((total_rcost ", filename1); 
  //cout << endl << "Unoptimized cost of recharger: " << rcost << endl;

  unsigned int tot_wt_upto_halt = tot_wait_upto_halt ("((waitcount", filename1, workspace.hlen, workspace.number_of_wrobs);
  unsigned int nrechs = rechinstances.size();
  //cout << "Number of recharging : " << nrechs << endl << endl;
  unsigned int tot_wait = tot_wt_upto_halt;

  //cout << "TOTAL WAIT TIME OF WORKERS (recharging is counted as waiting) : " << tot_wait << endl;
  double effic = 100*((workspace.number_of_wrobs*workspace.hlen) - tot_wait) / (double) (workspace.number_of_wrobs*workspace.hlen);
  cout << "hard EFFICIENCY (recharging is counted as waiting) : " << effic << endl;
  testcase.hardeffic = effic;

  tot_wait = tot_wt_upto_halt - nrechs;
  testcase.wait_idle = tot_wait;
  //cout << "TOTAL WAIT TIME OF WORKERS (recharging is NOT counted as waiting) : " << tot_wait << endl;
  effic = 100*((workspace.number_of_wrobs*workspace.hlen) - tot_wait) / (double) (workspace.number_of_wrobs*workspace.hlen);
  cout << "soft EFFICIENCY (recharging is NOT counted as waiting) : " << effic << endl;
  testcase.softeffic = effic;
  
  testcase.dim = workspace.length_x;
  testcase.wcount = workspace.number_of_wrobs;
  testcase.rcount = workspace.number_of_rechs;
  testcase.orig_hlen = workspace.hlen;
  cout << "-------------------------------------------------------";
 
  gettimeofday( &tm, NULL );
  wcte = (double)tm.tv_sec + (double)tm.tv_usec * .000001;
  testcase.elapsed_time = printTimeDifference(wcts, wcte);
  cout << endl;
  
  //create_latex_table (testcase);
  return 0;
}
