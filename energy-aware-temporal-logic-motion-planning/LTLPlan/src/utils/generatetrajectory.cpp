#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sys/time.h>
#include <vector>
#include "primitive.h"
#include "readinputs.h"
#include "extractoutput.h"


const unsigned int max_traj_length = 30;

void generateZ3File(prim_vec_t , pos_vec_t , workspace_t );
//void matlab_code_generator(workspace_t, pos_vec_t, vector<position>);
string extract_value(string ln)
{
  int i=ln.find(" ")+1;
  string ln1=ln.substr(i);
  return ln1.substr(0, ln1.length()-2);
}

void printTrajectory(vector<position> traj)
{
  cout << "Printing Trajectory" << endl;
  for(unsigned int i=0; i<traj.size(); i++)
  {
	cout << traj[i].x << " " << traj[i].y << endl;
  }
}

vector<position> getTrajectory()
{
  ifstream ifp;
  string ln, strx, stry;
  int loc1, loc2, yind=0;
  vector<position> vec;

  strx = "((x_1_";  stry = "((y_1_";
  ifp.open("z3_output");

  while(getline(ifp,ln))
  {
	loc1 = ln.find(strx);
	if(loc1!=string::npos)
	{
	   position pos;
	   pos.x = atoi(extract_value(ln).c_str());
	   vec.push_back(pos);
	   continue;
	}

        loc2 = ln.find(stry);
        if(loc2!=string::npos)
        {
	   vec[yind++].y = atoi(extract_value(ln).c_str());
        }
  }
  printTrajectory(vec);
  return vec;
}

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


