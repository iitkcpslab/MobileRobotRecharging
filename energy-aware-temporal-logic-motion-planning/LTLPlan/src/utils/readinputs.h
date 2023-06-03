/* License */
/*
Copyright (c) <2014>, <Indranil Saha>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/


struct w
{
  unsigned int length_x;
  unsigned int length_y;
  unsigned int number_of_uavs;
  position *pos_start;
  position *pos_end;
  unsigned int number_of_points;
  string total_cost;
  int rem_charge;
  int charge_thres;
  int recharge_amt;
};

typedef struct w workspace_t;


struct d
{  
  unsigned int length_x;
  unsigned int length_y;
  unsigned int number_of_uavs;
  unsigned int perc_obs;
};

typedef struct d dimension_t;


struct c
{
  float max_cost;
  float min_cost;
  float min2_cost;
  float min_cost_diff;
  float min2_min_cost_diff;
};

typedef struct c prim_cost_t;

 
typedef std::vector<Primitive> prim_vec_t;


void readPrimitives(prim_vec_t & ); 
void writePrimitives(prim_vec_t );
void readObstacles(pos_vec_t & );
void writeObstacles(pos_vec_t );
void writeObstaclesToFile(pos_vec_t );
void readWorkspace(workspace_t &);
void writeWorkspace(workspace_t);
void readDimension(dimension_t &);
void writeDimension(dimension_t);
void writeDimensionToFile(dimension_t );
void getPrimitiveCost(prim_vec_t , prim_cost_t & );
void writePrimitiveCost(prim_cost_t & );
