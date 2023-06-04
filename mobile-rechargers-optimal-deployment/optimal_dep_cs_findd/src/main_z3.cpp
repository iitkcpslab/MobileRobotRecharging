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
#include <string>
#include <cstdlib>
#include <sys/time.h>
#include "primitive.h"
#include "readinputs.h"
#include "generatez3file.h"

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


int is_sat()
{
        /** === this function checks if the given specifications satisfy the constraints and returns true/false === **/
        ifstream ifp;
        int flag;
        string str;
        ifp.open("../examples/z3_output");
        string line;

        if(ifp.is_open())
        {
                getline(ifp, line);
                line.compare("sat")==0 ? flag=1 : flag=0;
        }
        ifp.close();
        return flag;
}

pos_vec_t processLine(string line)
{
	pos_vec_t posvec;
	position pos;
	size_t ptx, pty;
        int xx, yy;
	int ptb = -1;
	while(1)
	{
		line = line.substr(ptb+1);
		ptx = line.find("a");
		pty = line.find("_");
		ptb = line.find("$");
		/*if (ptb == string::npos && line.find(")")!=string::npos)
		{
			ptb = line.find(")");
			flag = 1;
		}*/
                if(ptx==string::npos) break;
		string sx = line.substr(ptx+1, pty-ptx-1);
		string sy = line.substr(pty+1, ptb-pty-1);

		xx = atoi(sx.c_str());
		yy = atoi(sy.c_str());
		pos.x = xx; pos.y = yy;
		posvec.push_back(pos);
	}
	return posvec;
}

pos_vec_t getUnsatPoints()
{
	ifstream ifp;
	string line;
	pos_vec_t unsat_core;
	ifp.open("../examples/z3_output");	

	if (ifp.is_open())
	{
		getline(ifp, line);
		getline(ifp, line);
		unsat_core = processLine(line);
	}
/*
        cout << "Unsat points are :" << endl;
        for (unsigned int i=0; i<unsat_core.size(); i++)
        {
          cout << "(" << unsat_core[i].x << " " << unsat_core[i].y << ") ";
        }
        cout << endl;
*/
	return unsat_core;
}

pos_vec_t findCS()
{
        ifstream ifx;
        string line, str, strx, stry, strb, sx, sy;
        pos_vec_t csvec;
        position* csarr;
        size_t loc, locx, locy;
        int cscount=0, xx, yy, locb, ix, iy;
	system("grep -A 1 \"dest\" ../examples/z3_output > z3_output_dest");
        ifx.open("../examples/z3_output_dest");

        if (ifx.is_open())
        {
	   str = "dest";
           while (getline(ifx, line))
	   {
              loc = line.find(str);
              if(loc != string::npos)
	         cscount++;
           }
	   cscount = cscount / 2;
	   ifx.clear();

	   ifx.seekg(0);
	   csarr = (position*)malloc(sizeof(position)*cscount);
	   strx = "destx"; strb = " ";
	   while(getline(ifx, line))
	   {
	      locx = line.find(strx);
	      if(locx != string::npos)
	      {
	         locb = line.find(strb,locx);
		 sx = line.substr(locx+5,locb-(locx+5));
		 ix = atoi(sx.c_str());
				
		 getline(ifx, line);
		 locx = line.find_last_of(" ");
		 locy = line.find(")");
		 xx = atoi((line.substr(locx+1, locy-locx-1)).c_str());

	         csarr[ix-1].x = xx;
	      }
	   }
           ifx.clear();

           ifx.seekg(0);
	   stry = "desty";
           while(getline(ifx, line))
           {
              locy = line.find(stry);
              if(locy != string::npos)
              { 
                 locb = line.find(strb,locy);
                 sy = line.substr(locy+5,locb-(locy+5));
                 iy = atoi(sy.c_str());

                 getline(ifx, line); 
                 locx = line.find_last_of(" ");
                 locy = line.find(")");
                 yy = atoi((line.substr(locx+1, locy-locx-1)).c_str());

                 csarr[iy-1].y = yy;
              }
           }
	   ifx.close();
       }

       for(int i=0; i<cscount; i++)
       {  
           csvec.push_back(csarr[i]);
       }
       return csvec;           
}


