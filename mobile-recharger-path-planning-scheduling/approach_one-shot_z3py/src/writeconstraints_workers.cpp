#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include "primitive.h"
#include "readinputs.h"
#include "writeconstraints_workers.h"

void declareVariables_workers (ofstream &ofp, workspace_t workspace, worker_vec_t workers)
{
  unsigned int count1, count2;
  ofp << "# declaration : constants for workers" << endl;
  for (count1 = 0; count1 < workspace.number_of_wrobs; count1++)
  {
    for (count2 = 0; count2 < workspace.hlen; count2++)
    {
	ofp << "wtraj_" << count1+1 << "_" << count2+1 << " = Int('wtraj_" << count1+1 << "_" << count2+1 << "')" << endl;
    }
    ofp << endl;
  }
  ofp << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    {
	ofp << "wprim_" << count1 << "_" << count2 << " = Int('wprim_" << count1 << "_" << count2 << "')" << endl;
    }
    ofp << endl;
  }
  ofp << endl;  
  for (count1 = 0; count1 < workspace.number_of_wrobs; count1++)
  {
    for (count2 = 0; count2 < workspace.hlen; count2++)
    {
	ofp << "wx_" << count1+1 << "_" << count2+1 << " = Int('wx_" << count1+1 << "_" << count2+1 << "')" << endl;
    }
    ofp << endl;
  }
  ofp << endl;
  for (count1 = 0; count1 < workspace.number_of_wrobs; count1++)
  {
    for (count2 = 0; count2 < workspace.hlen; count2++)
    {
	ofp << "wy_" << count1+1 << "_" << count2+1 << " = Int('wy_" << count1+1 << "_" << count2+1 << "')" << endl;
    }
    ofp << endl;
  }
  ofp << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    {
	ofp << "ch_" << count1 << "_" << count2 << " = Int('ch_" << count1 << "_" << count2 << "')" << endl;
    }
    ofp << endl;
  }
  ofp << endl;
  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for(count2=1; count2<workspace.hlen; count2++)
    {
     ofp << "waitcount_" << count1 << "_" << count2 << " = Int('waitcount_" << count1 << "_" << count2 << "')" << endl;
    }
  }
  ofp << endl;
  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for(count2=1; count2<workspace.hlen; count2++)
    {
     ofp << "rechcount_" << count1 << "_" << count2 << " = Int('rechcount_" << count1 << "_" << count2 << "')" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++) //change15
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "rechassigned_" << count1 << "_" << count2 << " = Int('rechassigned_" << count1 << "_" << count2 << "')" << endl;
    }
  }
  ofp << endl;
  ofp << "total_wait = Int('total_wait')" << endl;
  ofp << "total_rech = Int('total_rech')" << endl;
}

/*
void declareVariables_workers2 (ofstream &ofp, workspace_t workspace, worker_vec_t workers, workerhalt_vec_t workerhalt, unsigned int max_timept)
{
  unsigned int count1, count2;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
        ofp << "(declare-const wprim_" << count1 << "_" << count2 <<" Int)" << endl;
    }
    ofp << endl;
  }
  ofp << endl;  

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept; count2++)
    {
        ofp << "(declare-const wx_" << count1 << "_" << count2 <<" Int)" << endl;
    }
    ofp << endl;
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept; count2++)
    {
        ofp << "(declare-const wy_" << count1 << "_" << count2 <<" Int)" << endl;
    }
    ofp << endl;
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept; count2++)
    {
        ofp << "(declare-const ch_" << count1 << "_" << count2 << " Int)" << endl;
    }
    ofp << endl;
  }
  ofp << endl;

  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
     ofp << "(declare-const rechcount_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
     ofp << "(declare-const waitcount_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++) //change15
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
      ofp << "(declare-const rechassigned_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  ofp << "(declare-const total_rech" << " Int)" << endl << endl;
}
*/


