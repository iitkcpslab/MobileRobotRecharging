/* License */
/*
Copyright (c) <2014>, <Indranil Saha>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/


#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include "primitive.h"
#include "readinputs.h"
#include "writeconstraints.h"


void declareVariables(ofstream &ofp, workspace_t workspace)
{
  unsigned int count, count1, count2;

  ofp << "(declare-fun obstacle (Int Int) Bool)" << endl;
  ofp << endl;
  for (count = 0; count < workspace.number_of_cs; count++)
  {
  	ofp << "(declare-const destx" << count + 1 <<" Int)" << endl;
  	ofp << "(declare-const desty" << count + 1 <<" Int)" << endl;
  }
  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points - 1; count2++)
    {
      ofp << "(declare-const prim_" << count1 + 1 << "_" << count2 + 1 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points; count2++)
    {
      ofp << "(declare-const x_" << count1 + 1 << "_" << count2 + 1 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points; count2++)
    {
      ofp << "(declare-const y_" << count1 + 1 << "_" << count2 + 1 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points - 1; count2++)
    {
      ofp << "(declare-const vel_i_" << count1 + 1 << "_" << count2 + 1 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points - 1; count2++)
    {
      ofp << "(declare-const vel_f_" << count1 + 1 << "_" << count2 + 1 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points - 1; count2++)
    {
      ofp << "(declare-const x_f_" << count1 + 1 << "_" << count2 + 1 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points - 1; count2++)
    {
      ofp << "(declare-const y_f_" << count1 + 1 << "_" << count2 + 1 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points - 1; count2++)
    {
      ofp << "(declare-const cost_" << count1 + 1 << "_" << count2 + 1 << " Real)" << endl;
    }
  }
  ofp << endl;
}


void writeInitialLocationConstraints(ofstream &ofp, workspace_t workspace, pos_vec_t &ob)
{
  unsigned int count1, count2=0;
  
  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    int flag = find_pos(ob, workspace.pos_start[count1]);
    if(!flag)
    {
      /* count1 keeps track of any point (obstacle or non-obstacle); count2 is for non-obstacles only */
      ofp << "(assert (and (= x_" << count2 + 1 << "_1 " << workspace.pos_start[count1].x << ")" << endl;
      ofp << "  (= y_" << count2 + 1 << "_1 " << workspace.pos_start[count1].y << ")))" << endl;
      count2++;
    }
  }
  ofp << endl;
}