int generateTrajectory(prim_vec_t primitives, prim_cost_t prim_cost, pos_vec_t obstacles, workspace_t workspace)
{
  ifstream ifp;
  string line;
  unsigned int count;
  char buffer[100];
  float cost;
  float max_total_cost, min_total_cost;

  struct timeval tm;
  double wcts, wcte;

  ofstream ofp;

  count = 2;
  while (1)
//	for (int x =1;x<=10; x++)
  {
    gettimeofday( &tm, NULL );
    wcts = (double)tm.tv_sec + (double)tm.tv_usec * .000001;

    workspace.number_of_points = count;
    cost = count * workspace.number_of_uavs *  prim_cost.max_cost;
    sprintf(buffer, "%f", cost);
    cout << "Cost =" << cost << endl;
    workspace.total_cost = string(buffer);

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
        //exit(0);
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
  //matlab_code_generator(workspace, obstacles, getTrajectory());
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

  //max_total_cost = extractTrajectoryCostInformation();
  max_total_cost = trajectory_length * workspace.number_of_uavs * prim_cost.max_cost;
  min_total_cost = trajectory_length * workspace.number_of_uavs * prim_cost.min_cost;
  current_cost = (max_total_cost + min_total_cost) / 2;

  cout << "min2_min_cost_diff = " << prim_cost.min2_min_cost_diff << endl << endl;

  cout << "max_total_cost = " << max_total_cost << endl;
  cout << "min_total_cost = " << min_total_cost << endl;
  cout << "current_cost  = " << current_cost << endl;


  system("mv z3_output z3_output_sat");
  while (max_total_cost - min_total_cost > prim_cost.min_cost_diff)
  {
    sprintf(buffer, "%f", current_cost);
    workspace.total_cost = string(buffer);

    generateZ3File(primitives, obstacles, workspace);
    cout << endl << "Timeout is set at 7200s." << endl;
    system("time z3 constraints.smt2 > z3_output");

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
      //max_total_cost = extractTrajectoryCostInformation();
      max_total_cost = current_cost;
      system("mv z3_output z3_output_sat");
    }
    else
    {
      cout << "unknown output from z3.." << endl;
      min_total_cost = current_cost;
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


void matlab_code_generator(workspace_t workspace, pos_vec_t obstacles, vector<position> traj)
{
        vector<position> obs_vec;
        ofstream ofp;
        ofp.open("/home/tanmoy/modelcheckermotionplanner/Experiments/LTLPlan/examples/output_ltlplan.m");

        ofp << "clear all;" << endl;
        ofp << "close all;" << endl;
        ofp << "dim_x = 17; dim_y = 17;" << endl;
        ofp << "axis([-1 dim_x -1 dim_y]);" << endl;
        //ofp << "rectangle('Position', [0, 0, dim_x, dim_y]);" << endl;
        ofp << "rectangle('Position', [0, 0, 17, 17], 'linewidth',2);" << endl;
        ofp << "for i=0:16" << endl;
        ofp << "        rectangle('Position', [0, i, 17, 1]);" << endl;
        ofp << "end" << endl << endl;
        ofp << "for i=0:16" << endl;
        ofp << "        rectangle('Position', [i, 0, 1, 17]);" << endl;
        ofp << "end" << endl << endl;

        for(int i=0; i < obstacles.size(); i++)
        {
                ofp << "rectangle(\'Position\',["<< obstacles[i].x << ", " << obstacles[i].y << ", 1, 1], \'facecolor\', \'black\');"<< endl;
        }
        ofp << endl << endl << "hold on;" << endl;
        //ofp << "axis off;" << endl;
        //ofp << "axis off;" << endl;


        int xx; int yy;
	xx = 8; yy = 6;
        ofp << "tri=[" << xx+0.1 << " " << xx+0.5 << " " << xx+0.9 << " " << xx+0.1 << ";" << yy+0.1 << " " << yy+0.9 << " " << yy+0.1 << " " << yy+0.1 << "];" << endl;
        ofp << "X=tri(1,:); Y=tri(2,:);" << endl;
        ofp << "plot(X, Y,'linewidth',1,..." << endl;
        ofp << "'MarkerEdgeColor', 'k');" << endl;
        ofp << "fill(X,Y,'b');" << endl;

	xx = 2; yy = 10;
        ofp << "tri=[" << xx+0.1 << " " << xx+0.5 << " " << xx+0.9 << " " << xx+0.1 << ";" << yy+0.1 << " " << yy+0.9 << " " << yy+0.1 << " " << yy+0.1 << "];" << endl;
        ofp << "X=tri(1,:); Y=tri(2,:);" << endl;
        ofp << "plot(X, Y,'linewidth',1,..." << endl;
        ofp << "'MarkerEdgeColor', 'k');" << endl;
        ofp << "fill(X,Y,'b');" << endl;

	xx = 13; yy = 12;
        ofp << "tri=[" << xx+0.1 << " " << xx+0.5 << " " << xx+0.9 << " " << xx+0.1 << ";" << yy+0.1 << " " << yy+0.9 << " " << yy+0.1 << " " << yy+0.1 << "];" << endl;
        ofp << "X=tri(1,:); Y=tri(2,:);" << endl;
        ofp << "plot(X, Y,'linewidth',1,..." << endl;
        ofp << "'MarkerEdgeColor', 'k');" << endl;
        ofp << "fill(X,Y,'b');" << endl;
        
	xx = 1; yy = 6;
        ofp << "tri=[" << xx+0.1 << " " << xx+0.5 << " " << xx+0.9 << " " << xx+0.1 << ";" << yy+0.1 << " " << yy+0.9 << " " << yy+0.1 << " " << yy+0.1 << "];" << endl;
        ofp << "X=tri(1,:); Y=tri(2,:);" << endl;
        ofp << "plot(X, Y,'linewidth',1,..." << endl;
        ofp << "'MarkerEdgeColor', 'k');" << endl;
        ofp << "fill(X,Y,'r');" << endl;

	xx = 10; yy = 15;
        ofp << "tri=[" << xx+0.1 << " " << xx+0.5 << " " << xx+0.9 << " " << xx+0.1 << ";" << yy+0.1 << " " << yy+0.9 << " " << yy+0.1 << " " << yy+0.1 << "];" << endl;
        ofp << "X=tri(1,:); Y=tri(2,:);" << endl;
        ofp << "plot(X, Y,'linewidth',1,..." << endl;
        ofp << "'MarkerEdgeColor', 'k');" << endl;
        ofp << "fill(X,Y,'r');" << endl;

	xx = 11; yy = 0;
        ofp << "tri=[" << xx+0.1 << " " << xx+0.5 << " " << xx+0.9 << " " << xx+0.1 << ";" << yy+0.1 << " " << yy+0.9 << " " << yy+0.1 << " " << yy+0.1 << "];" << endl;
        ofp << "X=tri(1,:); Y=tri(2,:);" << endl;
        ofp << "plot(X, Y,'linewidth',1,..." << endl;
        ofp << "'MarkerEdgeColor', 'k');" << endl;
        ofp << "fill(X,Y,'r');" << endl;

        xx = 10; yy = 12;
        ofp << "plot(" << xx+0.5 << "," << yy+0.5 << ", \'o\', \'LineWidth\', 1,..." << endl;
        ofp << "\'MarkerEdgeColor\', \'k\',..." << endl;
        ofp << "\'MarkerFaceColor\', \'g\',..." << endl;
        ofp << "'MarkerSize', 12)" << endl;

        xx = 4; yy = 8;
        ofp << "plot(" << xx+0.5 << "," << yy+0.5 << ", \'o\', \'LineWidth\', 1,..." << endl;
        ofp << "\'MarkerEdgeColor\', \'k\',..." << endl;
        ofp << "\'MarkerFaceColor\', \'g\',..." << endl;
        ofp << "'MarkerSize', 12)" << endl;

        xx = 12; yy = 5;
        ofp << "plot(" << xx+0.5 << "," << yy+0.5 << ", \'o\', \'LineWidth\', 1,..." << endl;
        ofp << "\'MarkerEdgeColor\', \'k\',..." << endl;
        ofp << "\'MarkerFaceColor\', \'g\',..." << endl;
        ofp << "'MarkerSize', 12)" << endl;


	

	for(int i=0; i < traj.size(); i++)
        {
                int xx = traj[i].x; int yy = traj[i].y;
                //ofp << "rectangle(\'Position\',["<< chargers_vec_turtle[i].x+0.1 << ", " << chargers_vec_turtle[i].y+0.1 << ", 0.8, 0.8], \'facecolor\', \'red\');"<< endl;
                //ofp << "plot(" << xx+0.5 << "," << yy+0.5 << ", \'o\', \'LineWidth\', 0.7,..." << endl;
		//ofp << "plot(" << xx+0.5 << "," << yy+0.5 << ", \'o\', \'LineWidth\', 0.7,..." << endl;
                //ofp << "\'MarkerEdgeColor\', \'k\',..." << endl;
                //ofp << "\'MarkerFaceColor\', \'g\',..." << endl;
                //ofp << "'MarkerSize', 12)" << endl;
        	ofp << "text(" << xx+0.3 << "," << yy+0.5<<",'\\color{blue}"<< i+1 <<"');" << endl;

        }
}