void instantiateVariables_workers (ofstream &ofp, workspace_t workspace, worker_vec_t workers)
{
  unsigned int count1, count2;
  ofp << "# instantiate : instantiation of constants for workers" << endl;
  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
     ofp << "s.add(wtraj_" << count1 << "_1==1)" << endl;
  }
  ofp << endl << endl;

  ofp << "# instantiate : trajectory point constraints for workers" << endl;
  for (count1 = 0; count1 < workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 < workspace.hlen; count2++)
    {
	ofp << "s.add(wtraj_" << count1+1 << "_" << count2+1 << ">=1, wtraj_" << count1+1 << "_" << count2+1 << "<=" << workers[count1].looplen << ")" << endl;
    }
  }
  ofp << endl;
 
  ofp << "# instantiate : moving/not-moving/recharging for workers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
	ofp << "s.add(wprim_" << count1 << "_" << count2 << ">=0, wprim_" << count1 << "_" << count2 << "<=2)" << endl;
    }
  }
  ofp << endl;

  ofp << "# instantiate : x-coordinate range for workers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    {
	ofp << "s.add(wx_" << count1 << "_" << count2 << ">=" << workspace.min_x << ", wx_" << count1 << "_" << count2 << "<=" << workspace.length_x << ")" << endl;
    }
  }
  ofp << endl;

  ofp << "# instantiate : y-coordinate range for workers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    {
	ofp << "s.add(wy_" << count1 << "_" << count2 << ">=" << workspace.min_y << ", wy_" << count1 << "_" << count2 << "<=" << workspace.length_y << ")" << endl;
    }
  }
  ofp << endl;

  ofp << "# instantiate : full charge at the beginning, for workers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
     ofp << "s.add(ch_" << count1 << "_1==" << workers[count1-1].fch << ")" << endl;
  }
  ofp << endl;

  ofp << "# instantiate : range of charge, for workers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    {
	ofp << "s.add(ch_" << count1 << "_" << count2 << ">=0" << ", ch_" << count1 << "_" << count2 << "<=" << workers[count1-1].fch << ")" << endl;
    }
  }
  ofp << endl;

  ofp << "# instantiate : waitcount for workers" << endl;
  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for(count2=1; count2<workspace.hlen; count2++)
    {
      ofp << "s.add(waitcount_" << count1 << "_" << count2 << ">=0" << ", waitcount_" << count1 << "_" << count2 << "<=1)" << endl;
    }
  }
  ofp << endl;

  ofp << "# instantiate : rechcount for workers" << endl;
  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for(count2=1; count2<workspace.hlen; count2++)
    {
      ofp << "s.add(rechcount_" << count1 << "_" << count2 << ">=0" << ", rechcount_" << count1 << "_" << count2 << "<=1)" << endl;
    }
  }
  ofp << endl;

  ofp << "# instantiate : rechassigned for workers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "s.add(rechassigned_" << count1 << "_" << count2 << ">=1" << ", rechassigned_" << count1 << "_" << count2 << "<=2)" << endl;
     
    }
  }
  ofp << endl;
}


void instantiateVariables_workers2 (ofstream &ofp, workspace_t workspace, worker_vec_t workers, workerhalt_vec_t workerhalt, unsigned int max_timept)
{
  unsigned int count1, count2;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
        ofp << "(assert (or (= wprim_" << count1 << "_" << count2 << " 0) ";
        ofp << "(= wprim_" << count1 << "_" << count2 << " 2)))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = workerhalt[count1-1].timept+1; count2 <= max_timept; count2++)
    {
        ofp << "(assert (and (>= ch_" << count1 << "_" << count2 << " 0) ";
        ofp << "(<= ch_" << count1 << "_" << count2 << " " << workers[count1-1].fch << ")))" << endl;
    }
    ofp << endl;
  }
  ofp << endl;

  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for (count2 = workerhalt[count1-1].timept; count2 <= max_timept-1; count2++)
    {
      ofp << "(assert (and (>= rechcount_" << count1 << "_" << count2 << " 0) " << endl;
      ofp << "(<= rechcount_" << count1 << "_" << count2 << " 1)))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++) //change15
  {
    for (count2 = workerhalt[count1-1].timept; count2 <= max_timept-1; count2++)
    {
      ofp << "(assert (and (>= rechassigned_" << count1 << "_" << count2 << " 1) " << endl;
      ofp << "(<= rechassigned_" << count1 << "_" << count2 << " 2)))" << endl;
    }
  }
  ofp << endl;
}


