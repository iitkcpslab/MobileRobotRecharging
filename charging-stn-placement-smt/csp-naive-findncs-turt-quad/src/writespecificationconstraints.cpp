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
#include <math.h>
#include "primitive.h"
#include "readinputs.h"
#include "writespecificationconstraints.h"


/* Functions for writing final destination constraints */

void writeFinalDestinationConstraints1(ofstream &ofp, workspace_t workspace)
{
  unsigned int count1;

  for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
  {
    ofp << "(assert (= x_" << count1 + 1 << "_" << workspace.number_of_points << " " << workspace.pos_end[count1].x << "))" << endl;
    ofp << "(assert (= y_" << count1 + 1 << "_" << workspace.number_of_points << " " << workspace.pos_end[count1].y << "))" << endl;
  }
  ofp << endl;
}


void writeFinalDestinationConstraints2(ofstream &ofp, workspace_t workspace)
{
  ofp << "(assert (>= x_1_" << workspace.number_of_points << " " << "16))" << endl;
  ofp << "(assert (<= x_1_" << workspace.number_of_points << " " << "18))" << endl;
  ofp << "(assert (>= x_2_" << workspace.number_of_points << " " << "16))" << endl;
  ofp << "(assert (<= x_2_" << workspace.number_of_points << " " << "18))" << endl;
  ofp << "(assert (>= y_1_" << workspace.number_of_points << " " << "8))" << endl;
  ofp << "(assert (<= y_1_" << workspace.number_of_points << " " << "10))" << endl;
  ofp << "(assert (>= y_2_" << workspace.number_of_points << " " << "8))" << endl;
  ofp << "(assert (<= y_2_" << workspace.number_of_points << " " << "10))" << endl;

  ofp << "(assert (>= x_3_" << workspace.number_of_points << " " << "14))" << endl;
  ofp << "(assert (<= x_3_" << workspace.number_of_points << " " << "16))" << endl;
  ofp << "(assert (>= x_4_" << workspace.number_of_points << " " << "14))" << endl;
  ofp << "(assert (<= x_4_" << workspace.number_of_points << " " << "16))" << endl;
  ofp << "(assert (>= y_3_" << workspace.number_of_points << " " << "8))" << endl;
  ofp << "(assert (<= y_3_" << workspace.number_of_points << " " << "10))" << endl;
  ofp << "(assert (>= y_4_" << workspace.number_of_points << " " << "8))" << endl;
  ofp << "(assert (<= y_4_" << workspace.number_of_points << " " << "10))" << endl;
  ofp << endl;
}



/* Functions for writing safe LTL constraints */

