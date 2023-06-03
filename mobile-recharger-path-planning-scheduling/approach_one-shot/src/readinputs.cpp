#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include "primitive.h"
#include "readinputs.h"
using namespace std;

void readPrimitives(prim_vec_t &primitives)
{
  ifstream ifp;

  string line;
  string str;
  int location, location1, location2, location3;
  position pos_tmp;
  int xmin, ymin, xmax, ymax;
  
  state q_i, q_f;
  position pos_f;
  string cost;
  pos_vec_t swath;
  position pos_min;
  position pos_max;

  ifp.open("../examples/2d_template.txt");

  if (ifp.is_open())
  {
    while (getline(ifp, line))
    {
      location = line.find(":");

      if (line.substr(0, location) == "q_i")
      {
        istringstream (line.substr(location+2, 1)) >> q_i.velocity;
      }

      if (line.substr(0, location) == "q_f")
      {
	istringstream (line.substr(location+2, 1)) >> q_f.velocity;
      }

      if (line.substr(0, location) == "pos_f")
      {
        location1 = line.find('[');
        location2 = line.find(',');
        location3 = line.find(']');
        istringstream (line.substr(location1 + 1, location2 - location1 - 1)) >> pos_f.x;
        istringstream (line.substr(location2 + 2, location3 - location2 - 2)) >> pos_f.y;
      }

      if (line.substr(0, location) == "cost")
      {
        cost = line.substr(location + 1);
        //cost.erase(cost.size() - 1);
      }

      if (line.substr(0, location) == "swath")
      {
        str = line.substr(location+1);
        xmin = 10000; ymin = 10000; xmax = -10000; ymax = -10000;
        location = str.find(';');
        while (location != -1)
        {
          location1 = str.find('[');
          location2 = str.find(',');
          location3 = str.find(']');
          istringstream (str.substr(location1 + 1, location2 - location1 - 1)) >> pos_tmp.x;
          istringstream (str.substr(location2 + 2, location3 - location2 - 2)) >> pos_tmp.y;
          swath.push_back(pos_tmp);
          if (pos_tmp.x < xmin) 
            xmin = pos_tmp.x;
          if (pos_tmp.y < ymin) 
            ymin = pos_tmp.y;
          if (pos_tmp.x > xmax) 
            xmax = pos_tmp.x;
          if (pos_tmp.y > ymax) 
            ymax = pos_tmp.y;
          str = str.substr(location+1);
          location = str.find(';');
          //cout << pos_tmp.x << "  ---  " << pos_tmp.y << endl;
        }
        location1 = str.find('[');
        location2 = str.find(',');
        location3 = str.find(']');
        istringstream (str.substr(location1 + 1, location2 - location1 - 1)) >> pos_tmp.x;
        istringstream (str.substr(location2 + 2, location3 - location2 - 2)) >> pos_tmp.y;
        //cout << pos_tmp.x << "  ---  " << pos_tmp.y << endl;
        swath.push_back(pos_tmp);
        if (pos_tmp.x < xmin) 
          xmin = pos_tmp.x;
        if (pos_tmp.y < ymin) 
          ymin = pos_tmp.y;
        if (pos_tmp.x > xmax) 
          xmax = pos_tmp.x;
        if (pos_tmp.y > ymax) 
          ymax = pos_tmp.y;
        pos_min.x = xmin;
        pos_min.y = ymin;
        pos_max.x = xmax;
        pos_max.y = ymax;        
        Primitive prim(q_i, q_f, pos_f, cost, swath, pos_min, pos_max);
        primitives.push_back(prim); 
        swath.erase (swath.begin(), swath.end());
      }
    }
    ifp.close();
  }
}


