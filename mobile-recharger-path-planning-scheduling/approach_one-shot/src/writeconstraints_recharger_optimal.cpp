#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include "primitive.h"
#include "readinputs.h"
#include "writeconstraints_recharger.h"
#include "writeconstraints_recharger_optimal.h"

void declareVariables2 (ofstream &ofp, workspace_t workspace, unsigned int max_timept)
{
  unsigned int count1, count2;

  ofp << "(declare-fun obstacle (Int Int) Bool)" << endl;
  ofp << "(define-fun bool_to_int ((b Bool)) Int" << endl;
  ofp << "  (ite b 1 0)" << endl << ")" ;
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept-1; count2++)
    { 
      ofp << "(declare-const rprim_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept-1; count2++)
    {
      ofp << "(declare-const rcost_" << count1 << "_" << count2 << " Real)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept-1; count2++)
    {
      ofp << "(declare-const rx_f_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept-1; count2++)
    {
      ofp << "(declare-const ry_f_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    { 
      ofp << "(declare-const rx_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    { 
      ofp << "(declare-const ry_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++) //change15
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    {
      ofp << "(declare-const rechassigned_" << count1 << "_" << count2 << " Int)" << endl;
    }
  }
  ofp << endl;

  ofp << "(declare-const total_rcost" << " Int)" << endl << endl;
}


bool isObstacle (pos_vec_t obstacles, position pos)
{
  pos_vec_t::iterator beg = obstacles.begin();
  for (; beg!=obstacles.end(); beg++)
  {
    if((*beg).x==pos.x && (*beg).y==pos.y)
    {
      return true;
    }
  }
  return false;
}


void placeRecharger2 (ofstream &ofp, worker_vec_t workers, pos_vec_t obstacles, unsigned int w_id, unsigned int timept, unsigned int r_id, int ofs_x, int ofs_y, unsigned int duratn)
{
  position pos;
  pos.x = workers[w_id].wpos_start.x + ofs_x;
  pos.y = workers[w_id].wpos_start.y + ofs_y; 

  if (!isObstacle (obstacles, pos))
  {
    ofp << "   (and ";
    for(unsigned int count = 0; count < duratn; count++)
    {
     ofp << "(= rx_" << r_id << "_" << timept+count << " " << pos.x << ") ";
     ofp << "(= ry_" << r_id << "_" << timept+count << " " << pos.y << ") ";
     if (count!=duratn-1)
     {
     //  ofp << "(= rechcount_" << w_id+1 << "_" << timept+count << " 1) ";
       ofp << "(= rechassigned_" << w_id+1 << "_" << timept+count << " " << r_id << ")";
     }
    }
    ofp << ")" << endl;
  }
}


void writeWaypointsConstraints2 (ofstream &ofp, workspace_t workspace, pos_vec_t obstacles, worker_vec_t workers, rechinst_vec_t rechinstances, workerhalt_vec_t workerhalt, unsigned int max_timept)
{
  rechinst_t a;
  workerhalt_t b;
  unsigned int count1, count2, count3;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    b = workerhalt[count1-1];
    /* b.duration should be one more because for recharging one more time pt is needed */
    for (count2 = b.timept; count2 <= max_timept-b.duration; count2++)
    {
      ofp << "(declare-const lastrech_" << count1 << "_" << count2 << " Bool)" << endl;
    }
  }

  /* intermediate recharging points DERIVED FROM SHOT-1 */
  ofp << endl << "; intermediate recharging" << endl;
  for (count1 = 0; count1 < rechinstances.size(); count1++)
  {
    a = rechinstances[count1];
    ofp << "(assert (and "; 
    ofp << "(= rx_" << a.rech_id << "_" << a.timept << " " << a.trajpt.x << ") ";
    ofp << "(= ry_" << a.rech_id << "_" << a.timept << " " << a.trajpt.y << ") ";
    // recharger's next position also is same as the previous
    ofp << "(= rx_" << a.rech_id << "_" << a.timept+1 << " " << a.trajpt.x << ") ";
    ofp << "(= ry_" << a.rech_id << "_" << a.timept+1 << " " << a.trajpt.y << ")";
    ofp << "(= rechassigned_" << a.worker_id << "_" << a.timept << " " << a.rech_id << ")))" << endl;
  }

  unsigned int duratn;
  /* last recharging of static workers, placing a recharger appropriately */
  ofp << "; last recharging" << endl;
  for (count1 = 0; count1 < workspace.number_of_wrobs; count1++)
  {
    b = workerhalt[count1];
    duratn = b.duration+1; // because worker and recharger has to be placed one more time point
    ofp << ";===============================================" << endl;
    for (count2 = b.timept; count2 <= max_timept-duratn+1; count2++)
    {
      ofp << "(assert" << endl;
      ofp << " (=> (= lastrech_" << count1+1 << "_" << count2 << " true)" << endl;
      ofp << "  (or" << endl;
      for (count3 = 1; count3 <= workspace.number_of_rechs; count3++)
      {
        placeRecharger2 (ofp, workers, obstacles, count1, count2, count3,  1,  0, duratn);
        placeRecharger2 (ofp, workers, obstacles, count1, count2, count3,  1,  1, duratn);
        placeRecharger2 (ofp, workers, obstacles, count1, count2, count3,  0,  1, duratn);
        placeRecharger2 (ofp, workers, obstacles, count1, count2, count3, -1,  1, duratn);
        placeRecharger2 (ofp, workers, obstacles, count1, count2, count3, -1,  0, duratn);
        placeRecharger2 (ofp, workers, obstacles, count1, count2, count3, -1, -1, duratn);
        placeRecharger2 (ofp, workers, obstacles, count1, count2, count3,  0, -1, duratn);
        placeRecharger2 (ofp, workers, obstacles, count1, count2, count3,  1, -1, duratn);
      }
      ofp << "  )  " << endl;
      ofp << " )" << endl;
      ofp << ")" << endl << endl;
    }
  }

  ofp << "; ensure last recharging of the halted workers" << endl;
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    b = workerhalt[count1-1];
    ofp << "(assert (= 1 (+" << endl; 
    //for (count2 = b.timept; count2 <= max_timept-b.duration+1; count2++)
    for (count2 = b.timept; count2 <= max_timept-duratn+1; count2++)
    {
      ofp << " (bool_to_int lastrech_" << count1 << "_" << count2 << ")" << endl;
    }
    ofp << ")))" << endl << endl;  
  }

  ofp << "; matching recharger's last position with initial one" << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    ofp << "(assert (and (= rx_" << count1 << "_" << max_timept << " rx_" << count1 << "_1) (= ry_" << count1 << "_" << max_timept << " ry_" << count1 << "_1)))" << endl;
  }
}


