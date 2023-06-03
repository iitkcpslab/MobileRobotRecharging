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
      ofp << "(declare-const r" << count1 + 1 << "gather1_" << count2 + 1 << " Bool)" << endl;
      ofp << "(declare-const r" << count1 + 1 << "gather2_" << count2 + 1 << " Bool)" << endl;
      ofp << "(declare-const r" << count1 + 1 << "gather3_" << count2 + 1 << " Bool)" << endl;
      ofp << "(declare-const r" << count1 + 1 << "gather4_" << count2 + 1 << " Bool)" << endl;
      ofp << "(declare-const r" << count1 + 1 << "upload1_" << count2 + 1 << " Bool)" << endl;
      ofp << "(declare-const r" << count1 + 1 << "upload2_" << count2 + 1 << " Bool)" << endl;
    }

    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << "(declare-const r" << count1 + 1 << "gather_" << count2 + 1 << " Bool)" << endl;
      ofp << "(declare-const r" << count1 + 1 << "upload_" << count2 + 1 << " Bool)" << endl;
    }

    ofp << "(declare-const gather1_" << count2 + 1 << " Bool)" << endl;
    ofp << "(declare-const gather2_" << count2 + 1 << " Bool)" << endl;
    ofp << "(declare-const gather3_" << count2 + 1 << " Bool)" << endl;
    ofp << "(declare-const gather4_" << count2 + 1 << " Bool)" << endl;
    ofp << "(declare-const upload1_" << count2 + 1 << " Bool)" << endl;
    ofp << "(declare-const upload2_" << count2 + 1 << " Bool)" << endl;
    ofp << "(declare-const gather_" << count2 + 1 << " Bool)" << endl;
    ofp << "(declare-const upload_" << count2 + 1 << " Bool)" << endl;
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
      ofp << "(assert (=> (= r" << count1 + 1 << "gather1_" << count2 + 1 << " true)";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 5))))" << endl; 
      
      ofp << "(assert (=> (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 5))"; 
      ofp << " (= r" << count1+ 1 << "gather1_" << count2 + 1 << " true)))" << endl;

      ofp << "(assert (=> (= r" << count1 + 1 << "gather2_" << count2 + 1 << " true)";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 9))))" << endl; 
      
      ofp << "(assert (=> (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 9))"; 
      ofp << " (= r" << count1+ 1 << "gather2_" << count2 + 1 << " true)))" << endl;

      ofp << "(assert (=> (= r" << count1 + 1 << "gather3_" << count2 + 1 << " true)";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 13))))" << endl; 
      
      ofp << "(assert (=> (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 13))"; 
      ofp << " (= r" << count1+ 1 << "gather3_" << count2 + 1 << " true)))" << endl;

      ofp << "(assert (=> (= r" << count1 + 1 << "gather4_" << count2 + 1 << " true)";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 5)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 9))))" << endl; 
      
      ofp << "(assert (=> (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 5)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 9))"; 
      ofp << " (= r" << count1+ 1 << "gather4_" << count2 + 1 << " true)))" << endl;

      ofp << "(assert (=> (= r" << count1 + 1 << "upload1_" << count2 + 1 << " true)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 17))"; 
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 1)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 17))"; 
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 1)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 18)))))" << endl; 
      
      ofp << "(assert (=> (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 17))"; 
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 1)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 17))"; 
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 1)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 18)))"; 
      ofp << " (= r" << count1+ 1 << "upload1_" << count2 + 1 << " true)))" << endl;

      ofp << "(assert (=> (= r" << count1 + 1 << "upload2_" << count2 + 1 << " true)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 0))"; 
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1))"; 
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 18)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1)))))" << endl; 
      
      ofp << "(assert (=> (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 0))"; 
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1))"; 
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 18)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1)))"; 
      ofp << " (= r" << count1+ 1 << "upload2_" << count2 + 1 << " true)))" << endl;
    }
    ofp << endl;
  
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << "(assert (=> (= r" << count1 + 1 << "gather_" << count2 + 1 << " true)";
      ofp << " (or (= r" << count1 + 1 << "gather1_" << count2 + 1 << " true)";
      ofp << " (= r" << count1 + 1 << "gather2_" << count2 + 1 << " true)";
      ofp << " (= r" << count1 + 1 << "gather3_" << count2 + 1 << " true)";
      ofp << " (= r" << count1 + 1 << "gather4_" << count2 + 1 << " true))))" << endl;
      
      ofp << "(assert (=> (or (= r" << count1 + 1 << "gather1_" << count2 + 1 << " true)";
      ofp << " (= r" << count1 + 1 << "gather2_" << count2 + 1 << " true)";
      ofp << " (= r" << count1 + 1 << "gather3_" << count2 + 1 << " true)";
      ofp << " (= r" << count1 + 1 << "gather4_" << count2 + 1 << " true))";
      ofp << " (= r" << count1 + 1 << "gather_" << count2 + 1 << " true)))" << endl;
    }
    ofp << endl;
  
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << "(assert (=> (= r" << count1 + 1 << "upload_" << count2 + 1 << " true)";
      ofp << " (or (= r" << count1 + 1 << "upload1_" << count2 + 1 << " true)";
      ofp << " (= r" << count1 + 1 << "upload2_" << count2 + 1 << " true))))" << endl;
      
      ofp << "(assert (=> (or (= r" << count1 + 1 << "upload1_" << count2 + 1 << " true)";
      ofp << " (= r" << count1 + 1 << "upload2_" << count2 + 1 << " true))";
      ofp << " (= r" << count1 + 1 << "upload_" << count2 + 1 << " true)))" << endl;
    }
    ofp << endl;

    ofp << "(assert (=> (= gather1_" << count2 + 1<< " true) (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "gather1_" << count2 + 1 << " true)"; 
    }
    ofp << ")))" << endl;
  
    ofp << "(assert (=> (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "gather1_" << count2 + 1 << " true)"; 
    }
    ofp << ") (= gather1_" << count2 + 1 << " true)))" << endl;

    ofp << "(assert (=> (= gather2_" << count2 + 1<< " true) (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "gather2_" << count2 + 1 << " true)"; 
    }
    ofp << ")))" << endl;
  
    ofp << "(assert (=> (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "gather2_" << count2 + 1 << " true)"; 
    }
    ofp << ") (= gather2_" << count2 + 1 << " true)))" << endl;

    ofp << "(assert (=> (= gather3_" << count2 + 1 << " true) (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "gather3_" << count2 + 1 << " true)"; 
    }
    ofp << ")))" << endl;
  
    ofp << "(assert (=> (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "gather3_" << count2 + 1 << " true)"; 
    }
    ofp << ") (= gather3_" << count2 + 1 << " true)))" << endl;

    ofp << "(assert (=> (= gather4_" << count2 + 1 << " true) (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "gather4_" << count2 + 1 << " true)"; 
    }
    ofp << ")))" << endl;
  
    ofp << "(assert (=> (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "gather4_" << count2 + 1 << " true)"; 
    }
    ofp << ") (= gather4_" << count2 + 1 << " true)))" << endl;

    ofp << "(assert (=> (= upload1_" << count2 + 1 << " true) (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "upload1_" << count2 + 1 << " true)"; 
    }
    ofp << ")))" << endl;
  
    ofp << "(assert (=> (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "upload1_" << count2 + 1 << " true)"; 
    }
    ofp << ") (= upload1_" << count2 + 1 << " true)))" << endl;

    ofp << "(assert (=> (= upload2_" << count2 + 1 << " true) (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "upload2_" << count2 + 1 << " true)"; 
    }
    ofp << ")))" << endl;
  
    ofp << "(assert (=> (or";
    for (count1 = 0; count1 < workspace.number_of_uavs; count1++)
    {
      ofp << " (= r" << count1 + 1 << "upload2_" << count2 + 1 << " true)"; 
    }
    ofp << ") (= upload2_" << count2 + 1 << " true)))" << endl;

    ofp << "(assert (=> (= gather_" << count2 + 1 << " true) (or (= gather1_" << count2 + 1 << " true) (= gather2_" << count2 + 1 << " true) (= gather3_" << count2 + 1 << " true) (= gather4_" << count2 + 1 << " true))))" << endl;
    ofp << "(assert (=> (or (= gather1_" << count2 + 1 << " true) (= gather2_" << count2 + 1 << " true) (= gather3_" << count2 + 1 << " true) (= gather4_" << count2 + 1 << " true)) (= gather_" << count2 + 1 << " true)))" << endl;

    ofp << "(assert (=> (= upload_" << count2 + 1 << " true) (or (= upload1_" << count2 + 1 << " true) (= upload2_" << count2 + 1 << " true))))" << endl;
    ofp << "(assert (=> (or (= upload1_" << count2 + 1 << " true) (= upload2_" << count2 + 1 << " true)) (= upload_" << count2 + 1 << " true)))" << endl;
    ofp << endl;
  }
  ofp << endl;
}