void readObstacles(pos_vec_t &obstacles, testcase_t &testcase)
{
  ifstream ifp;
  string line;
  int location; 
  position pos_tmp;

  ifp.open("../examples/obstacle.txt");  
  if (ifp.is_open())
  {
    while (getline(ifp, line))
    {
      if (line.find("ware")!=string::npos || line.find("pensyl")!=string::npos || line.find("rand")!=string::npos)
      {
        cout << line << endl;
	testcase.obs_name = line;
        continue;
      }
      location = line.find(' ');
      istringstream (line.substr(0, location)) >> pos_tmp.x;
      istringstream (line.substr(location + 1)) >> pos_tmp.y;
      obstacles.push_back(pos_tmp);
    }
  }
  ifp.close();

}

void writeObstacles(pos_vec_t obstacles)
{
  for (unsigned int count=0; count<obstacles.size(); count++)
  cout << obstacles[count].x << " " << obstacles[count].y << " => ";
}


void extendObstaclesList (pos_vec_t &obs, worker_vec_t workers)
{
  /* also add the trajectory of workers in the obstales list */
  for (unsigned int count1 = 0; count1 < workers.size(); count1++) 
  {
    worker_t wk  = workers[count1];
    for (unsigned int count2 = 0; count2 < wk.looptraj.size(); count2++)
      obs.push_back (wk.looptraj[count2]);
  }  
}


void readWorkspace (workspace_t &workspace, pos_vec_t &ob, worker_vec_t &workers)
{
  ifstream ifp;
  string line;
  pos_vec_t free_pos;
  ifp.open("../examples/workspace.txt");

  if (ifp.is_open())
  {
    getline(ifp, line);
    istringstream (line) >> workspace.length_x;

    getline(ifp, line);
    istringstream (line) >> workspace.length_y;

    getline(ifp, line);
    istringstream (line) >> workspace.number_of_wrobs;

    getline(ifp, line);
    istringstream (line) >> workspace.hlen;

    getline(ifp, line);
    istringstream (line) >> workspace.recharge;

    getline(ifp, line);
    istringstream (line) >> workspace.number_of_rechs;

/*
    getline(ifp, line);
    location = line.find(' ');
    istringstream (line.substr(0, location)) >> pos_tmp.x;
    istringstream (line.substr(location + 1)) >> pos_tmp.y;
    workspace.rpos_start = pos_tmp;
*/
    for(unsigned int i=1; i<=workspace.number_of_wrobs; i++)
    {
	stringstream ss;
	ss << "rob" << i << "_traj.txt";
	string filename = ss.str();
	
	worker_t worker = readWorkerUtil(filename);
	workers.push_back(worker);
    }
/*
    getline(ifp, line);
    workspace.total_cost = line;
    for(unsigned int i=0; i<=workspace.length_x; i++)
    {
      for(unsigned int j=0; j<=workspace.length_y; j++)
      {
	pos_tmp.x = i; pos_tmp.y = j;
	flag = find_pos(ob, pos_tmp);
	if(!flag)
	{
	  //non_obs <<  i << " " << j << endl;
	  //workspace.pos_start[count] = pos_tmp;
	  free_pos.push_back(pos_tmp);
	  count++;
	}
      }
   }

   workspace.pos_start = new position[count];
   for(int i=0; i<count; i++)
   {
	workspace.pos_start[i] = free_pos[i];
   }
   workspace.number_of_uavs = count;
  }
*/
  }
  ifp.close();
  cout << "dimension = " << workspace.length_x+1 << "*" << workspace.length_y+1 << endl;
  cout << "number of workers = " << workspace.number_of_wrobs << endl;
  cout << "hyperloop length = " << workspace.hlen << endl;
  cout << "max. recharge amt.  = " << workspace.recharge << endl;
  cout << "number of rechargers = " << workspace.number_of_rechs << endl;
}