void writeMatchingConstraints (ofstream &ofp, workspace_t workspace, worker_vec_t workers)
{
  unsigned int count1;
  ofp << "# matching : same location for workers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    ofp << "s.add(And(";
    ofp << "wx_" << count1 << "_1==wx_" << count1 << "_" << workspace.hlen << ", ";
    ofp << "wy_" << count1 << "_1==wy_" << count1 << "_" << workspace.hlen << "))" << endl;
  }
  ofp << endl;

  // added to make it one-shot -- charge matching for workers
  ofp << "# matching : same charge-level for workers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    ofp << "s.add(";
    ofp << "ch_" << count1 << "_1==ch_" << count1 << "_" << workspace.hlen << ")" << endl;
  }
  ofp << endl;

  // added to make it one-shot -- location matching for rechargers
  ofp << "# matching : same location for rechargers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    ofp << "s.add(And(";
    ofp << "rx_" << count1 << "_1==rx_" << count1 << "_" << workspace.hlen << ", ";
    ofp << "ry_" << count1 << "_1==ry_" << count1 << "_" << workspace.hlen << "))" << endl;
  }
  ofp << endl;
}


void writeMatchingConstraints_workers2 (ofstream &ofp, workspace_t workspace, worker_vec_t workers, workerhalt_vec_t workerhalt, unsigned int rstart_timept, unsigned int max_timept)
{
  unsigned int count1, count2;

  ofp << "; matching constraints for rechargers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    ofp << "(assert (and (= rx_" << count1 << "_" << rstart_timept << " " << workspace.rpos_hlen[count1-1].x << ") ";
    ofp << "(= ry_" << count1 << "_" << rstart_timept << " " << workspace.rpos_hlen[count1-1].y << ")))" << endl;

    ofp << "(assert (and (= rx_" << count1 << "_" << max_timept << " " << workspace.rpos_start[count1-1].x << ") ";
    ofp << "(= ry_" << count1 << "_" << max_timept << " " << workspace.rpos_start[count1-1].y << ")))" << endl;
  }

  ofp << "; matching constraints for workers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = workerhalt[count1-1].timept; count2 <= max_timept; count2++)
    {
      ofp << "(assert (and (= wx_" << count1 << "_" << count2 << " " << workers[count1-1].wpos_start.x << ") ";
      ofp << "(= wy_" << count1 << "_" << count2 << " " << workers[count1-1].wpos_start.y << ")))" << endl;
    }
    ofp << endl;
  }
  ofp << endl;
  /* specify charge at the point when the workers stopped moving */
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    ofp << "(assert (= ch_" << count1 << "_" << workerhalt[count1-1].timept << " " << workerhalt[count1-1].charge << "))" << endl;
  }
  ofp << endl;

  /* specify charge at the last point of hypercycle */
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    ofp << "(assert (= ch_" << count1 << "_" << max_timept << " " << workers[count1-1].fch << "))" << endl;
  }
  ofp << endl;
}


void writeTrajectoryToLoopMapping_workers (ofstream &ofp, workspace_t workspace, worker_vec_t workers)
{
  unsigned int count1, count2, count3;
  ofp << "# mapping : Worker trajectory to loop point" << endl;
  for(count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for(count2=1; count2<=workspace.hlen; count2++)
    {
      for(count3=1; count3<=workers[count1-1].looplen; count3++)
      {
	 ofp << "s.add(Implies(wtraj_" << count1 << "_" << count2 << "==" << count3 << ", "; // antecedent
	 ofp << "And(";
	 ofp << "wx_" << count1 << "_" << count2 << "==" << workers[count1-1].looptraj[count3-1].x << ", ";
	 ofp << "wy_" << count1 << "_" << count2 << "==" << workers[count1-1].looptraj[count3-1].y << ")))" << endl;
      }
    }
  }
  ofp << endl;
}


void placeRecharger1 (ofstream &ofp, worker_vec_t workers, unsigned int w_id, unsigned int timept, unsigned int r_id, int ofs_x, int ofs_y) 
{
  ofp << "And(";
  ofp << "rprim_" << r_id << "_" << timept << "==1, ";
  ofp << "rechassigned_" << w_id << "_" << timept << "==" << r_id << ", ";
  ofp << "rx_" << r_id << "_" << timept << "==wx_" << w_id << "_" << timept << "+" << ofs_x << ", ";
  ofp << "ry_" << r_id << "_" << timept << "==wy_" << w_id << "_" << timept << "+" << ofs_y << "), " << endl;
  return;
}