string showCS(pos_vec_t csvec)
{
  stringstream ss; 
  for(unsigned int i=0; i<csvec.size(); i++)
  {
     cout << "("<< csvec[i].x << " " << csvec[i].y << ") ";
     ss << "("<< csvec[i].x << " " << csvec[i].y << ")";
  }
  return ss.str();
}


pos_vec_t findBoundaryPoints(workspace_t workspace, pos_vec_t &obstacles)
{
  pos_vec_t boundary;
  for(unsigned int count1 = 0; count1 < workspace.number_of_uavs; count1++)
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
  return boundary;
}


void create_latex_table (testcase_t testres)
{
  string str, ln;
  stringstream ss;
  ss << "       ";
  ss << testres.xmax+1 << " " << testres.obs_name << " " << testres.prims_name << " ";
  ss << "cs=" << testres.fixed_param << " & " << testres.derived_param << " & " << testres.elapsed_time << " \\\\";
  str = ss.str();

  ifstream ifp;
  ofstream ofp;

  ifp.open("../examples/myresults/table_find_d_source.tex");
  ofp.open("../examples/myresults/table_find_d_destin.tex");

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
  
  /* for keeping result backup in another file */
  string filename;
  stringstream ss1;
  ss1 << "../examples/myresults/" << testres.xmax+1 << "_" << testres.obs_name << "_" << testres.prims_name << "_cs" << testres.fixed_param << ".txt";
  filename = ss1.str();

  ofstream ofp1;
  ofp1.open(filename.c_str());
  
  ofp1 << str << " " << testres.trajectory;
  ofp1.close();

  system("cp ../examples/myresults/table_find_d_destin.tex ../examples/myresults/table_find_d_source.tex");
  return; 
}


int main (int argc, char* argv[])
{
  double wcts, wcte;
  struct timeval tm;
  gettimeofday( &tm, NULL );
  wcts = (double)tm.tv_sec + (double)tm.tv_usec * .000001;  

  prim_vec_t primitives, rech_prims;
  pos_vec_t obstacles, unsat_core, csvec;
  workspace_t workspace;
  testcase_t testcase;
  string s;
  int cmdline = atoi(argv[1]);

  readPrimitives(primitives, testcase);
  readRechPrimitives(rech_prims);
  readObstacles(obstacles, testcase);
  readWorkspace(workspace, obstacles, testcase);
  //workspace.boundary = findBoundaryPoints(workspace, obstacles);
  //showCS(workspace.boundary);
  //writeObstacles (obstacles);
  //writePrimitives (primitives);
  workspace.number_of_points = 2; // refers to the distance from any loc to rech's trajectory (find d)
  cout << endl;
  while(1)
  {
      cout << "Checking for points" << workspace.number_of_points;
      cout << "....." << endl;
      generateZ3File(primitives, rech_prims, obstacles, workspace, cmdline);
      system("z3 ../examples/constraints.smt2 > ../examples/z3_output");
      //stringstream ss; ss << workspace.number_of_cs;
      //system(("cp ../examples/z3_output ../examples/z3out"+ ss.str()).c_str());
      if(is_sat()==1)
          break;
      (workspace.number_of_points)++;
  }
  cout << "This is the answer : d = " << workspace.number_of_points  << endl;

  testcase.xmax = workspace.length_x;
  testcase.ymax = workspace.length_y;
  testcase.fixed_param = workspace.number_of_cs;
  testcase.derived_param = workspace.number_of_points; // d
  workspace.csvec = findCS();
  cout << "Fixed (" << workspace.number_of_cs << ") no. of cs are as under:" << endl;
  testcase.trajectory = showCS(workspace.csvec);

  gettimeofday( &tm, NULL );
  wcte = (double)tm.tv_sec + (double)tm.tv_usec * .000001;
  testcase.elapsed_time = printTimeDifference(wcts, wcte);

  create_latex_table (testcase);
  return 0;
}