worker_t readWorkerUtil(string filename)
{
  ifstream ifp;
  string line;
  position pos_tmp;
  worker_t worker;
  unsigned int count;
  int location, charge;

  ifp.open(filename.c_str());
  if (ifp.is_open())
  {	
	getline(ifp, line);
	istringstream (line) >> worker.fch;
	getline(ifp, line);
	istringstream (line) >> worker.looplen;

	for (count=1; count<=worker.looplen; count++)
	{
	  getline(ifp, line);
	  location = line.find(' ');
	  istringstream (line.substr(0, location)) >> pos_tmp.x;
	  istringstream (line.substr(location + 1)) >> pos_tmp.y;
	  worker.looptraj.push_back(pos_tmp);
	}

	for (count=1; count<=worker.looplen; count++)
	{
	  getline(ifp, line);
	  istringstream (line) >> charge;
	  worker.req_charge.push_back (charge);
	}
  }
  ifp.close();
  worker.wpos_start = worker.looptraj[0];
  return worker;
}


void writePrimitives(prim_vec_t primitives)
{
  unsigned int count1, count2;
  state q_i, q_f;
  position pos_f;
  string cost;
  pos_vec_t swath;
  position pos_min;
  position pos_max;

  cout << endl << "PRIMITIVES:" << endl << endl;
  for(count1 = 0; count1 < primitives.size(); count1++)
  {
    cout << "Primitive " << count1 << endl;

    q_i = primitives[count1].get_q_i();
    cout << "q_i: " << q_i.velocity << endl;

    q_f = primitives[count1].get_q_f();
    cout << "q_f: " << q_f.velocity << endl;

    pos_f = primitives[count1].get_pos_f();
    cout << "pos_f: " << pos_f.x << " " << pos_f.y << endl;

    cost = primitives[count1].get_cost();
    cout << "cost: " << cost << endl;

    swath = primitives[count1].get_swath();
    cout << "swath: ";
    for(count2 = 0; count2 < swath.size(); count2++)
    {
      cout << swath[count2].x << " " << swath[count2].y << " | ";
    }
    cout << endl;
    
    pos_min = primitives[count1].get_pos_min();
    cout << "pos_min: " << pos_min.x << " " << pos_min.y << endl;

    pos_max = primitives[count1].get_pos_max();
    cout << "pos_max: " << pos_max.x << " " << pos_max.y << endl;

    cout << endl;
  }
}


/* reads recharge instances -- trajectory point (x,y) where recharge took place */
/*rechinst_vec_t readRechInstances_trajpt (rechinst_vec_t &rechinstances, string filename)
{
   ifstream ifp;
   string line, str, strx, stry;
   stringstream ss;
   unsigned int loc, i=0, strlen;

   ifp.open(filename.c_str());
   if (ifp.is_open())
   {
     strx = "((rx_"; stry = "((ry_";
     while (getline(ifp,line) && i<rechinstances.size())
     {
       if (line.find(strx) != string::npos)
       {
         ss.str("");
         ss << strx << rechinstances[i].timept;
         str = ss.str(); strlen = str.length();
         if (line.find(str) != string::npos)
         {
           loc = line.find(")");
           str = line.substr(strlen+1, loc-strlen-1);
           istringstream (str) >> rechinstances[i].trajpt.x;

           getline(ifp, line); // for y component of pos
           ss.str("");
           ss << stry << rechinstances[i].timept; str = ss.str(); strlen = str.length();
           loc = line.find(")");
           str = line.substr(strlen+1, loc-strlen-1);
           istringstream (str) >> rechinstances[i].trajpt.y;
           cout << "TESTTTT RECHINSTT for worker-" << rechinstances[i].worker_id << " (" << rechinstances[i].trajpt.x << " " << rechinstances[i].trajpt.y << ")"<< endl;
           
           i++;
         }
       }
     }  
   }
   return rechinstances;
}*/