void writeTransitionConstraints2 (ofstream &ofp, prim_vec_t primitives, pos_vec_t obstacles, workspace_t workspace, unsigned int max_timept)
{
  state q_i, q_f;
  position pos_f;
  pos_vec_t swath, swath1, swath2;
  string cost;
  unsigned int count, count1, count2, count3;

  bool workspace_obstacles[workspace.length_x + 1][workspace.length_y + 1];

  for (count1 = 0; count1 <= workspace.length_x; count1++)
  {
    for (count2 = 0; count2 <= workspace.length_y; count2++)
    { 
      workspace_obstacles[count1][count2] = false;
    }
  }

  for (count = 0; count < obstacles.size(); count++)
  {
    workspace_obstacles[obstacles[count].x][obstacles[count].y] = true;
  }
  ofp << endl;
  
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept-1; count2++)
    {
      ofp << "(assert (and (>= rprim_" << count1 << "_" << count2 << " 1) (<= rprim_" << count1 << "_" << count2 << " " << primitives.size() << ")))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    { 
      ofp << "(assert (and (>= rx_" << count1 << "_" << count2 << " " << workspace.min_x << ") (<= rx_" << count1 << "_" << count2 << " " << workspace.length_x << ")))" << endl;
    }
  } 
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    { 
      ofp << "(assert (and (>= ry_" << count1 << "_" << count2 << " " << workspace.min_y << ") (<= ry_" << count1 << "_" << count2 << " " << workspace.length_y << ")))" << endl;
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++) //change15
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    {
      ofp << "(assert (or" << endl;
      for (count3 = 1; count3 <= workspace.number_of_rechs; count3++)
      {
        ofp << "  (= rechassigned_" << count1 << "_" << count2 << " " << count3 << ") ";
      }
      ofp << "))" << endl;
    }
  }
      
