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
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include "primitive.h"
#include "readinputs.h"
using namespace std;

void readPrimitives(prim_vec_t &primitives)
{
  ifstream ifp;

  string line;
  string str;
  int location, location1, location2, location3;
  position pos_tmp;
  int xmin, ymin, xmax, ymax;
  
  state q_i, q_f;
  position pos_f;
  string cost;
  pos_vec_t swath;
  position pos_min;
  position pos_max;

  ifp.open("../examples/2d_template.txt");

  if (ifp.is_open())
  {
    while (getline(ifp, line))
    {
      //cout << line << endl;
      location = line.find(":");

      if (line.substr(0, location) == "q_i")
      {
        istringstream (line.substr(location+2, 1)) >> q_i.velocity;
      }

      if (line.substr(0, location) == "q_f")
      {
	istringstream (line.substr(location+2, 1)) >> q_f.velocity;
      }

      if (line.substr(0, location) == "pos_f")
      {
        location1 = line.find('[');
        location2 = line.find(',');
        location3 = line.find(']');
        istringstream (line.substr(location1 + 1, location2 - location1 - 1)) >> pos_f.x;
        istringstream (line.substr(location2 + 2, location3 - location2 - 2)) >> pos_f.y;
      }

      if (line.substr(0, location) == "cost")
      {
        cost = line.substr(location + 1);
        //cost.erase(cost.size() - 1);
      }

      if (line.substr(0, location) == "swath")
      {
        str = line.substr(location+1);
        xmin = 10000; ymin = 10000; xmax = -10000; ymax = -10000;
        location = str.find(';');
        while (location != -1)
        {
          location1 = str.find('[');
          location2 = str.find(',');
          location3 = str.find(']');
          istringstream (str.substr(location1 + 1, location2 - location1 - 1)) >> pos_tmp.x;
          istringstream (str.substr(location2 + 2, location3 - location2 - 2)) >> pos_tmp.y;
          swath.push_back(pos_tmp);
          if (pos_tmp.x < xmin) 
            xmin = pos_tmp.x;
          if (pos_tmp.y < ymin) 
            ymin = pos_tmp.y;
          if (pos_tmp.x > xmax) 
            xmax = pos_tmp.x;
          if (pos_tmp.y > ymax) 
            ymax = pos_tmp.y;
          str = str.substr(location+1);
          location = str.find(';');
          //cout << pos_tmp.x << "  ---  " << pos_tmp.y << endl;
        }
        location1 = str.find('[');
        location2 = str.find(',');
        location3 = str.find(']');
        istringstream (str.substr(location1 + 1, location2 - location1 - 1)) >> pos_tmp.x;
        istringstream (str.substr(location2 + 2, location3 - location2 - 2)) >> pos_tmp.y;
        //cout << pos_tmp.x << "  ---  " << pos_tmp.y << endl;
        swath.push_back(pos_tmp);
        if (pos_tmp.x < xmin) 
          xmin = pos_tmp.x;
        if (pos_tmp.y < ymin) 
          ymin = pos_tmp.y;
        if (pos_tmp.x > xmax) 
          xmax = pos_tmp.x;
        if (pos_tmp.y > ymax) 
          ymax = pos_tmp.y;
        pos_min.x = xmin;
        pos_min.y = ymin;
        pos_max.x = xmax;
        pos_max.y = ymax;        
        Primitive prim(q_i, q_f, pos_f, cost, swath, pos_min, pos_max);
        primitives.push_back(prim); 
        swath.erase (swath.begin(), swath.end());
      }
    }
    ifp.close();
  }
}


void writePrimitives(prim_vec_t primitives)
{
  unsigned int count1, count2;
  state q_i, q_f;
  position pos_f;
  string cost;
  pos_vec_t swath;
  position pos_min;
  position pos_max;

  cout << endl << "PRIMITIVES:" << endl << endl;
  for(count1 = 0; count1 < primitives.size(); count1++)
  {
    cout << "Primitive " << count1 << endl;

    q_i = primitives[count1].get_q_i();
    cout << "q_i: " << q_i.velocity << endl;

    q_f = primitives[count1].get_q_f();
    cout << "q_f: " << q_f.velocity << endl;

    pos_f = primitives[count1].get_pos_f();
    cout << "pos_f: " << pos_f.x << " " << pos_f.y << endl;

    cost = primitives[count1].get_cost();
    cout << "cost: " << cost << endl;

    swath = primitives[count1].get_swath();
    cout << "swath: ";
    for(count2 = 0; count2 < swath.size(); count2++)
    {
      cout << swath[count2].x << " " << swath[count2].y << " | ";
    }
    cout << endl;
    
    pos_min = primitives[count1].get_pos_min();
    cout << "pos_min: " << pos_min.x << " " << pos_min.y << endl;

    pos_max = primitives[count1].get_pos_max();
    cout << "pos_max: " << pos_max.x << " " << pos_max.y << endl;

    cout << endl;
  }
}


void readObstacles(pos_vec_t &obstacles)
{
  ifstream ifp;
  string line;
  int location; 
  position pos_tmp;

  ifp.open("../examples/obstacle.txt");  
  if (ifp.is_open())
  {
    while (getline(ifp, line))
    {
      location = line.find(' ');
      istringstream (line.substr(0, location)) >> pos_tmp.x;
      istringstream (line.substr(location + 1)) >> pos_tmp.y;
      obstacles.push_back(pos_tmp);
    }
  }
  ifp.close();
}