void writeFinalDestinationConstraints(ofstream &ofp, workspace_t workspace, prim_vec_t primitives, int delta)
{
  unsigned int count, count1, count3;
  state q_i, q_f;
  position pos_f;
  pos_vec_t swath, swath1, swath2;
  string cost;

  /* trajectory points on recharger's trajectory can be any free point on the workspace */
  for (count1 = 0; count1 < workspace.number_of_cs; count1++)
  {
    ofp << "(assert (and (>= destx" << count1 + 1 << " 0) (<= destx" << count1 + 1 << " " << workspace.length_x << ")))" << endl;
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_cs; count1++)
  {
    ofp << "(assert (and (>= desty" << count1 + 1 << " 0) (<= desty" << count1 + 1 << " " << workspace.length_y << ")))" << endl;
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_cs; count1++)
  {
    ofp << "(assert (= (obstacle destx" << count1 + 1 << " desty" << count1 + 1 << ") false))" << endl;
  }
  ofp << endl;

    /* perturb already existing CS in csvec; synthesize an all new location for the new CS */
/*
    if (count >= workspace.csvec.size())
    {
       destx1 = 0; destx2 = workspace.length_x; desty1 = 0; desty2 = workspace.length_y;     
    }
    else
    {
       destx1 = ((workspace.csvec)[count]).x - delta < 0 ? 0 : ((workspace.csvec)[count]).x - delta;
       destx2 = ((workspace.csvec)[count]).x + delta > workspace.length_x ? workspace.length_x : ((workspace.csvec)[count]).x + delta;
       desty1 = ((workspace.csvec)[count]).y - delta < 0 ? 0 : ((workspace.csvec)[count]).y - delta;
       desty2 = ((workspace.csvec)[count]).y + delta > workspace.length_y ? workspace.length_y : ((workspace.csvec)[count]).y + delta;
    }

    ofp << "(assert (and (>= destx" << count + 1 << " " << destx1 << ") (<= destx" << count + 1 << " " << destx2 << ")))" << endl;
    ofp << "(assert (and (>= desty" << count + 1 << " " << desty1 << ") (<= desty" << count + 1 << " " << desty2 << ")))" << endl;
*/

  /* at least one of the points on recharger's trajectory is reachable from any free location */
  for (count = 0; count < workspace.number_of_uavs; count++)
  {
    ofp << "(assert (! (or " << endl;
    for (count1 = 0; count1 < workspace.number_of_cs; count1++)
    {
      ofp << " (and (= x_" << count+1 << "_" << workspace.number_of_points << " destx" << count1+1 << ")" << endl;
      ofp << "      (= y_" << count+1 << "_" << workspace.number_of_points << " desty" << count1+1 << "))" << endl;
    }
    ofp << ") :named a" << workspace.pos_start[count].x << "_" << workspace.pos_start[count].y << "$" << "))" << endl;
  }
  ofp << endl;

  /* each location on the recharger's trajectory is connected with the previous location on the trajectory */
  int quot = workspace.number_of_cs;
  for (count1 = 0; count1 < workspace.number_of_cs-1; count1++)
  {
      ofp << "(assert (or" << endl;
      for (count = 0; count < primitives.size(); count++)
      {
        q_i = primitives[count].get_q_i();
        q_f = primitives[count].get_q_f();
        pos_f = primitives[count].get_pos_f();
        cost = primitives[count].get_cost();
        swath = primitives[count].get_swath();

	ofp << "  (and (= (+ destx" << (count1 % quot)+1 << " " << pos_f.x << ") destx" << (count1+1 % quot)+1 << ")" << endl;
	ofp << "       (= (+ desty" << (count1 % quot)+1 << " " << pos_f.y << ") desty" << (count1+1 % quot)+1 << ")" << endl;

	/* any primitive swath should not pass through obstacles */
        for (count3 = 0; swath.size()>2 && count3 < swath.size(); count3++)
        {
          ofp << "       (= (obstacle (+ destx" << count1+1 << " " << swath[count3].x << ") (+ desty" << count1+1 << " " << swath[count3].y << ")) false)" << endl;
        }
        ofp << "  )" << endl;
      }
      ofp << "))" << endl;
  }
  
  ofp << "(assert (and (= destx1 destx" << workspace.number_of_cs << ") (= desty1 desty" << workspace.number_of_cs << ")))"<< endl;
}


