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
  ofp << "# declaration : constants for rechargers" << endl;

  ofp << "obstacle = Function('obstacle', IntSort(), IntSort(), BoolSort())" << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    { 
      ofp << "rprim_" << count1 << "_" << count2 << " = Int('rprim_" << count1 << "_" << count2 << "')" << endl;
    }
  }

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "rcost_" << count1 << "_" << count2 << " = Int('rcost_" << count1 << "_" << count2 << "')" << endl;
    }
  }
  
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "rx_f_" << count1 << "_" << count2 << " = Int('rx_f_" << count1 << "_" << count2 << "')" << endl;
    }
  }

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "ry_f_" << count1 << "_" << count2 << " = Int('ry_f_" << count1 << "_" << count2 << "')" << endl;
    }
  }

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    { 
      ofp << "rx_" << count1 << "_" << count2 << " = Int('rx_" << count1 << "_" << count2 << "')" << endl;
    }
  }
 
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    { 
      ofp << "ry_" << count1 << "_" << count2 << " = Int('ry_" << count1 << "_" << count2 << "')" << endl;
    }
  }

  ofp << "total_rcost = Int('total_rcost')" << endl << endl;
}


void declareVariables_rechargers2 (ofstream &ofp, workspace_t workspace, workerhalt_vec_t workerhalt, unsigned int rstart_timept, unsigned int max_timept)
{
  unsigned int count1, count2;
  ofp << "# declaring recharger constraints" << endl;

  ofp << "obstacle = Function('obstacle', IntSort(), IntSort(), BoolSort())" << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = rstart_timept; count2 <= max_timept-1; count2++)
    { 
      ofp << "(declare-const rprim_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = rstart_timept; count2 <= max_timept-1; count2++)
    {
      ofp << "(declare-const rcost_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;
  
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = rstart_timept; count2 <= max_timept-1; count2++)
    {
      ofp << "(declare-const rx_f_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = rstart_timept; count2 <= max_timept-1; count2++)
    {
      ofp << "(declare-const ry_f_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = rstart_timept; count2 <= max_timept; count2++)
    { 
      ofp << "rx_" << count1 << "_" << count2 << " = Int('rx_" << count1 << "_" << count2 << "')" << endl;
    }
  }
  ofp << endl;
 
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = rstart_timept; count2 <= max_timept; count2++)
    { 
      ofp << "ry_" << count1 << "_" << count2 << " = Int('ry_" << count1 << "_" << count2 << "')" << endl;
    }
  }
  ofp << endl;

  //ofp << "(declare-const total_rcost" << " Int)" << endl << endl;
  ofp << "total_rcost = Int('total_rcost')" << endl << endl;
}


