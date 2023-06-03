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
      ofp << "(declare-const r" << count1 + 1 << "takechemical_" << count2 + 1 << " Bool)" << endl;
      ofp << "(declare-const r" << count1 + 1 << "dropchemical_" << count2 + 1 << " Bool)" << endl;
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
      if ((count1 + 1) == 1)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "takechemical_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 7))"; 
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 8))))))" << endl; 
      
        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 7))"; 
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 8))))"; 
        ofp << " (= r" << count1+ 1 << "takechemical_" << count2 + 1 << " true)))" << endl;
      }
     
      if ((count1 + 1) == 2)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "takechemical_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 0))";        
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 0))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 0))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 0))))";
        ofp << " (= r" << count1+ 1 << "takechemical_" << count2 + 1 << " true)))" << endl;
      }
   
      if ((count1 + 1) == 3)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "takechemical_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 7))";        
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 8))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 7))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 8))))";
        ofp << " (= r" << count1+ 1 << "takechemical_" << count2 + 1 << " true)))" << endl;
      }
  
      if ((count1 + 1) == 4)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "takechemical_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 15))";        
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 15))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 15))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 15))))";
        ofp << " (= r" << count1+ 1 << "takechemical_" << count2 + 1 << " true)))" << endl;
      }

      ofp << "(assert (=> (= r" << count1 + 1 << "dropchemical_" << count2 + 1 << " true)";
      ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 7))"; 
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 7))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 8))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 8))))))" << endl;

      ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 7))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 7))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 8))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 8))))";
      ofp << " (= r" << count1+ 1 << "dropchemical_" << count2 + 1 << " true)))" << endl;
    }
  }
  ofp << endl;
}

