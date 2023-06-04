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
#include <math.h>
#include "primitive.h"
#include "readinputs.h"
#include "writeconstraints.h"
#include "writespecificationconstraints.h"
#include "generatez3file.h"
using namespace std;

void generateZ3File(prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace)
{ 
  ofstream ofp;
  
  ofp.open("constraints.smt2");
   /* Declare the variables */
  ofp << "(set-option :produce-unsat-cores true)" << endl;
  declareVariables(ofp, workspace); 


  /* Write the General Constraints */
  writeInitialLocationConstraints(ofp, workspace, obstacles);
  writeTransitionConstraints(ofp, primitives, obstacles, workspace);
  //writeCollisionAvoidanceConstraints2(ofp, primitives, workspace);
  //writeCostConstraint(ofp, workspace);
 
  /* Write the specification constraints */
  writeFinalDestinationConstraints(ofp, workspace);
  
  //writeFinalDestinationConstraints2(ofp, workspace);

  //writeFormationConstraints(ofp, workspace);
  //ofp << endl;  
  //writePrecedenceConstraints(ofp, workspace);
  //ofp << endl;
  //writeDistanceConstraints(ofp, workspace);
  //ofp << endl;
  /* Check the satisfiability of the constraints and output the model */
  writeOutputConstraints(ofp, workspace);
  ofp << "(check-sat)" << endl;
  ofp << "(get-unsat-core)" << endl;
  ofp << "(get-model)" << endl;
 
  ofp.close();
}
