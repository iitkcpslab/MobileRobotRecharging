#include <iostream>
#include <fstream>
#include <sstream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#include "../utils/primitive.h"
#include "../utils/readinputs.h"
#include "../utils/writeconstraints.h"
#include "../utils/extractoutput.h"
#include "../utils/generatetrajectory.h"
#include "../ltlparser/generateloopconstraints.h"
#include "definepropositions.h"

using namespace std;

const unsigned int max_traj_length = 50;

/*
void printTimeDifference(double wcts, double wcte) 
{
  double duration;
  int hr, min;
  double sec;

  duration = wcte - wcts;
  hr = duration / 3600;
  min = (duration / 60) - (hr * 60) ;
  sec = duration - hr * 3600 - min * 60;
  cout << endl << duration << "s" << endl;
  cout << endl << hr << "h " << min << "m " << (((sec - int(sec)) > 0.5) ? (int(sec) + 1) : int(sec)) << "s" << endl << endl;

  ofstream ofp;
  ofp.open("result", fstream::app); 
  ofp << hr << "h " << min << "m " << (((sec - int(sec)) > 0.5) ? (int(sec) + 1) : int(sec)) << "s" << endl << endl;
  ofp.close();
}
*/

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
  char command[100];
  string line;

  sprintf(command, "time ./constraints_generator output %d", workspace.number_of_points - 1);
  system(command);

  ofp.open("constraints.smt2");

  /* Declare the variables */
  declareVariables(ofp, workspace);
  ofp << endl << endl;

  //declareLastVariables(ofp, workspace);
  //ofp << endl << endl;

  ofpr.open("ltlvariables.txt");
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

  writeInitialChargeConstraint(ofp, workspace);  // new
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


  writeChargeTransitionConstraint(ofp, workspace);  // new
  ofp << endl;

  definePropositions(ofp, workspace); // new
  ofp << endl;

  writeRechargeConstraint(ofp, workspace);  // new 
  ofp << endl;


  /* Write the specification constraints */
  //definePropositions(ofp, workspace);
  ofp << endl << endl;
  
  ofpr.open("ltlconstraints.txt");
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