/*
  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++) //change15
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    { 
      ofp << "(assert (xor" << endl;
      for (count3 = 1; count3 <= workspace.number_of_rechs; count3++)
      {
        ofp << "(= rechassigned_" << count1 << "_" << count2 << " " << count3 << ") ";
      }
      ofp << "))" << endl;
    }
  }
  ofp << endl;
*/
  for (count1 = 0; count1 <= workspace.length_x; count1++)
  {
    for (count2 = 0; count2 <= workspace.length_y; count2++)
    {
      if (workspace_obstacles[count1][count2] == 0) 
        ofp << "(assert (= (obstacle " << count1 << " " << count2 << ") " << "false" << "))" << endl;
      else
        ofp << "(assert (! (= (obstacle " << count1 << " " << count2 << ") " << "true" << ") :named obs_" << count1 << "_" << count2 << "))" << endl;
    }
  }
  ofp << endl;

  ofp << "; transition of recharger(s)" << endl;
  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept-1; count2++)
    {
      for (count = 0; count < primitives.size(); count++)
      {
        q_i = primitives[count].get_q_i();
        q_f = primitives[count].get_q_f();
        pos_f = primitives[count].get_pos_f();
        cost = primitives[count].get_cost();
        swath = primitives[count].get_swath();
        ofp << "(assert (or (not (= rprim_" << count1 << "_" << count2 << " " << count + 1 << "))" << endl;
        ofp << "  (and   (= rx_f_" << count1 << "_" << count2 << " " << pos_f.x << ")" << endl;
        ofp << "     (= ry_f_" << count1 << "_" << count2 << " " << pos_f.y << ")" << endl;
        ofp << "     (= rcost_" << count1 << "_" << count2 << " " << floatToReal(cost) << ")" << endl;
        for (count3 = 0; count3 < swath.size(); count3++)
        {
          ofp << "     (= (obstacle (+ rx_" << count1 << "_" << count2 << " " << swath[count3].x << ") (+ ry_" << count1 << "_" << count2 << " " << swath[count3].y << ")) false)" << endl;
        }
        ofp << ")))" << endl;
        ofp << endl;
      }
    }
  }
  ofp << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 < max_timept; count2++)
    {
      ofp << "(assert (= rx_" << count1 << "_" << count2 + 1 << " (+ rx_" << count1 << "_" << count2 << " rx_f_" << count1 << "_" << count2 << ")))" << endl;
      ofp << "(assert (= ry_" << count1 << "_" << count2 + 1 << " (+ ry_" << count1 << "_" << count2 << " ry_f_" << count1 << "_" << count2 << ")))" << endl;
    }
  }
  ofp << endl;
}