void writeTransition_workers (ofstream &ofp, workspace_t workspace, worker_vec_t workers)
{
  unsigned int count1, count2, count3;
  worker_t worker;

  ofp << "# transition : for workers" << endl;
  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for (count2=1; count2<=workspace.hlen-1; count2++)
    {
      ofp << "rech_amt_" << count1 << "_" << count2 << " = Int('rech_amt_" << count1 << "_" << count2 << "')" << endl;
    }
  }
  ofp << endl;

  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for (count2=1; count2<=workspace.hlen-1; count2++)
    {
      ofp << "s.add(And(";
      ofp << "rech_amt_" << count1 << "_" << count2 << "<=" << workspace.recharge << ", ";
      ofp << "rech_amt_" << count1 << "_" << count2 << ">0))" << endl;
    }
  }
  ofp << endl;

  ofp << "# recharging : intermediate" << endl;
  for(count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    ofp << "fch_" << count1 << " = Int('fch_" << count1 << "')" << endl;
    ofp << "s.add(fch_" << count1 << "==" << workers[count1-1].fch << ")" << endl << endl;

    worker = workers[count1-1];
    for(count2=1; count2<=workspace.hlen-1; count2++)
    {
      ofp << "# wprim = 1 : robot is on move" << endl;
      ofp << "s.add(";
      ofp << "Implies(And(";
      ofp << "wtraj_" << count1 << "_" << count2 << "<" << worker.looplen << ","; // antecedent
      ofp << "wprim_" << count1 << "_" << count2 << "==1), " << endl; // antecedent
      ofp << "And(";
      ofp << "wtraj_" << count1 << "_" << count2+1 << "==wtraj_" << count1 << "_" << count2 << "+1, "; // cons 
      ofp << "ch_" << count1 << "_" << count2+1 << "==ch_" << count1 << "_" << count2 << " -" << worker.req_charge[(count2-1)%worker.looplen] << ")), " << endl; // consequence


      ofp << "# wprim = 1 : robot is on move, circular return to first pos" << endl;
      ofp << "Implies(And(";
      ofp << "wtraj_" << count1 << "_" << count2 << "==" << worker.looplen << ","; // antecedent
      ofp << "wprim_" << count1 << "_" << count2 << "==1), " << endl; // antecedent
      ofp << "And(";
      ofp << "wtraj_" << count1 << "_" << count2+1 << "==1, "; // cons 
      ofp << "ch_" << count1 << "_" << count2+1 << "==ch_" << count1 << "_" << count2 << " -" << worker.req_charge[(count2-1)%worker.looplen] << ")), " << endl; // consequence


      ofp << "# wprim = 0 : robot is static" << endl;
      ofp << "Implies(And(";
      ofp << "wprim_" << count1 << "_" << count2 << "==0), " << endl; // antecedent
      ofp << "And(";
      ofp << "wtraj_" << count1 << "_" << count2+1 << "==wtraj_" << count1 << "_" << count2 << ", "; // cons 
      ofp << "ch_" << count1 << "_" << count2+1 << "==ch_" << count1 << "_" << count2 << "))"; // consequence
      ofp << ")" << endl;
    }
    ofp << endl;
  }

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    worker = workers[count1-1];
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "# wprim = 2" << endl;
      ofp << "s.add(";
      ofp << "Implies(";
      ofp << "wprim_" << count1 << "_" << count2 << "==2, " << endl; // antecedent
      /* consequence -- start */
      ofp << "And(";
      ofp << "wtraj_" << count1 << "_" << count2+1 << "==wtraj_" << count1 << "_" << count2 << ", ";
      ofp << "ch_" << count1 << "_" << count2 << "<" << worker.fch << ", ";
      ofp << "ch_" << count1 << "_" << count2+1 << "==ch_" << count1 << "_" << count2 << "+" << "rech_amt_" << count1 << "_" << count2 << ", "<< endl;

      ofp << "Or(" << endl;
      for (count3 = 1; count3 <= workspace.number_of_rechs; count3++)
      {
        placeRecharger1 (ofp, workers, count1, count2, count3,  1,  0);
        placeRecharger1 (ofp, workers, count1, count2, count3,  1,  1);
        placeRecharger1 (ofp, workers, count1, count2, count3,  0,  1);
        placeRecharger1 (ofp, workers, count1, count2, count3, -1,  1);
        placeRecharger1 (ofp, workers, count1, count2, count3, -1,  0);
        placeRecharger1 (ofp, workers, count1, count2, count3, -1, -1);
        placeRecharger1 (ofp, workers, count1, count2, count3,  0, -1);
        placeRecharger1 (ofp, workers, count1, count2, count3,  1, -1);
      } 
      ofp << "))))" << endl;
      /* consequence -- end */
    }
  }
  ofp << endl;
}