void writeObstacles (pos_vec_t obstacles)
{
  position pos_tmp;
  unsigned int count;
  cout << endl << "OBSTACLES:" << endl << endl;
  for(count = 0; count < obstacles.size(); count++)
  {
    pos_tmp = obstacles[count];
    cout << pos_tmp.x << " " << pos_tmp.y << endl;
  }
  cout << endl;
}


void writeObstaclesToFile (pos_vec_t obstacles)
{
  ofstream ofp;
  position pos_tmp;
  unsigned int count;
  
  ofp.open("../examples/obstacle.txt");  
  for(count = 0; count < obstacles.size(); count++)
  {
    pos_tmp = obstacles[count];
    ofp << pos_tmp.x << " " << pos_tmp.y << endl;
  }
  ofp.close();
}

int find_pos(pos_vec_t &pos_vec, position pos)
{
  pos_vec_t::iterator beg = pos_vec.begin();
  for(;beg!=pos_vec.end();beg++)
  {
    if((*beg).x==pos.x && (*beg).y==pos.y)
    {
      //cout << endl << "obstacle is "<< pos.x << " " << pos.y << endl;
      return 1;
    }
  }
  return 0;
}

void readWorkspace(workspace_t &workspace, pos_vec_t &ob)
{
  ifstream ifp;
  string line;
  pos_vec_t free_pos;
  position pos_tmp;
  int flag=0, count=0;
  ifp.open("../examples/workspace.txt.bak");

  if (ifp.is_open())
  {
    getline(ifp, line);
    istringstream (line) >> workspace.length_x;

    getline(ifp, line);
    istringstream (line) >> workspace.length_y;

    getline(ifp, line);
    /*istringstream (line) >> workspace.number_of_points;*/

    getline(ifp, line);
    //istringstream (line) >> workspace.number_of_cs;

    getline(ifp, line);
    workspace.total_cost = line;
    for(unsigned int i=0; i<=workspace.length_x; i++)
    {
      for(unsigned int j=0; j<=workspace.length_y; j++)
      {
	pos_tmp.x = i; pos_tmp.y = j;
	flag = find_pos(ob, pos_tmp);
	if(!flag)
	{
	  //non_obs <<  i << " " << j << endl;
	  //workspace.pos_start[count] = pos_tmp;
	  free_pos.push_back(pos_tmp);
	  count++;
	}
      }
   }

   workspace.pos_start = new position[count];
   for(int i=0; i<count; i++)
   {
	workspace.pos_start[i] = free_pos[i];
   }
   workspace.number_of_uavs = count;
  }
  ifp.close();
}

void writeWorkspace(workspace_t workspace)
{
  unsigned int count;

  cout << endl << "WORKSPACE:" << endl << endl;
  cout << workspace.length_x << endl;
  cout << workspace.length_y << endl;
  cout << workspace.number_of_uavs << endl;  
  for (count = 0; count < workspace.number_of_uavs; count++)
  {
    cout << workspace.pos_start[count].x << " " << workspace.pos_start[count].y << endl;
   // cout << workspace.pos_end[count].x << " " << workspace.pos_end[count].y << endl;
  }
  cout << workspace.number_of_points << endl;
  cout << workspace.total_cost << endl;
  cout << endl;
}


void readDimension(dimension_t &dimension)
{
  ifstream ifp;
  string line;

  ifp.open("../examples/dimension.txt");
  if (ifp.is_open())
  {
    getline(ifp, line);
    istringstream (line) >> dimension.length_x;
    
    getline(ifp, line);
    istringstream (line) >> dimension.length_y;

    getline(ifp, line);
    istringstream (line) >> dimension.number_of_uavs;
    
    getline(ifp, line);
    istringstream (line) >> dimension.perc_obs;
    ifp.close();
  }
  else
  {
    cout << "dimension.txt file cannot be opened.." << endl;
    exit(0);
  }
}


void writeDimension(dimension_t dimension)
{
  cout << endl << "DIMENSION:" << endl << endl;
  cout << dimension.length_x << endl;
  cout << dimension.length_y << endl;
  cout << dimension.number_of_uavs << endl;
  cout << dimension.perc_obs << endl;
  cout << endl;
}


void writeDimensionToFile(dimension_t dimension)
{
  ofstream ofp;

  ofp.open("../examples/dimension.txt");
  ofp << dimension.length_x << endl;
  ofp << dimension.length_y << endl;
  ofp << dimension.number_of_uavs << endl;
  ofp << dimension.perc_obs << endl;
  ofp.close();
}

void readCTLSpec(string &ctlspec)
{
  ifstream ifp;
  string line;

  ifp.open("../examples/ctlspec.txt");
  if (ifp.is_open())
  {
    while (getline(ifp,line))
    {
	ctlspec.append(line);
	ctlspec.append("\n");
    }
    ifp.close();
  }
  else
  {
    cout << "ctlspec.txt file cannot be opened.." << endl;
    exit(0);
  }
}
