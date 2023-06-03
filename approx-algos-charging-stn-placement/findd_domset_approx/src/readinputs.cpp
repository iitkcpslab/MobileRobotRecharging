#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <set>
#include <math.h>
#include <stdlib.h>
#include "primitive.h"
#include "readinputs.h"
using namespace std;


set<int> getVelocityDistinct (prim_vec_t prims)
{
  set<int> velset;

  for(unsigned int i=0; i<prims.size(); i++)
  {
    velset.insert(prims[i].get_q_i().velocity);
    velset.insert(prims[i].get_q_f().velocity);
  }
  return velset;
}


void printVelocityDistinct (set<int> velset)
{
  set<int>::iterator it = velset.begin();
  for( ;it!=velset.end(); it++)
  {
    cout << *it << "  ";
  }
  cout << endl;
}


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


pos_vec_t findBoundaryPoints(workspace_t workspace, pos_vec_t obstacles)
{
  pos_vec_t boundary;
  for(int count1 = 0; count1 < workspace.number_of_locs; count1++)
  {
        position p, p1, p2, p3, p4;
        p = workspace.pos_start[count1];
        p1.x = p.x + 1; p1.y = p.y;
        p2.x = p.x - 1; p2.y = p.y;
        p3.x = p.x; p3.y = p.y + 1;
        p4.x = p.x; p4.y = p.y - 1;

        if(!find_pos(obstacles,p) && ( find_pos(obstacles,p1) || find_pos(obstacles,p2) || find_pos(obstacles,p3) || find_pos(obstacles,p4) ) )
        {
           boundary.push_back(p);
        }
     //}
  }
  cout << "workspace boundary points : " << boundary.size() << endl;
  return boundary;
}


void readObstacles(pos_vec_t &obstacles)
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
      location = line.find(' ');
      istringstream (line.substr(0, location)) >> pos_tmp.x;
      istringstream (line.substr(location + 1)) >> pos_tmp.y;
      obstacles.push_back(pos_tmp);
    }
  }
  ifp.close();
}


void writePositions (pos_vec_t obstacles)
{
  for (unsigned int count=0; count<obstacles.size(); count++)
    cout << obstacles[count].x << " " << obstacles[count].y << " -> ";

  cout << "total count = " << obstacles.size() << endl;
}


int find_pos(pos_vec_t pos_vec, position pos)
{
  pos_vec_t::iterator beg = pos_vec.begin();
  for(;beg!=pos_vec.end();beg++)
  {
    if((*beg).x==pos.x && (*beg).y==pos.y)
    {
      //cout << endl << "obstacle is "<< pos.x << " " << pos.y << endl;
      return 1;
    }
  }
  return 0;
}


pos_vec_t getFreeLocations (workspace_t workspace, pos_vec_t ob)
{
    position pos_tmp;
    pos_vec_t free_locs;
    unsigned int count=0;
    int flag;
    for(unsigned int count1 = 0; count1 <= workspace.length_x; count1++)
    {
      for(unsigned int count2 = 0; count2 <= workspace.length_y; count2++)
      {
        pos_tmp.x = count1; pos_tmp.y = count2;
        flag = find_pos(ob, pos_tmp);
        if(!flag)
        {
          //non_obs <<  i << " " << j << endl;
          //workspace.pos_start[count] = pos_tmp;
          free_locs.push_back(pos_tmp);
          count++;
        }
      }
   }
   return free_locs;
}


void readWorkspace (workspace_t &workspace, pos_vec_t ob)
{
  ifstream ifp;
  string line;
  pos_vec_t free_pos;
  position pos_tmp;
  int flag=0, count=0;
  
  ifp.open("../examples/workspace.txt");

  if (ifp.is_open())
  {
    getline(ifp, line);
    istringstream (line) >> workspace.length_x;

    getline(ifp, line);
    istringstream (line) >> workspace.length_y;

    getline(ifp, line);
    istringstream (line) >> workspace.ncs;

    for(unsigned int i=0; i<=workspace.length_x; i++)
    {
      for(unsigned int j=0; j<=workspace.length_y; j++)
      {
        pos_tmp.x = i; pos_tmp.y = j;
        flag = find_pos(ob, pos_tmp);
        if(!flag)
        {
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
   workspace.number_of_locs = count;
  }
  ifp.close();

  return;
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