/* Reads recharge instances -- worker_id, timept, recharger position */
string readRechInstances (rechinst_vec_t &rechinstances, worker_vec_t workers, string filename) //change15
{
  ifstream ifp;
  string line;
  rechinst_t rechinst;
  unsigned int check_rech;
  unsigned int first, last, loc;
  
  ifp.open(filename.c_str());
  if (ifp.is_open())
  {
    while (getline(ifp,line))
    {
      if (line.find ("((rechcount_") != string::npos)
      {
        loc = line.find(" ");
        istringstream (line.substr (loc+1, 1)) >> check_rech;
        if (check_rech == 1)
        {
          first = line.find_first_of ("_"); last = line.find_last_of("_");
          istringstream (line.substr (first+1, last-first-1)) >> rechinst.worker_id;
          istringstream (line.substr (last+1, loc-last-1)) >> rechinst.timept;

          rechinstances.push_back (rechinst);
        }
      }
    }
  }
  ifp.close();
  
  unsigned int i = 0;
  stringstream ss, ss1;
  string strx, stry, str;
  unsigned int rt, rw;

  ss.str("");
  str = ss.str();
  
  for (i=0; i<rechinstances.size(); i++)
  {
    rt = rechinstances[i].timept;
    rw = rechinstances[i].worker_id;
     ss << "((rechassigned_" << rw << "_" << rt << " ";
     str = ss.str(); ss.str("");
    rechinstances[i].rech_id = readValue (str, filename);
    rechinstances[i].trajpt = readRechargerPosition (filename, rechinstances[i].rech_id, rt);

    ss1 << "worker-" << rechinstances[i].worker_id << ", timept = " << rechinstances[i].timept << ", pos (" << rechinstances[i].trajpt.x << " " << rechinstances[i].trajpt.y << "), recharger-" << rechinstances[i].rech_id << endl;
  }
  cout << ss1.str();
  return ss1.str();
/*
   i = 0;

   for (unsigned int count=0; count < rechinstances.size(); count++)
   {
   ifp.open(filename.c_str());
   if (ifp.is_open())
   {
     strx = "((rx_"; stry = "((ry_";
     while (getline(ifp,line))
     {
         ss.str("");
         ss << strx << rechinstances[count].timept;
         str = ss.str(); strlen = str.length();
         cout << "test string : " << str << endl;
         
         if (line.find(str) != string::npos)
         {
           loc = line.find(")");
           str = line.substr(strlen+1, loc-strlen-1);
           istringstream (str) >> rechinstances[count].trajpt.x;

           getline(ifp, line); // for y component of pos
           ss.str("");
           loc = line.find(")");
           str = line.substr(strlen+1, loc-strlen-1);
           istringstream (str) >> rechinstances[count].trajpt.y;

           cout << "TESTTTT RECHINSTT for worker-" << rechinstances[count].worker_id << " (" << rechinstances[count].trajpt.x << " " << rechinstances[count].trajpt.y << ")"<< endl;
           
           count++;
         }
       
     }
   }
   ifp.close();
  }
*/
}


/* Reads recharger's position at the given trajectory sequence */
position readRechargerPosition (string filename, unsigned int robid, unsigned int trajseq) //change15
{
  ifstream ifp;
  string line, strx, stry;
  unsigned int k,strlen;
  stringstream ss;
  position pos;

  ss << "((rx_" << robid << "_" << trajseq << " "; strx = ss.str(); ss.str("");
  ss << "((ry_" << robid << "_" << trajseq << " "; stry = ss.str();
  strlen = strx.length();

  ifp.open (filename.c_str());
  if (ifp.is_open())
  {
    while (getline(ifp, line))
    {
      k = line.find(")");
      if (line.find(strx) != string::npos)
      {
        istringstream (line.substr (strlen, k-strlen)) >> pos.x;
      }
      else if (line.find(stry) != string::npos)
      {
        istringstream (line.substr (strlen, k-strlen)) >> pos.y;
      }
    }
  }
  ifp.close();
  return pos;
}