/*
int generateTrajectory(prim_vec_t primitives, prim_cost_t prim_cost, pos_vec_t obstacles, workspace_t workspace)
{
  ifstream ifp;
  string line;
  unsigned int count;
  char buffer[100];
  float cost;
  char command[100];
  float max_total_cost, min_total_cost;

  struct timeval tm;
  double wcts, wcte;

  ofstream ofp;
  
  count = 2;
  while (1)
  {
    gettimeofday( &tm, NULL );
    wcts = (double)tm.tv_sec + (double)tm.tv_usec * .000001;

    workspace.number_of_points = count;
    cost = count * workspace.number_of_uavs *  prim_cost.max_cost;
    sprintf(buffer, "%f", cost);
    cout << "Cost =" << cost << endl;
    workspace.total_cost = string(buffer);    

    sprintf(command, "time ./constraints_generator output %d", workspace.number_of_points - 1);
    system(command);

    generateZ3File(primitives, obstacles, workspace);
    //cout << endl << "Timeout is set at 3600s." << endl;
    //system("timeout 7200s z3 constraints.smt2 > z3_output");
    system("time z3 constraints.smt2 > z3_output");

    ifp.open("z3_output");
    if (ifp.is_open())
    {
      getline(ifp, line);
      ifp.close();
    }
    
    cout << "$$$$$$$$ " << count << " " << line << endl;
     
    if (line == "unsat")
    {
      count = count + 1;
      if (count > max_traj_length)
      {
        cout << "Trajectory does not exist.." << endl;
        exit(0);
      }
    }
    else if (line == "sat")
    {
      system("cp z3_output z3_output_sat");
      gettimeofday( &tm, NULL );
      wcte = (double)tm.tv_sec + (double)tm.tv_usec * .000001;

      ofp.open("result");
      ofp << "Trajectory Length = " << count << endl << endl;
      ofp.close();
      
      ofp.open("result", fstream::app);
      ofp << "Final Iteration Time = ";
      ofp.close();
      printTimeDifference(wcts, wcte);
      
      break;
    }
    else
    {
      cout << "unknown output from z3.." << endl;
      count = count + 1;
      if (count > max_traj_length)
      {
        exit(0);
      }
    }
    if (count > max_traj_length) 
      break;
  }
  system("perl processoutputfile.pl");
  system("mv planner_output plan_noopt");

  max_total_cost = count * workspace.number_of_uavs * prim_cost.max_cost;
  min_total_cost = count * workspace.number_of_uavs * prim_cost.min_cost;
  cout << "max_total_cost = " << max_total_cost << endl;
  cout << "min_total_cost = " << min_total_cost << endl;

  ofp.open("result", fstream::app);
  ofp << "max_total_cost = " << max_total_cost << endl;
  ofp << "min_total_cost = " << min_total_cost << endl;
  ofp << "Cost Before Optimization = " << extractTrajectoryCostInformation() << endl << endl;
  ofp.close(); 
  cout << "Cost  = " << extractTrajectoryCostInformation() << endl << endl;

  return count;
}



void optimizeTrajectory(prim_vec_t primitives, prim_cost_t prim_cost, pos_vec_t obstacles, workspace_t workspace, int trajectory_length)
{
  float max_total_cost, min_total_cost, current_cost;
  ifstream ifp;
  string line;
  char buffer[100];

  ofstream ofp;
 
  workspace.number_of_points = trajectory_length;
 
  max_total_cost = extractTrajectoryCostInformation();
  min_total_cost = trajectory_length * workspace.number_of_uavs * prim_cost.min_cost;
  current_cost = (max_total_cost + min_total_cost) / 2;

  cout << "min2_min_cost_diff = " << prim_cost.min2_min_cost_diff << endl << endl; 

  cout << "max_total_cost = " << max_total_cost << endl;
  cout << "min_total_cost = " << min_total_cost << endl;
  cout << "current_cost  = " << current_cost << endl;


  system("mv z3_output z3_output_sat");
  while (max_total_cost - min_total_cost > prim_cost.min2_min_cost_diff)
  {
    sprintf(buffer, "%f", current_cost);
    workspace.total_cost = string(buffer);

    generateZ3File(primitives, obstacles, workspace);
    cout << endl << "Timeout is set at 7200s." << endl;
    system("timeout 7200 time z3 constraints.smt2 > z3_output");

    ifp.open("z3_output");
    getline(ifp, line);
    ifp.close();
    cout << "$$$$$$$$ " << trajectory_length << " " << line << endl;

    if (line == "unsat")
    {
      min_total_cost = current_cost;
    }
    else if (line == "sat")
    {
      max_total_cost = extractTrajectoryCostInformation();
      system("mv z3_output z3_output_sat");
    }
    else
    {
      cout << "unknown output from z3.." << endl;
      min_total_cost = current_cost;
      //break;
    }
    current_cost = (max_total_cost + min_total_cost) / 2;
    cout << "max_total_cost = " << max_total_cost << endl;
    cout << "min_total_cost = " << min_total_cost << endl;
    cout << "current_cost  = " << current_cost << endl;
  }
  
  system("mv z3_output_sat z3_output");
  system("perl processoutputfile.pl");
  system("mv planner_output plan_opt");

  ofp.open("result", fstream::app);
  ofp << "Cost After Optimization = " << extractTrajectoryCostInformation() << endl << endl;
  ofp.close();
  cout << "Cost  = " << extractTrajectoryCostInformation() << endl << endl;
}
*/

int main ()
{
  prim_vec_t primitives;
  pos_vec_t obstacles;
  workspace_t workspace;
  prim_cost_t prim_cost;
  char command[100];
  int trajectory_length;

  readPrimitives(primitives);
  //writePrimitives(primitives);

  getPrimitiveCost(primitives, prim_cost);
  //writePrimitiveCost(prim_cost);

  readObstacles(obstacles);
  //writeObstacles(obstacles);

  readWorkspace(workspace);
  //writeWorkspace(workspace);

  sprintf(command, "time ./formula_simplifier input");
  system(command);

  struct timeval tm;
  double wcts, wcte;
  ofstream ofp;

  gettimeofday( &tm, NULL );
  wcts = (double)tm.tv_sec + (double)tm.tv_usec * .000001;
  trajectory_length = generateTrajectory(primitives, prim_cost, obstacles, workspace);
  gettimeofday( &tm, NULL );
  wcte = (double)tm.tv_sec + (double)tm.tv_usec * .000001;
  ofp.open("result", fstream::app);
  ofp << "Total Time Before Optimization = ";
  ofp.close();
  printTimeDifference(wcts, wcte);

  gettimeofday( &tm, NULL );
  wcts = (double)tm.tv_sec + (double)tm.tv_usec * .000001;
  //optimizeTrajectory(primitives, prim_cost, obstacles, workspace, trajectory_length);
  gettimeofday( &tm, NULL );
  wcte = (double)tm.tv_sec + (double)tm.tv_usec * .000001;
  ofp.open("result", fstream::app);
  ofp << "Total Time For Optimization = ";
  ofp.close();
  printTimeDifference(wcts, wcte);
  
  matlab_code_generator(workspace, obstacles, getTrajectory()); 

}
