#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>
#include "primitive.h"
#include "readinputs.h"
#include "create_graph.h"
using namespace std;

int main ()
{
  prim_vec_t primitives;
  pos_vec_t obstacles;
  workspace_t workspace;
  graph_t graph;

  cout << endl << "====== DOMSET BASED APPROXIMATION ALGORITHM ======" << endl;
  cout << "Reading inputs ..." << endl;
  readPrimitives (primitives);
  readObstacles (obstacles);
  readWorkspace (workspace, obstacles);

  pos_vec_t obsfree = getFreeLocations (workspace, obstacles);
  set<int> velset = getVelocityDistinct (primitives);
  

  // create graph
  createNodesForObsFreeLocations (velset, obsfree, graph);
  createAdjMatrix (graph, primitives, obstacles, workspace);

  workspace.boundary = findBoundaryPoints(workspace, obstacles);
  getBoundaryNodes (graph, workspace);

  cout << endl;
  cout << "total nodes = " << graph.count_graph_nodes << endl;
  cout << endl << "Processing, please wait ..." << endl;
  greedyHeur_adjmat (graph);

  return 0;
}

