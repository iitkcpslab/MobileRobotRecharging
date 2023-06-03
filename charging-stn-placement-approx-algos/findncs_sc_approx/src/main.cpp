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

  cout << endl << "===== GREEDY SC HEURISTICS FOR VC =====" << endl;
  cout << "Reading inputs ..." << endl;
  readPrimitives (primitives);
  readObstacles (obstacles);
  readWorkspace (workspace, obstacles);

  pos_vec_t obsfree = getFreeLocations (workspace, obstacles);
  set<int> velset = getVelocityDistinct (primitives);
  workspace.boundary = findBoundaryPoints(workspace, obstacles); 

  // creation of graph
  createNodesForObsFreeLocations (velset, obsfree, graph); // create nodes
  createLists (graph, primitives, obstacles, workspace); // adjacency list creation

  node_t** adj = graph.adj;
  unordered_map <string, unsigned int> umap = graph.umap;

  findBoundaryNodes_graph(graph, workspace);
  cout << endl << "Processing, please wait ..." << endl;
  greedyHeur_VC(graph, workspace);

  return 0;
}