void writeTransition_workers2 (ofstream &ofp, workspace_t workspace, worker_vec_t workers, workerhalt_vec_t workerhalt, unsigned int max_timept)
{
  unsigned int count1, count2, count3;
  worker_t worker;
  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
      ofp << "(declare-const rech_amt_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }

  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
      ofp << "(assert (and (<= rech_amt_" << count1 << "_" << count2 <<  " " << workspace.recharge << ") ";
      ofp << "(> rech_amt_" << count1 << "_" << count2 << " 0)))" << endl; //change11
    }
  }

  /* intermediate recharging */
  for(count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    ofp << "(declare-const fch_" << count1 << " Int)" << endl;
    ofp << "(assert (= fch_" << count1 << " " << workers[count1-1].fch << "))" << endl;
    worker = workers[count1-1];
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
      /* changes in transition and charge for a STATIC primitive */
      ofp << "; wprim = 0" << endl;
      ofp << "(assert (=> (= wprim_" << count1 << "_" << count2 << " 0) " << endl;
      ofp << "(= ch_" << count1 << "_" << count2+1 << " ch_" << count1 << "_" << count2 << ")))" << endl << endl;
    }
  }

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    worker = workers[count1-1];
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
      ofp << "(assert (=> (= wprim_" << count1 << "_" << count2 << " 2)" << endl;
      ofp << "(and" << endl;
      ofp << "(< ch_" << count1 << "_" << count2 << " " << worker.fch << ")" << endl; //change 30jan2019
      ofp << "(= ch_" << count1 << "_" << count2+1 << " ";
      ofp << "(+ ch_" << count1 << "_" << count2 << " ";
      ofp << "rech_amt_" << count1 << "_" << count2 << "))" << endl;

      ofp << "(or" << endl; //change15
      for (count3 = 1; count3 <= workspace.number_of_rechs; count3++)
      {
        placeRecharger1 (ofp, workers, count1, count2, count3,  1,  0);
        placeRecharger1 (ofp, workers, count1, count2, count3,  1,  1);
        placeRecharger1 (ofp, workers, count1, count2, count3,  0,  1);
        placeRecharger1 (ofp, workers, count1, count2, count3, -1,  1);
        placeRecharger1 (ofp, workers, count1, count2, count3, -1,  0);
        placeRecharger1 (ofp, workers, count1, count2, count3, -1, -1);
        placeRecharger1 (ofp, workers, count1, count2, count3,  0, -1);
        placeRecharger1 (ofp, workers, count1, count2, count3,  1, -1);
      } 
      ofp << "))))" << endl << endl;
    }
  }
  ofp << endl;
}