/* Gets Final halt details of a single worker -- worker_id, timept, charge and duration */
workerhalt_t getWChargeDetails (string str, worker_vec_t workers, workspace_t workspace)
{
  unsigned int loc1, loc2;
  workerhalt_t chd;

  loc1 = str.find (" ");
  loc2 = str.find (")");
  istringstream (str.substr (loc1+1, loc2-loc1-1)) >> chd.charge;

  loc2 = str.find_last_of ("_");
  istringstream (str.substr (loc2+1, loc1-loc2-1)) >> chd.timept;
 
  loc1 = str.find_first_of ("_");
  istringstream (str.substr (loc1+1, loc2-loc1-1)) >> chd.worker_id;

  chd.duration =  ceil ((double) (workers[chd.worker_id-1].fch - chd.charge) / workspace.recharge);
  return chd;
}


/* checks if two workers have same charge after they do final halt */
unsigned int isWSameChargeValue (string str1, string str2, worker_vec_t workers, workspace_t workspace)
{
  workerhalt_t charge_det1, charge_det2;
  charge_det1 = getWChargeDetails (str1, workers, workspace);
  charge_det2 = getWChargeDetails (str2, workers, workspace);

  return ((charge_det1.charge == charge_det2.charge) ? 1 : 0);
}


/* Reads final halt details of all the workers */
string readWorkerHaltDetails (workerhalt_vec_t &workerhalt, workspace_t workspace, worker_vec_t workers, string filename)
{
  ifstream ifp;
  workerhalt_t wh;
  string line, str, str1, str2, str_curr, str_next;
  stringstream ss;
  unsigned int count1, flag, a, b;

  ifp.open(filename.c_str());
  if (ifp.is_open())
  {
    getline (ifp, str1);
    for (count1 = 0; count1 < workspace.number_of_wrobs; count1++)
    { 
      ss.str("");
      ss << "((ch_" << count1+1; str = ss.str();
      flag = 0;

      while (getline (ifp, str2))
      {
        if ((str1.find(str) != string::npos) && (str2.find(str) != string::npos))
        {
            if (isWSameChargeValue (str1, str2, workers, workspace) == 0)
            {
              str_curr = str1; str_next = str2;
            }
            str1 = str2;
            flag = 1;
        }
        else if (flag)
        {
            wh = getWChargeDetails (str_next, workers, workspace);
            //change 12
	    //for (unsigned int count2=1; count2<=wh.duration; count2++)
            //{
            //   wh.timept = wh.timept+count2-1;
               workerhalt.push_back (wh);
            //}
            // change 12
            str1 = str2;
            break;
        }
        else
        {
            str1 = str2;
        }
       }
      }
    }
    ifp.close();

    ss.str("");
    workerhalt_t w;
    for (count1=0; count1<workerhalt.size(); count1++)
    {
      w = workerhalt[count1];
      a = workers[w.worker_id-1].wpos_start.x;
      b = workers[w.worker_id-1].wpos_start.y;
      
      ss << "Last rech of worker " << w.worker_id << " @ t_" << w.timept << " : (" << a << " " << b << ") --> " << w.duration << " unit(s) | ";
      ss << "remaining charge : " << w.charge << endl;
    }
    ss << endl << "=======================================================" << endl;
    cout << ss.str();
    return ss.str();
}


/* writes final halt details of the workers */
void writeWChargeDetails (workerhalt_vec_t workerhalt)
{
  unsigned int count1;
  cout << "Writing worker charge details ..." << endl;
  for (count1 = 0; count1 < workerhalt.size(); count1++)
  {
    workerhalt_t w = workerhalt[count1];
    cout << endl << "rob : " << w.worker_id << endl;
    cout << "timept : " << w.timept << endl;
    cout << "charge : " << w.charge << endl;
    cout << "duration : " << w.duration << endl;
  }
}


