#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include "primitive.h"
#include "readinputs.h"
#include "writeconstraints_recharger.h"


void declareVariables_rechargers (ofstream &ofp, workspace_t workspace)
{
  unsigned int count1, count2;
  ofp << "(declare-fun obstacle (Int Int) Bool)" << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    { 
      ofp << "(declare-const rprim_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "(declare-const rcost_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;
  
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "(declare-const rx_f_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "(declare-const ry_f_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    { 
      ofp << "(declare-const rx_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;
 
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    { 
      ofp << "(declare-const ry_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  ofp << "(declare-const total_rcost" << " Int)" << endl << endl;
}


void writeTransitionConstraints_rechargers (ofstream &ofp, prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace, unsigned int max_timept)
{
  state q_i, q_f;
  position pos_f;
  pos_vec_t swath, swath1, swath2;
  string cost;
  unsigned int count, count1, count2, count3;
  bool workspace_obstacles[workspace.length_x + 1][workspace.length_y + 1];

  ofp << "; transition of rechargers" << endl;
  for (count1 = 0; count1 <= workspace.length_x; count1++)
  {
    for (count2 = 0; count2 <= workspace.length_y; count2++)
    { 
      workspace_obstacles[count1][count2] = false;
    }
  }
  for (count = 0; count < obstacles.size(); count++)
  {
    workspace_obstacles[obstacles[count].x][obstacles[count].y] = true;
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept-1; count2++)
    {
      ofp << "(assert (and (>= rprim_" << count1 << "_" << count2 << " 1) (<= rprim_" << count1 << "_" << count2 << " " << primitives.size() << ")))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    { 
      ofp << "(assert (and (>= rx_" << count1 << "_" << count2 << " " << workspace.min_x << ") (<= rx_" << count1 << "_" << count2 << " " << workspace.length_x << ")))" << endl;
    }
  }
  ofp << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 2; count2 <= max_timept; count2++)
    { 
      ofp << "(assert (and (>= ry_" << count1 << "_" << count2 << " " << workspace.min_y << ") (<= ry_" << count1 << "_" << count2 << " " << workspace.length_y << ")))" << endl;
    }
  }
  ofp << endl;
  for (count1 = 0; count1 <= workspace.length_x; count1++)
  {
    for (count2 = 0; count2 <= workspace.length_y; count2++)
    {
      if (workspace_obstacles[count1][count2] == 0) 
        ofp << "(assert (= (obstacle " << count1 << " " << count2 << ") " << "false" << "))" << endl;
      else
        ofp << "(assert (! (= (obstacle " << count1 << " " << count2 << ") " << "true" << ") :named obs_" << count1 << "_" << count2 << "))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept-1; count2++)
    {
      for (count = 0; count < primitives.size(); count++)
      {
        q_i = primitives[count].get_q_i();
        q_f = primitives[count].get_q_f();
        pos_f = primitives[count].get_pos_f();
        cost = primitives[count].get_cost();
        swath = primitives[count].get_swath();
        ofp << "(assert (or (not (= rprim_" << count1 << "_" << count2 << " " << count + 1 << "))" << endl;
        ofp << "  (and (= rx_f_" << count1 << "_" << count2 << " " << pos_f.x << ")" << endl;
        ofp << "     (= ry_f_" << count1 << "_" << count2 << " " << pos_f.y << ")" << endl;
        ofp << "     (= rcost_" << count1 << "_" << count2 << " " << floatToReal(cost) << ")" << endl;

        for (count3 = 0; count3 < swath.size(); count3++)
        {
          ofp << "     (= (obstacle (+ rx_" << count1 << "_" << count2 << " " << swath[count3].x << ") (+ ry_" << count1 << "_" << count2 << " " << swath[count3].y << ")) false)" << endl;
        }

        ofp << ")))" << endl;
        ofp << endl;
      }
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 < max_timept; count2++)
    {
      ofp << "(assert (= rx_" << count1 << "_" << count2 + 1 << " (+ rx_" << count1 << "_" << count2 << " rx_f_" << count1 << "_" << count2 << ")))" << endl;
      ofp << "(assert (= ry_" << count1 << "_" << count2 + 1 << " (+ ry_" << count1 << "_" << count2 << " ry_f_" << count1 << "_" << count2 << ")))" << endl;
    }
  }
  ofp << endl;
}


void writeCollisionAvoidanceConstraints (ofstream &ofp, prim_vec_t prims, workspace_t workspace)
{
  unsigned int count, count1, count2, count3;
  pos_vec_t swath;
  position pos_f;

  ofp << endl << "; collision avoidance" << endl;
  for (count = 1; count <= workspace.number_of_rechs; count++)
  {
   for (count1=1; count1<=workspace.number_of_wrobs; count1++)
   {
    for (count2=1; count2<=workspace.hlen-1; count2++)
    {
      for (count3=0; count3<prims.size(); count3++)
      {
        pos_f = prims[count3].get_pos_f();
	ofp << "(assert (=> (= rprim_" << count << "_" << count2 << " " << count3+1 << ") " << endl;
        ofp << "(not (and (= wx_" << count1 << "_" << count2+1 << " (+ rx_" << count << "_" << count2 << " " << pos_f.x << ")) ";
        ofp << "(= wy_" << count1 << "_" << count2+1 << " (+ ry_" << count << "_" << count2 << " " << pos_f.y << "))))" << endl;
        ofp << "))" << endl;
      }  
    }
  }
 }
}


void writeMatchingConstraints_rechargers (ofstream &ofp, workspace_t workspace, worker_vec_t workers)
{
  ofp << "(assert (and" << endl;
  for (unsigned int rid=1; rid<=workspace.number_of_rechs; rid++)
  {
    ofp << " (= rx_" << rid << "_1 rx_" << rid << "_" << workspace.hlen << ")";
    ofp << " (= ry_" << rid << "_1 ry_" << rid << "_" << workspace.hlen << ")" << endl;
  }
  ofp << "))"<< endl << endl;
}


void minimizeWaiting_rechargers (ofstream &ofp, workspace_t workspace, worker_vec_t workers, prim_vec_t prims)
{
  unsigned int count1, count2;
  /* minimize */
  ofp << "(assert (= total_rcost (+ " << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for(count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "rcost_" << count1 << "_" << count2 << endl;
    }
  }
  ofp << ")))" << endl;
  ofp << ";(minimize total_rcost)" << endl;
}


void writeOutputConstraints_rechargers (ofstream &ofp, workspace_t workspace)
{
  unsigned int count1, count2;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 0; count2 < workspace.hlen-1; count2++)
    {
      ofp << "(get-value (rprim_" << count1 << "_" << count2 + 1 << "))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    {
      ofp << "(get-value (rx_" << count1 << "_" << count2 << "))" << endl;
      ofp << "(get-value (ry_" << count1 << "_" << count2 << "))" << endl;
    }
  }
  ofp << endl;
  ofp << "(get-value (total_rcost))" << endl;
}


string floatToReal(string fls)
{
  float flf;
  string str1, str2;
  long int num, den;
  int length;
  int pos;

  istringstream (fls) >> flf;
  pos = fls.find('.');
  if (pos == -1)
  {
    return fls;
  }
  else
  {
    length = fls.length();
    den = pow(10, (length - pos));
    num = flf * den;
    str1 = tostr(num);
    str2 = tostr(den);
    return ("(/ " + str1 + " " + str2 + ")");
  }
}

template <typename T> string tostr(const T& t)
{
  ostringstream os;
  os << t;
  return os.str();
}
