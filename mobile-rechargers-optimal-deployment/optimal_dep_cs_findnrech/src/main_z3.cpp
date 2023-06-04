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
#include <math.h>
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

pos_vec_t findCS(int rech_i)
{
        ifstream ifx;
        string line, str, strx, stry, strb, sx, sy;
	stringstream ss;
        pos_vec_t csvec;
        position* csarr;
        size_t loc, locx, locy;
        int cscount=0, xx, yy, locb, ix, iy;

	ss << "grep -A 1 \"dx" << rech_i << "\" ../examples/z3_output > z3_output_dest";
        system(ss.str().c_str());
	ss.str("");
	ss << "grep -A 1 \"dy" << rech_i << "\" ../examples/z3_output >> z3_output_dest";
        system(ss.str().c_str());
	
        ifx.open("../examples/z3_output_dest");

	int digcount = floor(log10(rech_i)) + 1; // number of digits of the int
        if (ifx.is_open())
        {
           str = " d";
           while (getline(ifx, line))
           {
              loc = line.find(str);
              if(loc != string::npos)
                 cscount++;
           }
           cscount = cscount/2;
           ifx.clear();

           ifx.seekg(0);
           csarr = (position*)malloc(sizeof(position)*cscount);
           strx = "dx"; strb = " ";
           while(getline(ifx, line))
           {
              locx = line.find(strx);
              if(locx != string::npos)
              {
                 locb = line.find(strb,locx);
                 sx = line.substr(locx+3+digcount,locb-(locx+3+digcount));
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
           stry = "dy";
           while(getline(ifx, line))
           {
              locy = line.find(stry);
              if(locy != string::npos)
              {
                 locb = line.find(strb,locy);
                 sy = line.substr(locy+3+digcount,locb-(locy+3+digcount));
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


string showCS(vector<pos_vec_t> csvec)
{
  stringstream ss; 
  for(unsigned int i=0; i<csvec.size(); i++)
  {
    cout << "rech " << i+1 << endl;
    for(unsigned int j=0; j<csvec[i].size(); j++)
    {
      cout << "("<< csvec[i][j].x << " " << csvec[i][j].y << ") ";
      ss << "("<< csvec[i][j].x << " " << csvec[i][j].y << ")";
    }
    cout << endl; ss << endl;
  }
  return ss.str();
}

void create_latex_table (testcase_t testres)
{
  string str, ln;
  stringstream ss;
  ss << "       ";
  ss << testres.xmax+1 << " " << testres.obs_name << " " << testres.prims_name << " ";
  ss << "cs=" << testres.fixed_param1 << " d=" << testres.fixed_param2 << " & " << testres.derived_param << " & " << testres.elapsed_time << " \\\\";
  str = ss.str();

  ifstream ifp;
  ofstream ofp;

  ifp.open("../examples/myresults/table_find_nrechs_source.tex");
  ofp.open("../examples/myresults/table_find_nrechs_destin.tex");

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
  ss1 << "../examples/myresults/" << testres.xmax+1 << "_" << testres.obs_name << "_" << testres.prims_name << "_cs" << testres.fixed_param1 << "_d" << testres.fixed_param2 << ".txt";
  filename = ss1.str();

  ofstream ofp1;
  ofp1.open(filename.c_str());
  
  ofp1 << str << " " << testres.trajectory;
  ofp1.close();

  system("cp ../examples/myresults/table_find_nrechs_destin.tex ../examples/myresults/table_find_nrechs_source.tex");
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

  workspace.number_of_rechs = 1; // refers to the distance from any loc to rech's trajectory (find d)

  cout << endl;
  while(1)
  {
      cout << "Checking for rech " << workspace.number_of_rechs;
      cout << "....." << endl;
      generateZ3File(primitives, rech_prims, obstacles, workspace, cmdline);
      system("z3 ../examples/constraints.smt2 > ../examples/z3_output");
      //stringstream ss; ss << workspace.number_of_cs;
      //system(("cp ../examples/z3_output ../examples/z3out"+ ss.str()).c_str());
      if(is_sat()==1)
          break;
      (workspace.number_of_rechs)++;
  }
  cout << "This is the answer : nrechs = " << workspace.number_of_rechs  << endl;

  testcase.xmax = workspace.length_x;
  testcase.ymax = workspace.length_y;
  testcase.fixed_param1 = workspace.number_of_cs;
  testcase.fixed_param2 = workspace.number_of_points; // d
  testcase.derived_param = workspace.number_of_rechs;

  cout << "Fixed (" << workspace.number_of_cs << ", " << workspace.number_of_points << ") no. of cs and d are as under:" << endl;
  for (unsigned int i=0; i<workspace.number_of_rechs; i++)
  {
    workspace.csvec.push_back(findCS(i+1));
  }
  testcase.trajectory = showCS(workspace.csvec);

  gettimeofday( &tm, NULL );
  wcte = (double)tm.tv_sec + (double)tm.tv_usec * .000001;
  testcase.elapsed_time = printTimeDifference(wcts, wcte);

  create_latex_table (testcase);
  return 0;
}