/* Reads trajectory of a robot (depending on robstr) up to length trajlen*/
pos_vec_t readWorkingTraj (string filename, string robstrx, string robstry, unsigned int trajlen)
{
  ifstream ifp;
  pos_vec_t robtraj;
  string line, strx, stry, rcost;
  unsigned int k,strlen,flag=0;
  stringstream ss;
  position pos;

  for (unsigned int trajseq=1; trajseq <= trajlen; trajseq++)
  {
   ss << robstrx << trajseq << " "; // ex : robstrx = "((rx_" or "((wx_2_"
   strx = ss.str(); ss.str("");
   ss << robstry << trajseq << " "; // ex : robstry = "((ry_" or "((wy_2_"
   stry = ss.str(); ss.str("");
   strlen = strx.length(); // same as stry.length()
   rcost = "((total_rcost ";

   ifp.open (filename.c_str());
   if (ifp.is_open())
   {
     while (getline(ifp, line))
     {
       k = line.find(")"); 
       if (line.find(strx) != string::npos)
       {
         flag = 1; 
         istringstream (line.substr (strlen, k-strlen)) >> pos.x;
         getline (ifp, line);
         k = line.find(")");
         istringstream (line.substr (strlen, k-strlen)) >> pos.y;
       }
       if (flag)
       {
         robtraj.push_back(pos);
         flag = 0;
       }
     }
   }
   ifp.close();
 }
 return robtraj;
}


string writeWorkingTraj (worker_vec_t workers)
{
  pos_vec_t wt;
  stringstream ss;
  for(unsigned int count=0; count<workers.size(); count++)
  {
    wt = workers[count].workingtraj;
    //cout << "printing working traj for worker - " << count+1 << " of size " << wt.size() << endl;
    ss << "printing working traj for worker - " << count+1 << " of size " << wt.size() << endl;
    for (unsigned int count1=0; count1 < wt.size(); count1++)
    {
      //cout << "(" << wt[count1].x << " " << wt[count1].y << ") --> ";
      ss << "(" << wt[count1].x << " " << wt[count1].y << ") --> ";
    }
    //cout << "End" << endl << endl;
    ss << "End" << endl << endl;
  }
  //cout << ss.str();
  return ss.str();
}

/*
string getRechargerTraj (string filename, unsigned int robid) //change15
{
  ifstream ifp;
  pos_vec_t traj2, traj3, recharger_traj;
  unsigned int count=1,k;
  position pos;
  stringstream ss;
  string line;
  
  ss.str(""); ss << "((rx_" << robid << "_"; string robstrx = ss.str();
  unsigned int strlen;

  ifp.open(filename.c_str());
  if (ifp.is_open())
  {
    while (getline (ifp, line))
    {
      if (line.find (robstrx) != string::npos)
      {
        ss.str(""); ss << "((rx_" << robid << "_";
        ss << count << " "; strlen = ss.str().length();
        k = line.find(")");
        istringstream (line.substr (strlen, k-strlen)) >> pos.x;

        getline(ifp,line);
        k = line.find(")");
        istringstream (line.substr (strlen, k-strlen)) >> pos.y;

        recharger_traj.push_back(pos);
        count++;
      }
    }
  }
  ss.str("");
  ss << "printing recharger traj of size : " << recharger_traj.size()<< endl;
  for (count=0; count < recharger_traj.size(); count++)
  {
    //cout << "(" << recharger_traj[count].x << " " << recharger_traj[count].y << ") --> ";
    ss << "(" << recharger_traj[count].x << " " << recharger_traj[count].y << ") --> ";
  }
  //cout << "End" << endl;
  ss << "End" << endl;
  return ss.str();
}
*/