void writeFormationConstraints(ofstream &ofp, workspace_t workspace)
{
  unsigned int count, count1, count2;

  for (count = 1; count <= workspace.number_of_points; count++)
  {
    for (count1 = 1; count1 <= workspace.number_of_uavs; count1++)
    {
      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << "(declare-const gx_" << count << "_" << count1 << "_" << count2 << " Int)" << endl;
        }
      }
    }
  }
  ofp << endl;

  for (count = 1; count <= workspace.number_of_points; count++)
  {
    for (count1 = 1; count1 <= workspace.number_of_uavs; count1++)
    {
      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << "(declare-const gy_" << count << "_" << count1 << "_" << count2 << " Int)" << endl;
        }
      }
    }
  }
  ofp << endl;

  for (count = 1; count <= workspace.number_of_points; count++)
  {
    ofp << "(declare-const gx_total_" << count << " Int)" << endl;
    ofp << "(declare-const gy_total_" << count << " Int)" << endl;
  }
  ofp << endl;

  for (count = 1; count <= workspace.number_of_points; count++)
  {
    for (count1 = 1; count1 <= workspace.number_of_uavs; count1++)
    {
      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << "(assert (or (= gx_" << count << "_" << count1 << "_" << count2 << " 0)" << " (= gx_" << count << "_" << count1 << "_" << count2 << " 1)))" << endl;
        }
      }
    }
  }
  ofp << endl;

  for (count = 1; count <= workspace.number_of_points; count++)
  {
    for (count1 = 1; count1 <= workspace.number_of_uavs; count1++)
    {
      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << "(assert (or (= gy_" << count << "_" << count1 << "_" << count2 << " 0)" << " (= gy_" << count << "_" << count1 << "_" << count2 << " 1)))" << endl;
        }
      }
    }
  }
  ofp << endl;

  for (count = 1; count <= workspace.number_of_points; count++)
  {
    for (count1 = 1; count1 <= workspace.number_of_uavs; count1++)
    {
      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << "(assert (=> (= gx_" << count << "_" << count1 << "_" << count2 << " 1) (= x_" << count1 << "_" << count << " x_" << count2 << "_" << count << ")))" << endl;
          ofp << "(assert (=> (= x_" << count1 << "_" << count << " x_" << count2 << "_" << count << ") (= gx_" << count << "_" << count1 << "_" << count2 << " 1)))" << endl;
        }
      }

      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << "(assert (=> (= gx_" << count << "_" << count1 << "_" << count2 << " 1) (not (= y_" << count1 << "_" << count << " y_" << count2 << "_" << count<< "))))" << endl;
        }
      }

      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << "(assert (=> (= gy_" << count << "_" << count1 << "_" << count2 << " 1) (= y_" << count1 << "_" << count << " y_" << count2 << "_" << count << ")))" << endl;
        }
      }
      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << "(assert (=> (= gy_" << count << "_" << count1 << "_" << count2 << " 1) (not (= x_" << count1 << "_" << count << " x_" << count2 << "_" << count << "))))" << endl;
        }
      }
    }
    //ofp << endl;
    ofp << "(assert (= gx_total_" << count << " (+";
    for (count1 = 1; count1 <= workspace.number_of_uavs; count1++)
    {
      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << " gx_" << count << "_" << count1 << "_" << count2;
        }
      }
    }
    ofp << ")))" << endl;

    ofp << "(assert (= gy_total_" << count << " (+";
    for (count1 = 1; count1 <= workspace.number_of_uavs; count1++)
    {
      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << " gy_" << count << "_" << count1  << "_" << count2;
        }
      }
    }
    ofp << ")))" << endl;

   ofp << "(assert (or (and (= gx_total_" << count << " " << "0) (= gy_total_" << count << " " << workspace.number_of_uavs * (workspace.number_of_uavs - 1) << "))" << endl;
   ofp << "            (and (= gx_total_" << count << " " << workspace.number_of_uavs * (workspace.number_of_uavs - 1) << ") (= gy_total_" << count << " " << "0))" << endl;
   ofp << "            (and (= gx_total_" << count << " " << sqrt(workspace.number_of_uavs) * sqrt(workspace.number_of_uavs) * (sqrt(workspace.number_of_uavs) - 1) << ") (= gy_total_" << count << " " << sqrt(workspace.number_of_uavs) * sqrt(workspace.number_of_uavs) * (sqrt(workspace.number_of_uavs) - 1) << "))))" << endl;
  }
}


void writePrecedenceConstraints(ofstream &ofp, workspace_t workspace)
{
  unsigned int count;

  for (count = 1; count <= workspace.number_of_points; count++)
  {
    ofp << "(assert (<= x_1_" << count << " x_4_" << count << "))" << endl;
    ofp << "(assert (<= x_2_" << count << " x_3_" << count << "))" << endl;
    ofp << "(assert (<= y_1_" << count << " y_2_" << count << "))" << endl;
    ofp << "(assert (<= y_4_" << count << " y_3_" << count << "))" << endl;
  }
}


void writeDistanceConstraints(ofstream &ofp, workspace_t workspace)
{
  unsigned int count, count1, count2;
  for (count = 1; count <= workspace.number_of_points; count++)
  {
    for (count1 = 1; count1 <= workspace.number_of_uavs; count1++)
    {
      for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
      {
        if (count1 != count2)
        {
          ofp << "(assert (or (> (- x_" << count1 << "_" << count << " x_" << count2 << "_" << count << ") 1)" << endl;
          ofp << "            (> (- x_" << count2 << "_" << count << " x_" << count1 << "_" << count << ") 1)" << endl;
          ofp << "            (> (- y_" << count1 << "_" << count << " y_" << count2 << "_" << count << ") 1)" << endl;
          ofp << "            (> (- y_" << count2 << "_" << count << " y_" << count1 << "_" << count << ") 1)))" << endl;
        }
      }
    }
  }
}
