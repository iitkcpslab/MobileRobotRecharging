#include <iostream>
#include <fstream>
#include "../utils/primitive.h"
#include "../utils/readinputs.h"
#include "definepropositions.h"


void declarePropositions(ofstream &ofp, workspace_t workspace)
{
  unsigned int count1, count2;


  for (count2 = 0; count2 < workspace.number_of_points; count2++)
  {
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
 	ofp << "(declare-const r" << count1 + 1 << "pick_" << count2 + 1 <<" Bool)" << endl;
 	ofp << "(declare-const r" << count1 + 1 << "drop_" << count2 + 1 <<" Bool)" << endl;
 	ofp << "(declare-const r" << count1 + 1 << "chrg_" << count2 + 1 <<" Bool)" << endl;
    }
  }
  ofp << endl;
}


void definePropositions(ofstream &ofp, workspace_t workspace)
{
  unsigned int count1, count2; 

  for (count2 = 0; count2 < workspace.number_of_points; count2++)
  {
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      	// Pick
        ofp << "(assert (=> (= r" << count1 + 1 << "pick_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 6))"; 
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 2)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 10))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12))))))" << endl; 

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 6))"; 
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 2)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 10))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12))))"; 
        ofp << " (= r" << count1 + 1 << "pick_" << count2 + 1 << " true)))";

      	// Drop
        ofp << "(assert (=> (= r" << count1 + 1 << "drop_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 1)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 6))"; 
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 10)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 15))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 11)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 2))))))" << endl; 

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 1)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 6))"; 
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 10)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 15))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 11)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 2))))"; 
        ofp << " (= r" << count1 + 1 << "drop_" << count2 + 1 << " true)))";
/*
      	// Chrg
        ofp << "(assert (=> (= r" << count1 + 1 << "chrg_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 10)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12)))))" << endl; 

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 10)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12)))"; 
        ofp << " (= r" << count1 + 1 << "chrg_" << count2 + 1 << " true)))";
*/	
      }
  }
  ofp << endl;
}