string getRechargerTraj (string filename, unsigned int robid) //change15
{
  ifstream ifp;
  pos_vec_t traj2, traj3, recharger_traj;
  unsigned int count=1,k;
  position pos;
  stringstream ss;
  string line;

  ss.str(""); ss << "((rx_" << robid << "_"; string robstrx = ss.str();
  unsigned int strlen;

  ifp.open(filename.c_str());
  if (ifp.is_open())
  {
    while (getline (ifp, line))
    {
      if (line.find (robstrx) != string::npos)
      {
        ss.str(""); ss << "((rx_" << robid << "_";
        ss << count << " "; strlen = ss.str().length();
        k = line.find(")");
        istringstream (line.substr (strlen, k-strlen)) >> pos.x;

        getline(ifp,line);
        k = line.find(")");
        istringstream (line.substr (strlen, k-strlen)) >> pos.y;
        
        recharger_traj.push_back(pos);
        count++;
      }
    }
  }
  ss.str("");
  ss << "printing recharger traj of size : " << recharger_traj.size()<< endl;
  for (count=0; count < recharger_traj.size(); count++)
  {
    //cout << "(" << recharger_traj[count].x << " " << recharger_traj[count].y << ") --> ";
    ss << "(" << recharger_traj[count].x << " " << recharger_traj[count].y << ") --> ";
  }
  //cout << "End" << endl;
  ss << "End" << endl;
  return ss.str();
}


/* reads a value corresponding to a string (with following <space>) */
unsigned int readValue (string simplestr, string filename)
{
  ifstream ifp;
  string line;
  int val=0, s, n;

  s = simplestr.length();
 
  ifp.open (filename.c_str());
  if (ifp.is_open())
  {
     while (getline (ifp, line))
     {
       n = line.find(")") - s;
       if (line.find (simplestr) != string::npos)
       {
         istringstream (line.substr (s,n)) >> val;
         break;
       }
     }
  }
  ifp.close();
  return val;
}


unsigned int tot_wait_upto_halt (string simplestr, string filename, unsigned int ext_hyp, unsigned int nwrobs)
{
  ifstream ifp;
  string line;
  int val;
  int tot_int_wait=0;
  stringstream ss;
  //s = simplestr.length();
  for (unsigned int count=1; count<=nwrobs; count++) 
  {
    //int nwrobs = log(count)+1; // number of digits
    for (unsigned int count1=1; count1 <= ext_hyp; count1++)
    {
      ss.str(""); ss << "((waitcount_" << count << "_" << count1 << " "; 
      string mystr = ss.str();
/*
      int ext_hyp_len = log(count1)+1;
      int tot_strlen = s + nwrobs + ext_hyp_len + 3;
      n = line.find(")") - tot_strlen;

      if (line.find (simplestr) != string::npos)
      {
        istringstream (line.substr (tot_strlen, n)) >> val;
        if (val)
          tot_int_wait++;
        
      }
    }
  }
*/
      val = readValue (mystr, filename);
      if(val)
        tot_int_wait++;
     }
  }
  return tot_int_wait;
}

