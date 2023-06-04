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

pos_vec_t findBoundaryPoints(workspace_t workspace, pos_vec_t &obstacles)
{
  pos_vec_t boundary; 
  for(int count1 = 0; count1 < workspace.number_of_uavs; count1++)
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
  for(int i=0; i<csvec.size(); i++)
  {
     cout << "cs"<<i << ": "<< csvec[i].x << " " << csvec[i].y<< endl;
  }
}

int main (int argc, char* argv[])
{
  prim_vec_t primitives;
  pos_vec_t obstacles, unsat_core;
  workspace_t workspace;
  string s;
  
  int ncs = atoi(argv[1]);
  readPrimitives(primitives); 
  readObstacles(obstacles);
  readWorkspace(workspace, obstacles);
  workspace.boundary = findBoundaryPoints(workspace, obstacles);

  
  workspace.number_of_cs = ncs;
  workspace.number_of_points = 1;
  do
  {
	(workspace.number_of_points)++;
	cout << endl << "Checking for ncs = " << workspace.number_of_cs <<", d = " << workspace.number_of_points << endl;
	cout << "....." << endl;
	generateZ3File(primitives, obstacles, workspace);
	system("z3 ../examples/constraints.smt2 > ../examples/z3_output");
  }while (is_sat()==0);

  if(is_sat())
  {
  	cout << endl << "Answer is d = " << workspace.number_of_points << endl;
	showCS(findCS());
  }

  return 0;
}