void writeTransitionConstraints_rechargers (ofstream &ofp, prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace, unsigned int max_timept)
{
  state q_i, q_f;
  position pos_f;
  pos_vec_t swath, swath1, swath2;
  string cost;
  unsigned int count, count1, count2, count3;
  bool workspace_obstacles[workspace.length_x + 1][workspace.length_y + 1];

  ofp << "# transition : rechargers" << endl;
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
      ofp << "s.add(";
      ofp << "rprim_" << count1 << "_" << count2 << ">=1, ";
      ofp << "rprim_" << count1 << "_" << count2 << "<=" << primitives.size() << ")" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    { 
      ofp << "s.add(";
      ofp << "rx_" << count1 << "_" << count2 << ">=" << workspace.min_x << ", ";
      ofp << "rx_" << count1 << "_" << count2 << "<=" << workspace.length_x << ")" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 2; count2 <= max_timept; count2++)
    { 
      ofp << "s.add(";
      ofp << "ry_" << count1 << "_" << count2 << ">=" << workspace.min_y << ", ";
      ofp << "ry_" << count1 << "_" << count2 << "<=" << workspace.length_y << ")" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 <= workspace.length_x; count1++)
  {
    for (count2 = 0; count2 <= workspace.length_y; count2++)
    {
      if (workspace_obstacles[count1][count2] == 0) 
	ofp << "s.add(obstacle(" << count1 << "," << count2 << ")==False)";
      else
	ofp << "s.add(obstacle(" << count1 << "," << count2 << ")==True)";
      ofp << endl;
    }
  }
  ofp << endl;

  ofp << "# motion primitives : rechargers" << endl;
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
	
  	ofp << "s.add(";
	ofp <<      "Or("; 
	ofp <<        "rprim_" << count1 << "_" << count2 << "!=" << count+1 << "," << endl;
	ofp <<        "And(";
	ofp <<          "rx_f_" << count1 << "_" << count2 << "==" << pos_f.x << ", ";
	ofp <<          "ry_f_" << count1 << "_" << count2 << "==" << pos_f.y << ", ";
	ofp <<          "rcost_" << count1 << "_" << count2 << "==" << floatToReal(cost) << ", " << endl;

	for (count3 = 0; count3 < swath.size(); count3++)
        {
	  ofp <<        "obstacle(rx_" << count1 << "_" << count2 << " + " << swath[count3].x << ", ";
	  ofp <<                 "ry_" << count1 << "_" << count2 << " + " << swath[count3].y << ")==False, " << endl;
        }
	ofp << ")))" << endl;
      }
    }
  }

  ofp << endl << "# transition : change rx and ry of rechargers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 < max_timept; count2++)
    {
      ofp << "s.add(";
      ofp << "rx_" << count1 << "_" << count2+1 << "==rx_" << count1 << "_" << count2 << " + ";
      ofp << "rx_f_" << count1 << "_" << count2 << ", ";

      ofp << "ry_" << count1 << "_" << count2+1 << "==ry_" << count1 << "_" << count2 << " + ";
      ofp << "ry_f_" << count1 << "_" << count2 << ")" << endl;
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


void writeCollisionAvoidanceConstraints_rechargers2 (ofstream &ofp, workspace_t workspace, worker_vec_t workers, unsigned int rstart_timept, unsigned int max_timept)
{
  unsigned int count, count1, count2, count3;
  worker_t wk;
  pos_vec_t wktr;
/*
  ofp << "; total_rcost" << endl;
  ofp << "(assert (= total_rcost (+ " << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for(count2 = 1; count2 <= max_timept-1; count2++)
    {
      ofp << "rcost_" << count1 << "_" << count2 << endl;
    }
  }
  ofp << endl;
  ofp << ")))" << endl << endl;
*/
  ofp << "; collision avoidance - 2nd phase - between rechargers and static workers" << endl;
  for (count = 1; count <= workspace.number_of_rechs; count++)
  {
    for (count1 = rstart_timept+1; count1 <= max_timept; count1++)
    {
      for (count2 = 0; count2 < workers.size(); count2++)
      {
        wk = workers[count2];
        ofp << "(assert (not (and (= rx_" << count << "_" << count1 << " " << wk.workingtraj[0].x << ") ";
        ofp << "(= ry_" << count << "_" << count1 << " " << wk.workingtraj[0].y << "))))" << endl;
      }
    }
  }

  for (count1 = rstart_timept+1; count1 <= max_timept; count1++)
  {
    for (count2 = 1; count2 <= workspace.number_of_rechs; count2++)
    {
      for (count3 = count2+1; count3 <= workspace.number_of_rechs; count3++)
      {
        ofp << "(assert (not" << endl;
        ofp << "  (and (= rx_" << count2 << "_" << count1 << " " << "(= rx_" << count3 << "_" << count1 << ")) ";
        ofp << "  (= ry_" << count2 << "_" << count1 << " " << "(= ry_" << count3 << "_" << count1 << "))))) ";
      }
    }
  }
}


void minimizeWaiting_rechargers (ofstream &ofp, workspace_t workspace, worker_vec_t workers)
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


void writeOutputConstraints_rechargers2 (ofstream &ofp, workspace_t workspace, workerhalt_vec_t workerhalt, unsigned int rstart_timept, unsigned int max_timept)
{
  unsigned int count1, count2;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = rstart_timept; count2 <= max_timept-1; count2++)
    {
      ofp << "(get-value (rprim_" << count1 << "_" << count2 << "))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = rstart_timept; count2 <= max_timept; count2++)
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