/*
void matlab_code_generator (pos_vec_t ob, worker_vec_t workers, vector<pos_vec_t> rech_trajs)
{
  ofstream ofp;
  stringstream ss;
  string filename;
  
  //ss << "rss_inflated_traj_" << workers.size() << "_" << rechtraj.size() << ".m";
  ss << "iros_traj_w" << workers.size() << "_r" << rech_trajs.size() << "_.m";
  filename = ss.str();
  ofp.open(filename.c_str());

  ofp << "clear all; close all;" << endl;
  ofp << "dim_x = 19; dim_y = 19;" << endl;
  ofp << "axis([-1 dim_x -1 dim_y]);" << endl; 
  ofp << "rectangle('Position', [0, 0, dim_x, dim_y], 'linewidth', 2);" << endl << endl;

  ofp << "for i=0:(dim_y-1)" << endl;
  ofp << "  rectangle('Position', [0, i, dim_x, 1]);" << endl;
  ofp << "end" << endl << endl;

  ofp << "for i=0:(dim_x-1)" << endl;
  ofp << "  rectangle('Position', [i, 0, 1, dim_y]);" << endl;
  ofp << "end" << endl << endl;

  ofp << "hold on;" << endl;
  for (unsigned int i=0; i<ob.size(); i++)
  {
    ofp << "rectangle ('Position', [" << ob[i].x << ", " << ob[i].y << ", 1, 1], 'facecolor', 'black');" << endl;
  }
  //ofp << "rectangle('Position',[3, 3, 1, 1], 'facecolor', 'black');" << endl; 

  ofp << "hold on;" << endl << endl;

  unsigned int actual_hyp, ext_hyp, count1, count2,  count3;
  unsigned int wx1, wy1, wx2, wy2, wx3, wy3, wx4, wy4, rx1, ry1, rx2, ry2;
  actual_hyp = workers[0].workingtraj.size();
  ext_hyp = rech_trajs[0].size();

  cout << "IN MATLAB GENERATOR : actual_hyp " << actual_hyp << " ext_hyp " << ext_hyp << endl;

  for (count1 = 0; count1 < actual_hyp; count1++)
  {
    wx1 = workers[0].workingtraj[count1].x;
    wy1 = workers[0].workingtraj[count1].y;
    wx2 = workers[1].workingtraj[count1].x;
    wy2 = workers[1].workingtraj[count1].y;
    wx3 = workers[2].workingtraj[count1].x;
    wy3 = workers[2].workingtraj[count1].y;
    wx4 = workers[3].workingtraj[count1].x;
    wy4 = workers[3].workingtraj[count1].y;
   
    rx1 = (rech_trajs[0])[count1].x;
    ry1 = (rech_trajs[0])[count1].y;
    rx2 = (rech_trajs[1])[count1].x;
    ry2 = (rech_trajs[1])[count1].y;

    ofp << "% traj=" << count1+1 << endl; 
    ofp << "plot_robs_2 (" << wx1 << ", " << wy1 << ", " << wx2 << ", " << wy2 << ", " << wx3 << ", " << wy3 << ", " << wx4 << ", " << wy4 << ", " << rx1 << ", " << ry1 << ", " << rx2 << ", " << ry2 << ", 7)" << endl;
    ofp << "pause(0.5);";
    ofp << "erase_2 (" << wx1 << ", " << wy1 << ", " << wx2 << ", " << wy2 << ", " << wx3 << ", " << wy3 << ", " << wx4 << ", " << wy4 << ", " << rx1 << ", " << ry1 << ", " << rx2 << ", " << ry2 << ")" << endl;
  }
  
  unsigned int wtrajlen = workers[0].workingtraj.size();
  for (count1 = actual_hyp; count1 < ext_hyp; count1++)
  {
    wx1 = workers[0].workingtraj[wtrajlen-1].x;
    wy1 = workers[0].workingtraj[wtrajlen-1].y;
    wx2 = workers[1].workingtraj[wtrajlen-1].x;
    wy2 = workers[1].workingtraj[wtrajlen-1].y;
    wx3 = workers[2].workingtraj[wtrajlen-1].x;
    wy3 = workers[2].workingtraj[wtrajlen-1].y;
    wx4 = workers[3].workingtraj[wtrajlen-1].x;
    wy4 = workers[3].workingtraj[wtrajlen-1].y;

    rx1 = (rech_trajs[0])[count1].x;
    ry1 = (rech_trajs[0])[count1].y;
    rx2 = (rech_trajs[1])[count1].x;
    ry2 = (rech_trajs[1])[count1].y;

    ofp << "% traj=" << count1+1 << endl;
    ofp << "plot_robs_2 (" << wx1 << ", " << wy1 << ", " << wx2 << ", " << wy2 << ", " << wx3 << ", " << wy3 << ", " << wx4 << ", " << wy4 << ", " << rx1 << ", " << ry1 << ", " << rx2 << ", " << ry2 << ", 7)" << endl;
    ofp << "pause(0.5);";
    ofp << "erase (" << wx1 << ", " << wy1 << ", " << wx2 << ", " << wy2 << ", " << wx3 << ", " << wy3 << ", " << wx4 << ", " << wy4 << ", " << rx1 << ", " << ry1 << ", " << rx2 << ", " << ry2 << ")" << endl;

  }
}*/