void writeTransitionConstraints(ofstream &ofp, prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace)
{
  state q_i, q_f;
  position pos_f;
  pos_vec_t swath, swath1, swath2;
  string cost;
  unsigned int count, count1, count2, count3;

  bool workspace_obstacles[workspace.length_x + 1][workspace.length_y + 1];

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

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    ofp << "(assert (= vel_i_" << count1 + 1 << "_1 0))" << endl;
    //ofp << "(assert (= vel_f_" << count1 + 1 << "_" << workspace.number_of_points - 1 << " 0))" << endl;
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points - 1; count2++)
    {
      ofp << "(assert (and (>= prim_" << count1 + 1 << "_" << count2 + 1 << " 1) (<= prim_" << count1 + 1 << "_" << count2 + 1 << " " << primitives.size() << ")))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 1; count2 < workspace.number_of_points - 1; count2++)
    {
      ofp << "(assert (and (>= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0) (<= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 8)))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points - 2; count2++)
    {
      ofp << "(assert (and (>= vel_f_" << count1 + 1 << "_" << count2 + 1 << " 0) (<= vel_f_" << count1 + 1 << "_" << count2 + 1 << " 8)))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points; count2++)
    {
      ofp << "(assert (and (>= x_" << count1 + 1 << "_" << count2 + 1 << " 0) (<= x_" << count1 + 1 << "_" << count2 + 1 << " " << workspace.length_x << ")))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points; count2++)
    {
      ofp << "(assert (and (>= y_" << count1 + 1 << "_" << count2 + 1 << " 0) (<= y_" << count1 + 1 << "_" << count2 + 1 << " " << workspace.length_y << ")))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 <= workspace.length_x; count1++)
  {
    for (count2 = 0; count2 <= workspace.length_y; count2++)
    {
      if (workspace_obstacles[count1][count2] == 0)
        ofp << "(assert (= (obstacle " << count1 << " " << count2 << ") " << "false" << "))" << endl;
        //ofp << "(assert (! (= (obstacle " << count1 << " " << count2 << ") " << "false" << ") :named obs_" << count1 << "_" << count2 << "))" << endl;
      else
        //ofp << "(assert (= (obstacle " << count1 << " " << count2 << ") " << "true" << "))" << endl;
        ofp << "(assert (! (= (obstacle " << count1 << " " << count2 << ") " << "true" << ") :named obs-" << count1 << "-" << count2 << "))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 0; count2 < workspace.number_of_points - 1; count2++)
    {
      for (count = 0; count < primitives.size(); count++)
      {
        q_i = primitives[count].get_q_i();
        q_f = primitives[count].get_q_f();
        pos_f = primitives[count].get_pos_f();
        cost = primitives[count].get_cost();
        swath = primitives[count].get_swath();
        ofp << "(assert (or (not (= prim_" << count1 + 1 << "_" << count2 + 1 << " " << count + 1 << "))" << endl;
        ofp << "(and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " " << q_i.velocity << ")" << endl;
        ofp << "     (= vel_f_" << count1 + 1 << "_" << count2 + 1 << " " << q_f.velocity << ")" << endl;
        ofp << "     (= x_f_" << count1 + 1 << "_" << count2 + 1 << " " << pos_f.x << ")" << endl;
        ofp << "     (= y_f_" << count1 + 1 << "_" << count2 + 1 << " " << pos_f.y << ")" << endl;
        ofp << "     (= cost_" << count1 + 1 << "_" << count2 + 1 << " " << floatToReal(cost) << ")" << endl;
        for (count3 = 0; count3 < swath.size(); count3++)
        {
          ofp << "     (= (obstacle (+ x_" << count1 + 1 << "_" << count2 + 1 << " " << swath[count3].x << ") (+ y_" << count1 + 1 << "_" << count2 + 1 << " " << swath[count3].y << ")) false)" << endl;
        }
        ofp << ")))" << endl;
        //ofp << ")) :named tran_" << count1 + 1 << "_" << count2 + 1 << "_" << count + 1 << "))" << endl;
        ofp << endl;
      }
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 1; count2 < workspace.number_of_points; count2++)
    {
      ofp << "(assert (= x_" << count1 + 1 << "_" << count2 + 1 << " (+ x_" << count1 + 1 << "_" << count2 << " x_f_" << count1 + 1 << "_" << count2 << ")))" << endl;
      //ofp << "(assert (! (= x_" << count1 + 1 << "_" << count2 + 1 << " (+ x_" << count1 + 1 << "_" << count2 << " x_f_" << count1 + 1 << "_" << count2 << ")) :named xmatch_" << count1 << "_" << count2 << "))" << endl;
      ofp << "(assert (= y_" << count1 + 1 << "_" << count2 + 1 << " (+ y_" << count1 + 1 << "_" << count2 << " y_f_" << count1 + 1 << "_" << count2 << ")))" << endl;
      //ofp << "(assert (! (= y_" << count1 + 1 << "_" << count2 + 1 << " (+ y_" << count1 + 1 << "_" << count2 << " y_f_" << count1 + 1 << "_" << count2 << ")) :named ymatch_" << count1 << "_" << count2 << "))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    for (count2 = 1; count2 < workspace.number_of_points - 1; count2++)
    {
      ofp << "(assert (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " vel_f_" << count1 + 1 << "_" << count2 << "))" << endl;
      //ofp << "(assert (! (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " vel_f_" << count1 + 1 << "_" << count2 << ") :named velmatch_" << count1 << "_" << count2 << "))" << endl;
    }
  }
  ofp << endl;
}


void writeOutputConstraints(ofstream &ofp, workspace_t workspace)
{
	//unsigned int count1, count2;
	ofp << ";writeoutput constraint" << endl;
	//ofp << "(check-sat)" << endl;
	ofp << ";(get-model)" << endl;
	//ofp << "(get-value (destx)" << endl;
	//ofp << "(get-value (desty)" << endl;
	ofp << endl;
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