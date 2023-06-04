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
#include "primitive.h"
#include "readinputs.h"
#include "generatez3file.h"

using namespace std;

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
	int ptx, pty, ptb=-1, ptc;
	int xx, yy, cc;
	while(1)
	{
		line = line.substr(ptb+1);
		ptx = line.find("a");
		pty = line.find("_");
		ptb = line.find("$");
		ptc = line.find("@");
		/*if (ptb == string::npos && line.find(")")!=string::npos)
		{
			ptb = line.find(")");
			flag = 1;
		}*/
                if(ptx==string::npos) break;
		string sx = line.substr(ptx+1, pty-ptx-1);
		string sy = line.substr(pty+1, ptb-pty-1);
		string sc = line.substr(ptb+1, ptc-ptb-1);

		xx = atoi(sx.c_str());
		yy = atoi(sy.c_str());
		cc = atoi(sc.c_str());
		pos.x = xx; pos.y = yy; pos.c = cc;
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
	return unsat_core;
}

pos_vec_t findCS()
{
        ifstream ifx;
        string line, str, strx, stry, strb, sx, sy;
        pos_vec_t csvec;
        position* csarr;
        int cscount=0, loc, locx, locy, xx, yy, locb, ix, iy;
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
              //cout << "cs" << i << ": " << csarr[i].x << " " << csarr[i].y << endl;
              csvec.push_back(csarr[i]);
           }
	return csvec;           
}

void showCS(pos_vec_t csvec)
{
  for(unsigned int i=0; i<csvec.size(); i++)
  {
     cout << "cs"<< i+1 << ": "<< csvec[i].x << " " << csvec[i].y<< endl;
  }
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

int main (int argc, char* argv[])
{
  prim_vec_t primitives;
  pos_vec_t obstacles, unsat_core, csvec;
  workspace_t workspace;
  string s;
  int flag1 = 0;
  int cmdline = atoi(argv[1]);
  int delta = atoi(argv[2]);
  cout << endl << "Checking with const ncs = " << cmdline << ", delta = " << delta << endl;   

  readPrimitives(primitives); 
  readObstacles(obstacles);
  readWorkspace(workspace, obstacles);
  workspace.boundary = findBoundaryPoints(workspace, obstacles);
  //showCS(workspace.boundary);
  workspace.number_of_cs = cmdline;
  workspace.number_of_points = 2;
  cout << endl;
  while(1)
  {
      cout << "Checking for d = " << workspace.number_of_points << endl;
      generateZ3File(primitives, obstacles, workspace, delta);
      system("z3 ../examples/constraints.smt2 > ../examples/z3_output");
      //stringstream ss; ss << workspace.number_of_points;
      //system(("cp ../examples/z3_output ../examples/z3out"+ ss.str()).c_str());
      if(is_sat()==1)
          break;

      else
               unsat_core = getUnsatPoints();
               workspace.number_of_uavs = unsat_core.size();
               workspace.pos_start = new position[workspace.number_of_uavs];
               for(unsigned int i=0; i<workspace.number_of_uavs; i++)
               {
                  workspace.pos_start[i] = unsat_core[i];
                  cout << "unsat pt"<<i<<" : "<<workspace.pos_start[i].x << " " << workspace.pos_start[i].y << " @ " << workspace.pos_start[i].c << endl;
               }
           flag1 = 0;
           
           (workspace.number_of_points)++;
           while(flag1==0)
           {
               generateZ3File(primitives, obstacles, workspace, delta);
               system("z3 ../examples/constraints.smt2 > ../examples/z3_output");
	       if(is_sat()==1)
               {
                   readWorkspace(workspace, obstacles);
                   pos_vec_t cstemp = findCS();
         	   //workspace.csvec.insert(workspace.csvec.end(), cstemp.begin(), cstemp.end());
        	   workspace.csvec = cstemp;
                   //workspace.number_of_cs = workspace.csvec.size();
         	   //showCS(workspace.csvec);                   
                   flag1 = 1;
               }
               else
               {
               /*unsat_core = getUnsatPoints();
               workspace.number_of_uavs = unsat_core.size();
               workspace.pos_start = new position[workspace.number_of_uavs];
               for(unsigned int i=0; i<workspace.number_of_uavs; i++)
               {
                  workspace.pos_start[i] = unsat_core[i];
                  cout << "unsat pt"<<i<<" : "<<workspace.pos_start[i].x << " " << workspace.pos_start[i].y << " @ " << workspace.pos_start[i].c << endl;
               }*/

                   workspace.csvec.clear();
                   (workspace.number_of_points)++;
               }
           }
  }
    cout << "Final checking for CS = " << cmdline << endl;
    cout << "This is the answer : d = " << workspace.number_of_points  << endl;
    workspace.csvec = findCS();
    showCS(workspace.csvec);
    return 0;
}