void get_counts_workers (ofstream &ofp, workspace_t workspace, worker_vec_t workers)
{
  unsigned int count1, count2;
  for(count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for(count2=1; count2<workspace.hlen; count2++)
    {
      ofp << "s.add(" << endl;
      ofp << "Implies(wprim_" << count1 << "_" << count2 << "==0, ";
      ofp << "And(waitcount_" << count1 << "_" << count2 << "==1, ";
      ofp << "rechcount_" << count1 << "_" << count2 << "==0)), " << endl;

      ofp << "Implies(wprim_" << count1 << "_" << count2 << "==2, ";
      ofp << "And(waitcount_" << count1 << "_" << count2 << "==1, ";
      ofp << "rechcount_" << count1 << "_" << count2 << "==1)), " << endl;

      ofp << "Implies(wprim_" << count1 << "_" << count2 << "==1, ";
      ofp << "And(waitcount_" << count1 << "_" << count2 << "==0, ";
      ofp << "rechcount_" << count1 << "_" << count2 << "==0)))" << endl;
    }
    ofp << endl;
  }

  /* to minimize total_wait, first get the sum of waits */
  ofp << endl << "# summation of all waits" << endl;
  ofp << "s.add(total_wait==" << endl;
  for(count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for(count2=1; count2<workspace.hlen; count2++)
    {
       ofp << "waitcount_" << count1 << "_" << count2;
       if(count1<workspace.number_of_wrobs || count2<workspace.hlen-1) ofp << " +";
       ofp << endl;
    }
  } 
  ofp << ")" << endl << endl;

  ofp << endl << "# summation of all recharge events" << endl;
  ofp << "s.add(total_rech==" << endl;
  for(count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for(count2=1; count2<workspace.hlen; count2++)
    {
       ofp << "rechcount_" << count1 << "_" << count2;
       if(count1<workspace.number_of_wrobs || count2<workspace.hlen-1) ofp << " +";
       ofp << endl;
    }
  }
  ofp << ")" << endl << endl;

  ofp << "# checking for SAT for a given value of total_wait" << endl;
  //ofp << "s.add(total_wait==50)" << endl << endl;
  //ofp << "print(s.check())" << endl;

  //ofp << "(minimize total_wait)" << endl;
  //ofp << "(check-sat)" << endl;
  //ofp << "(get-objectives)" << endl;

  //ofp << "# optimization : total_wait" << endl;
  //ofp << "opt.minimize(total_wait)" << endl;
  //ofp << "opt.check()" << endl;
}


void writeOutputConstraints_workers (ofstream &ofp, workspace_t workspace, worker_vec_t workers)
{
  unsigned int count1, count2;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
	ofp << "(get-value (wprim_" << count1 << "_" << count2 << ")) " << endl;
    }
    ofp << endl;
  }
 
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    {
	ofp << "(get-value (wtraj_" << count1 << "_" << count2 << ")) " << endl;
    }
    ofp << endl;
  }

  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for (count2=1; count2<=workspace.hlen; count2++)
    {
      ofp << "(get-value (wx_" << count1 << "_" << count2 << "))" << endl;
      ofp << "(get-value (wy_" << count1 << "_" << count2 << "))" << endl;
    }
    ofp << endl;
  }

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2 = 1; count2 <= workspace.hlen; count2++)
    {
        ofp << "(get-value (ch_" << count1 << "_" << count2 << ")) " << endl;
    }
    ofp << endl;
  }

  for(count1=1; count1<=workspace.number_of_wrobs; count1++)
  { 
    for(count2=1; count2<workspace.hlen; count2++)
    {  
       ofp << "(get-value (rechcount_" << count1 << "_" << count2 << "))" << endl;
    }
  }

  for(count1=1; count1<=workspace.number_of_wrobs; count1++)
  { 
    for(count2=1; count2<workspace.hlen; count2++)
    {  
       ofp << "(get-value (waitcount_" << count1 << "_" << count2 << "))" << endl;
    }
  }

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++) //change15
  {
    for (count2 = 1; count2 <= workspace.hlen-1; count2++)
    {
      ofp << "(get-value (rechassigned_" << count1 << "_" << count2 << "))" << endl;
    }
  }
  ofp << "(get-value (total_rech))" << endl;
}


void writeOutputConstraints_workers2 (ofstream &ofp, workspace_t workspace, worker_vec_t workers, workerhalt_vec_t workerhalt, unsigned int max_timept)
{
  unsigned int count1, count2;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
	ofp << "(get-value (wprim_" << count1 << "_" << count2 << ")) " << endl;
    }
    ofp << endl;
  }

  for (count1=1; count1<=workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept; count2++)
    {
      ofp << "(get-value (wx_" << count1 << "_" << count2 << "))" << endl;
      ofp << "(get-value (wy_" << count1 << "_" << count2 << "))" << endl;
    }
    ofp << endl;
  }

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept; count2++)
    {
        ofp << "(get-value (ch_" << count1 << "_" << count2 << ")) " << endl;
    }
    ofp << endl;
  }

  for(count1=1; count1<=workspace.number_of_wrobs; count1++)
  { 
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {  
       ofp << "(get-value (rechcount_" << count1 << "_" << count2 << "))" << endl;
    }
  }

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++) //change15
  {
    for (count2=workerhalt[count1-1].timept; count2<=max_timept-1; count2++)
    {
      ofp << "(get-value (rechassigned_" << count1 << "_" << count2 << "))" << endl;
    }
  }

  ofp << "(get-value (total_wait))" << endl;
}
