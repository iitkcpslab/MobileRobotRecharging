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
      if ((count1 + 1) == 1)
      {
        ofp << "(declare-const r" << count1 + 1 << "parking1_" << count2 + 1 << " Bool)" << endl;
      }      
      if ((count1 + 1) == 2)
      {
        ofp << "(declare-const r" << count1 + 1 << "parking2_" << count2 + 1 << " Bool)" << endl;
      }
      if ((count1 + 1) == 3)
      {
      ofp << "(declare-const r" << count1 + 1 << "parking3_" << count2 + 1 << " Bool)" << endl;
      }
      if ((count1 + 1) == 4)
      {
      ofp << "(declare-const r" << count1 + 1 << "parking4_" << count2 + 1 << " Bool)" << endl;
      }

      ofp << "(declare-const r" << count1 + 1 << "mailbox1_" << count2 + 1 << " Bool)" << endl;
      ofp << "(declare-const r" << count1 + 1 << "mailbox2_" << count2 + 1 << " Bool)" << endl;

      if ((count1 + 1) == 1)
      {
      ofp << "(declare-const r" << count1 + 1 << "deliver1_" << count2 + 1 << " Bool)" << endl;
      }
      if ((count1 + 1) == 2)
      {
      ofp << "(declare-const r" << count1 + 1 << "deliver2_" << count2 + 1 << " Bool)" << endl;
      }
      if ((count1 + 1) == 3)
      {
        ofp << "(declare-const r" << count1 + 1 << "deliver3_" << count2 + 1 << " Bool)" << endl;
      }
      if ((count1 + 1) == 4)
      {
        ofp << "(declare-const r" << count1 + 1 << "deliver4_" << count2 + 1 << " Bool)" << endl;
      }

      ofp << "(declare-const r" << count1 + 1 << "collect1_" << count2 + 1 << " Bool)" << endl;
      ofp << "(declare-const r" << count1 + 1 << "collect2_" << count2 + 1 << " Bool)" << endl;
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
      // Parking
      if ((count1 + 1) == 1)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "parking1_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 16)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12))"; 
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12))))))" << endl; 
      
        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)"; 
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 16)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12))"; 
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12))))"; 
        ofp << " (= r" << count1+ 1 << "parking1_" << count2 + 1 << " true)))" << endl;
      }
      
      if ((count1 + 1) == 2)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "parking2_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 14)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12))";        
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 15)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 14)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 15)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 12))))";
        ofp << " (= r" << count1+ 1 << "parking2_" << count2 + 1 << " true)))" << endl;
      }

      if ((count1 + 1) == 3)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "parking3_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 3))";        
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 16)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 3))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 17)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 3))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 16)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 3))))";
        ofp << " (= r" << count1+ 1 << "parking3_" << count2 + 1 << " true)))" << endl;
      }

      if ((count1 + 1) == 4)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "parking4_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 15)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 3))";        
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 14)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 3))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 15)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 3))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 14)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 3))))";
        ofp << " (= r" << count1+ 1 << "parking4_" << count2 + 1 << " true)))" << endl;
      }
 
      // Mailbox
      ofp << "(assert (=> (= r" << count1 + 1 << "mailbox1_" << count2 + 1 << " true)";
      ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 8))"; 
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 9))))))" << endl;

      ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 8))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 9))))";
      ofp << " (= r" << count1+ 1 << "mailbox1_" << count2 + 1 << " true)))" << endl;

      ofp << "(assert (=> (= r" << count1 + 1 << "mailbox2_" << count2 + 1 << " true)";
      ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 6))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 7))))))" << endl;

      ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 6))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 13)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 7))))";
      ofp << " (= r" << count1+ 1 << "mailbox2_" << count2 + 1 << " true)))" << endl;
 
      // deliver
      if ((count1 + 1) == 1)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "deliver1_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 14))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 10)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 14))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 9)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 14))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 10)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 14))))";
        ofp << " (= r" << count1+ 1 << "deliver1_" << count2 + 1 << " true)))" << endl;
      }
 
      if ((count1 + 1) == 2)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "deliver2_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 2)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 14))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 3)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 14))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 2)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 14))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 3)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 14))))";
        ofp << " (= r" << count1+ 1 << "deliver2_" << count2 + 1 << " true)))" << endl;
      }

      if ((count1 + 1) == 3)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "deliver3_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 7)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 7)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 8)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1))))";
        ofp << " (= r" << count1+ 1 << "deliver3_" << count2 + 1 << " true)))" << endl;
      }
 
      if ((count1 + 1) == 4)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "deliver4_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 4)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 4))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 4)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 5))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 4)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 4))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 4)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 5))))";
        ofp << " (= r" << count1+ 1 << "deliver4_" << count2 + 1 << " true)))" << endl;
      }

      /*if ((count1 + 1) == 3)
      {
        ofp << "(assert (=> (= r" << count1 + 1 << "deliver3_" << count2 + 1 << " true)";
        ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 2)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 3)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1))))))" << endl;

        ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
        ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 2)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1))";
        ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 3)";
        ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 1))))";
        ofp << " (= r" << count1+ 1 << "deliver3_" << count2 + 1 << " true)))" << endl;
      }*/
 
      // collect
      ofp << "(assert (=> (= r" << count1 + 1 << "collect1_" << count2 + 1 << " true)";
      ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 11)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 10))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 11)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 11))))))" << endl;

      ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 11)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 10))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 11)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 11))))";
      ofp << " (= r" << count1+ 1 << "collect1_" << count2 + 1 << " true)))" << endl;

      ofp << "(assert (=> (= r" << count1 + 1 << "collect2_" << count2 + 1 << " true)";
      ofp << " (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 11)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 2))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 11)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 3))))))" << endl;

      ofp << "(assert (=> (and (= vel_i_" << count1 + 1 << "_" << count2 + 1 << " 0)";
      ofp << " (or (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 11)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 2))";
      ofp << " (and (= x_" << count1 + 1 << "_" << count2 + 1 << " 11)";
      ofp << " (= y_" << count1 + 1 << "_" << count2 + 1 << " 3))))";
      ofp << " (= r" << count1+ 1 << "collect2_" << count2 + 1 << " true)))" << endl;
    }
  }
  ofp << endl;
}