void writeCollisionAvoidanceConstraints2 (ofstream &ofp, workspace_t workspace, worker_vec_t workers, unsigned int ext_hlen)
{
  unsigned int count, count1, count2, count3, orig_hlen=workspace.hlen;
  worker_t wk;
  pos_vec_t wktr;

  ofp << endl << "; collision avoidance - 1st phase - between rechargers and workers" << endl;
  for (count = 1; count <= workspace.number_of_rechs; count++)
  {
    for (count1 = 1; count1 <= orig_hlen; count1++)
    {
     for (count2 = 0; count2 < workers.size(); count2++)
     {
       wk = workers[count2];
       wktr = wk.workingtraj;
       ofp << "(assert (not (and (= rx_" << count << "_" << count1 << " " << wktr[count1-1].x << ") ";
       ofp << "(= ry_" << count << "_" << count1 << " " << wktr[count1-1].y << "))))" << endl;
     }
    }
  }
  ofp << endl;
  
  ofp << "; collision avoidance - 2nd phase - between rechargers and static workers" << endl;
  for (count = 1; count <= workspace.number_of_rechs; count++)
  {
    for (count1 = orig_hlen+1; count1 <= ext_hlen; count1++)
    {
      for (count2 = 0; count2 < workers.size(); count2++)
      {
        wk = workers[count2];
        ofp << "(assert (not (and (= rx_" << count << "_" << count1 << " " << wk.workingtraj[orig_hlen-1].x << ") ";
        ofp << "(= ry_" << count << "_" << count1 << " " << wk.workingtraj[orig_hlen-1].y << "))))" << endl;
      }
    }
  }
  ofp << endl;

  ofp << "; collision avoidance - 1st & 2nd phase - among rechargers" << endl;
  for (count1 = 1; count1 <= ext_hlen; count1++)
  {
    for (count2 = 1; count2 <= workspace.number_of_rechs; count2++)
    {
      for (count3 = count2+1; count3 <= workspace.number_of_rechs; count3++)
      {
       ofp << "(assert (not (and (= rx_" << count2 << "_" << count1 << " " << "rx_" << count3 << "_" << count1 << ") ";
       ofp << "(= ry_" << count2 << "_" << count1 << " " << "ry_" << count3 << "_" << count1 << "))))" << endl;
      }
    }
  }
  ofp << endl;
}


void minimize_rcost (ofstream &ofp, unsigned int max_timept, unsigned int ext_hyp_start, unsigned int nrecharger)
{
  
  if (max_timept > ext_hyp_start) // primitives are always applied upto one less than max_timept
  {
    ofp << "; total_rcost" << endl;
    ofp << "(assert (= total_rcost (+ " << endl;
    for (unsigned int count1 = 1; count1 <= nrecharger; count1++)
    {
      for(unsigned int count2 = ext_hyp_start; count2 <= max_timept-1; count2++)
      {   
        ofp << "rcost_" << count1 << "_" << count2 << endl;
      }
    }
    ofp << endl;
    ofp << ")))" << endl << endl;
  }
  ofp << "(minimize (total_rcost))" << endl;
}


void writeOutputConstraints2 (ofstream &ofp, unsigned int max_timept, workspace_t workspace, workerhalt_vec_t workerhalt, unsigned int flag)
{
  unsigned int count1, count2;

  ofp << "(check-sat)" << endl;

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 0; count2 < max_timept-1; count2++)
    {
      ofp << "(get-value (rprim_" << count1 << "_" << count2 + 1 << "))" << endl;
    }
  }

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 0; count2 < max_timept-1; count2++)
    {
      ofp << "(get-value (rcost_" << count1 << "_" << count2 + 1 << "))" << endl;
    }
  }

  for (count1 = 1; count1 <= workspace.number_of_rechs; count1++)
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    {
      ofp << "(get-value (rx_" << count1 << "_" << count2 << "))" << endl;
      ofp << "(get-value (ry_" << count1 << "_" << count2 << "))" << endl;
    }
  }

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++) //change15
  {
    for (count2 = 1; count2 <= max_timept; count2++)
    {
      ofp << "(get-value (rechassigned_" << count1 << "_" << count2 << "))" << endl;
    }
  }

  ofp << "(get-value (total_rcost))" << endl;

  for (count1 = 1; count1 <= workspace.number_of_wrobs; count1++)
  {
    workerhalt_t b = workerhalt[count1-1];
    //for (count2 = b.timept; count2 <= max_timept-b.duration+1; count2++)
    for (count2 = b.timept; count2 <= max_timept-b.duration; count2++) // as an extra stationary time pt needed
    {
      ofp << "(get-value (lastrech_" << count1 << "_" << count2 << "))" << endl;
    }
  }
}
