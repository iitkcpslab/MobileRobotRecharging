#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>
#include <stdlib.h>
#include "../utils/primitive.h"
#include "../utils/readinputs.h"
#include "../utils/writeconstraints.h"
#include "../safe/writespecificationconstraints.h"
#include "../stlparser/generateloopconstraints.h"
#include "definepropositions.h"

using namespace std;


void writeStateLoopConstraints(ofstream &ofp, workspace_t workspace)
{
  unsigned int count1, count2;

  for (count1 = 2; count1 <= workspace.number_of_points - 1; count1++)
  {
    for (count2 = 1; count2 <= workspace.number_of_uavs; count2++)
    {
      ofp << "(assert (=> l_" << count1 << " (= x_" << count2 << "_" << count1 << " x_" << count2 << "_" << workspace.number_of_points  << ")))" << endl;
      ofp << "(assert (=> l_" << count1 << " (= y_" << count2 << "_" << count1 << " y_" << count2 << "_" << workspace.number_of_points << ")))" << endl;
      ofp << "(assert (=> l_" << count1 << " (= vel_i_" << count2 << "_" << count1 << " vel_f_" << count2 << "_" << workspace.number_of_points - 1 << ")))" << endl;
    }
  }
  ofp << endl;
}


void writeLoopOutputConstraints(ofstream &ofp, workspace_t workspace)
{
  unsigned int count2;

  for (count2 = 0; count2 < workspace.number_of_points - 1; count2++)
  {
      ofp << "(get-value (l_" << count2 + 1 << "))" << endl;
  }
  ofp << endl;
}


void generateZ3File(prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace)
{
  ofstream ofp;
  ifstream ofpr;

  string line;

  ofp.open("constraints.smt2");

  /* Declare the variables */
  declareVariables(ofp, workspace);
  ofp << endl << endl;

  //declareLastVariables(ofp, workspace);
  //ofp << endl << endl;

  ofpr.open("stlvariables.txt");
  if (ofpr.is_open())
  {
    while(std::getline(ofpr, line))
    {
      std::istringstream iss(line);
      ofp << line << endl;
    }
  }
  ofpr.close();
  ofp << endl << endl;

  declareLoopVariables(ofp, workspace.number_of_points);
  
  declarePropositions(ofp, workspace);
    
  /* Write the General Constraints */
  writeInitialLocationConstraints(ofp, workspace);
  ofp << endl;

  writeObstacleConstraints(ofp, obstacles, workspace);
  ofp << endl;

  writeTransitionConstraints(ofp, primitives, obstacles, workspace);
  ofp << endl;

  writeCollisionAvoidanceConstraints2(ofp, primitives, workspace);
  ofp << endl;

  writeDistanceConstraints(ofp, workspace);
  ofp << endl;

  writeCostConstraint(ofp, workspace);
  ofp << endl;

  /* Write the specification constraints */
  definePropositions(ofp, workspace);
  ofp << endl << endl;
  
  ofpr.open("stlconstraints.txt");
  if (ofpr.is_open())
  {
    while(std::getline(ofpr, line))
    {
      std::istringstream iss(line);
      ofp << line << endl;
    }
  }
  ofpr.close();
  ofp << endl << endl;

  writeLoopConstraints(ofp, workspace.number_of_points);
  writeStateLoopConstraints(ofp, workspace);

  ofp << "(check-sat)" << endl;
  //ofp << "(get-model)" << endl;
  writeOutputConstraints(ofp, workspace);
  writeLoopOutputConstraints(ofp, workspace);

  ofp.close();
}


int main (int argc, char *argv[])
{
  prim_vec_t primitives;
  pos_vec_t obstacles;
  workspace_t workspace;
  char command[100];
 
  readPrimitives(primitives);
  //writePrimitives(primitives);

  readObstacles(obstacles);
  //writeObstacles(obstacles);

  readWorkspace(workspace);
  //writeWorkspace(workspace);

  sprintf(command, "./formula_simplifier input");
  system(command);
  
  sprintf(command, "./constraints_generator output %d", workspace.number_of_points - 1);
  system(command);

  generateZ3File(primitives, obstacles, workspace);

  return 0;
}
