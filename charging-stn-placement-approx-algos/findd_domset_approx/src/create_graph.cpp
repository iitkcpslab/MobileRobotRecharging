#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <set>
#include <unordered_map>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>
#include "primitive.h"
#include "readinputs.h"
#include "create_graph.h"

using namespace std;

typedef pair<unsigned int, unsigned int> pair_t;


// set union
set<unsigned int> set_union(set<unsigned int> a, set<unsigned int> b)
{
  set<unsigned int> c = a;
  c.insert(b.begin(), b.end());
  return c;
}


// set difference
set<unsigned int> set_minus(set<unsigned int> a, set<unsigned int> b)
{
  set<unsigned int> c;
  set_difference(a.begin(), a.end(), b.begin(), b.end(), inserter(c, c.end()));
  return c;
}


// print a set
void print_set (graph_t graph, set<unsigned int> c)
{
  set<unsigned int>::iterator it = c.begin();
  for(; it!=c.end(); it++)
    cout << *it << " ";

  cout << endl << endl;
  it = c.begin();
  for(; it!=c.end(); it++)
    cout << graph.nodes[*it]->nid << ",";

  return;
}

// print a set
void print_set (set<unsigned int> c)
{
  set<unsigned int>::iterator it = c.begin();
  for(; it!=c.end(); it++)
    cout << *it << " ";

  cout << endl;
  return;
}


// print node info
void printNode (graph_t graph, int nindex)
{
  cout << "nindex:" << nindex << " ";
  cout << "(" << graph.nodes[nindex]->pos.x << " ";
  cout << graph.nodes[nindex]->pos.y << ");";
  cout << graph.nodes[nindex]->vel << " ";
  cout << "outdegree=" << graph.nodes[nindex]->outdeg << " ";
  cout << "visited=" << graph.nodes[nindex]->visited << endl;
  return;
}


// print incident nodes of a given node.
void printIncidentNodes (graph_t graph, int nindex)
{
  cout << "incidence details for node: " << nindex << endl;
  //printNode (graph, nindex);
  for (unsigned int j=0; j<graph.count_graph_nodes; j++)
  {
    if(graph.adjmat[nindex][j]==1)
    {
	    printNode(graph, j);
    }
  }
  cout << endl;
  return;
}


// initialize graph.boundary with the boundary nodes
void getBoundaryNodes (graph_t& graph, workspace_t workspace)
{
   int x,y;
   ostringstream oss;
   int precision = 2;
   unsigned int node;

   cout << "graph.count_vel "  << graph.count_vel << endl;
   for(unsigned int i=0; i<workspace.boundary.size(); i++)
   {
      x = workspace.boundary[i].x; 
      y = workspace.boundary[i].y;
      for(unsigned int vel=0; vel<graph.count_vel; vel++)
      {
        // get the node index of a boundary vertex
        oss << setw(precision) << setfill('0') << x << setw(precision) << y << setw(precision) << vel;
        node = graph.umap[oss.str()]; // get node index
        graph.boundary.push_back(node);
	oss.str("");
      }
   }
   return;
}


void printBoundaryNodes (vector<unsigned int> s)
{
	cout << "the boundary nodes are " << endl;
	for(auto it=s.begin(); it!=s.end(); it++) cout << *it << ' ';
}


// checks if a position is an obstacle. returns true if pos is an obstacle
bool isObstacle (position pos, pos_vec_t obstacles)
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


// checks if a move from a source node, on applying a primitive, ends up in an obstacle-free location or goes out of the boundary (i.e., valid move). Returns true if a valid move.
// calls isObstacle (pos, obstacles)
bool isValidMove (position src, pos_vec_t swath, pos_vec_t obstacles, workspace_t ws)
{
  bool is_valid = true;
  for (unsigned int i=0; i<swath.size(); i++)
  {
    position pos;
    pos.x = src.x + swath[i].x;
    pos.y = src.y + swath[i].y;

    if (pos.x < 0 || pos.y < 0 || pos.x > ws.length_x || pos.y > ws.length_y)
      {is_valid = false; break;}
    is_valid = is_valid & (!isObstacle (pos, obstacles));
  }
  return is_valid;
}


// generates nid (unique) of a node. returns the nid. assuming, each of x,y,vel has a precision of 2.
string getNid (position pos, int vel)
{
  ostringstream oss;
  int precision = 2;
  oss << setw(precision) << setfill('0') << pos.x << setw(precision) << pos.y << setw(precision) << vel;

  return oss.str();
}


// creates a new node with information like nid (unique), position, velocity. nid is same as the index value in the adj list. returns pointer to the node.
node_t* createNode (position pos, int vel)
{
  node_t* temp;
  temp = new node_t();
  temp->nid = getNid (pos, vel);
  temp->pos = pos; 
  temp->vel = vel;
  temp->outdeg = 0; // new for adjmat
  temp->visited = false;
  return temp;
}


// creates an adjacency matrix with the created nodes
// a cell contains 1 if primitive condition matches; else 0.
void createAdjMatrix (graph_t& graph, prim_vec_t prims, pos_vec_t obstacles, workspace_t workspace)
{
  unsigned int ncount=graph.count_graph_nodes;
  unsigned int nrows, ncols, r, c;
  nrows = ncols = ncount;

  // create adj matrix
  graph.adjmat = (int**) malloc(sizeof(int*) * nrows); // rows
  for(unsigned int i=0; i<nrows; i++) // for all rows
    graph.adjmat[i] = (int*)malloc(sizeof(int) * ncols); // cols
 
  // initialize adj matrix
  for(unsigned int i=0; i<nrows; i++)
    for(unsigned int j=0; j<ncols; j++)
      graph.adjmat[i][j]=0;

  string sstr, dstr;
  // populate the adj matrix with incidence with path length 1
  for(unsigned int i=0; i<ncount; i++) // for all nodes
  {
    // source node info
    position spos = graph.nodes[i]->pos;
    int svel = graph.nodes[i]->vel;
    int sdeg = 0; // to be modified as per adjacency

    sstr = getNid(spos, svel); 
    r = graph.umap[sstr];

    graph.adjmat[r][r] = 1; sdeg++;
    for(unsigned int j=0; j<prims.size(); j++) // for i^th node
    {
      // capturing properties of a primitive
      state q_i = prims[j].get_q_i();
      state q_f = prims[j].get_q_f();
      position offset = prims[j].get_pos_f();
      pos_vec_t swath = prims[j].get_swath();

      if (svel==q_i.velocity) // if init vel of head node matches q_i
      {// are all the nodes covered ?
        if (isValidMove (spos, swath, obstacles, workspace))
        {
          position dpos;
          dpos.x = spos.x + offset.x;
          dpos.y = spos.y + offset.y;
	  dstr = getNid(dpos, q_f.velocity); 
	  c = graph.umap[dstr];

	  graph.adjmat[r][c] = 1;
	  sdeg++;
        }
      }
    }
    graph.nodes[i]->outdeg = sdeg;
  }
  graph.ncs = workspace.ncs;
  cout << "adjacency matrix created ..." << endl;
  return;
}


// creates list(array) of nodes. changes attributes of the graph.
// calls createNode (pos, vel)
void createNodesForObsFreeLocations (set<int> velset, pos_vec_t obsfree, graph_t& graph)
{
  node_t** nodes;
  position pos;
  int vel;
  unsigned int nodecount=0, velcount=0;

  set<int>::iterator it = velset.begin();
  for ( ; it!=velset.end(); it++)
    velcount++;

  graph.count_vel = velcount;
  graph.count_graph_nodes = nodecount = obsfree.size()*velcount;
  nodes = (node_t**) malloc(sizeof(node_t*) * nodecount);

  nodecount=0;

  /* creating nodes */
  // for each obsfree location
  for (unsigned int i=0; i<obsfree.size(); i++)
  {
    pos.x = obsfree[i].x; pos.y = obsfree[i].y; 

    // for each velocity
    for (it = velset.begin(); it!=velset.end(); it++)
    {
      vel = *it;
      node_t* temp = createNode (pos, vel); // unique 'nid' for all
      nodes[nodecount] = temp; // nodecount --> node
      graph.umap[temp->nid] = nodecount; // nid --> nodecount
      nodecount++;
    }
  }
  graph.nodes = nodes;
  cout << "Graph nodes created ..." << endl;

  // set of uncovered nodes. set of covered nodes is empty.
  for(unsigned int i=0; i<graph.count_graph_nodes; i++) graph.notcovrd.insert(i);
  cout << "Uncovered and covered nodes are initialized ..." << endl;
  return;
}


// initializes 2d matrix arr with all elements assigned elt value
void initializeMatrix (int** arr, int nrows, int ncols, int elt)
{
  for(unsigned int i=0; i<nrows; i++)
  {
    arr[i] = (int*)malloc(sizeof(int) * ncols);
    for(unsigned int j=0; j<ncols; j++)
    {
      arr[i][j] = elt;
    }
  }
  return;
}


// multiplies two matrices a and b and stores in mat. returns mat with nclos1 and nrows2.
int** multiplyMatrices (int** a, int** b, int nrows1, int ncols1, int nrows2, int ncols2)
{
  if(ncols1 != nrows2){cout << "Incompatible for matrix multiplication" << endl; exit(0);}

  int** mat = (int**)malloc(sizeof(int*) * nrows1);
  initializeMatrix (mat, nrows1, ncols2, 0);

  for(unsigned int i=0; i<nrows1; i++)
  {
    for(unsigned int j=0; j<ncols2; j++)
    {
       for(unsigned int k=0; k<ncols1; k++)
       {
          mat[i][j] += a[i][k] * b[k][j];
       }
    }
  }
  return mat;
}


// copies a matrix a into matrix b
void copyMatrix (int** a, int**b, int nrows, int ncols)
{
  for(unsigned int i=0; i<nrows; i++)
  {
    for(unsigned int j=0; j<ncols; j++)
    {
      b[i][j]=a[i][j];
    }
  }
  return;
}


// creates a matrix named 'a' with nrows and ncols, returns 'a'
int** createMatrix (int nrows, int ncols)
{
  int** a = (int**) malloc(sizeof(int*) * nrows); // rows
  for(unsigned int i=0; i<nrows; i++) // for all rows
     a[i] = (int*)malloc(sizeof(int) * ncols); // cols

  for(unsigned int i=0; i<nrows; i++)
  {
    for(unsigned int j=0; j<ncols; j++)
    {
      a[i][j]=0;
    }
  }
  return a;
}


// normalizes a matrix named "arr". replaces any non-zero element with 1
void normalizeMatrix (int** arr, int nrows, int ncols)
{
   for(unsigned int i=0; i<nrows; i++)
   {
      for(unsigned int j=0; j<ncols; j++)
      {
	  if(arr[i][j]>0) arr[i][j]=1;
      }
   }
}


// NEW FUNCTION -----------------------------------------------------
// covers all the nodes associated to a single location and different velocities
void getCoverageForAllVels (graph_t& graph, unsigned int v, set<unsigned int>& covered, unsigned int precision)
{
  string nid = graph.nodes[v]->nid;
  string subst = nid.substr(0, 2*precision); // get the location only

  ostringstream oss;
  for(unsigned int i=0; i<graph.count_vel; i++) // velocities
  {
    oss << subst << setw(precision) << setfill('0') << i;
    covered.insert(graph.umap[oss.str()]);
    oss.str("");
  }
  return;
}


// get the node index with maximum cover
set<unsigned int> getCoverForD (graph_t& graph, int** temp, int nrows, int ncols)
{
   int max_cov=0, max_ind=-1;
   set<unsigned int> covset[nrows];
   int* ncovs;
   bool* is_visited;
   set<unsigned int> covrd, notcovrd, cover, intersect;

   ncovs = (int*)malloc(sizeof(int) * nrows);
   is_visited = (bool*)malloc(sizeof(bool) * nrows);

   // initialization
   covrd = graph.covrd; 
   notcovrd = graph.notcovrd;
   for(unsigned int i=0; i<graph.count_graph_nodes; i++) 
   {
      ncovs[i] = 0; 
      is_visited[i] = false;
   }

   while(notcovrd.size()>0)
   {
     cout << "not covered size = " << notcovrd.size();

     // find covered node for all boundary nodes. then, find the max.
     for(unsigned int i=0; i<graph.count_graph_nodes; i++)
     //for(unsigned int i=0; i<graph.boundary.size(); i++)
     {
        unsigned int node;
	//node = graph.boundary[i];
	node = i;
	
        // stores into covset[node] the covered nodes by 'node'
        for(unsigned int j=0; j<ncols; j++)
        {
	   if(temp[node][j]==1 && is_visited[j]==false)    
	   {	 
      	      getCoverageForAllVels(graph, j, covset[node], 2);
	   }
        }


        // compute intersection with uncovered and covered nodes 
        intersect=set_minus(notcovrd, set_minus(notcovrd, covset[node])); 
        ncovs[node] = intersect.size();

	auto it = covrd.find(node);
        // find maximum covered node
        if(it==covrd.end() && ncovs[node] > max_cov)
        {
           max_ind = node; 
           max_cov = ncovs[node];
        }
     }
     // update global sets, covrd and notcovrd, with the maxcov node
     covrd = set_union (covrd, covset[max_ind]);
     notcovrd = set_minus (notcovrd, covset[max_ind]);
     cover.insert(max_ind);
     cout << "  inserted : " << max_ind << " nelements=" << max_cov << endl;;

     for(auto it=covset[max_ind].begin(); it!=covset[max_ind].end(); it++)
        is_visited[*it] = true;

     for(unsigned int k=0; k<graph.count_graph_nodes; k++)
        covset[k].erase(covset[k].begin(), covset[k].end());

     max_cov=0, max_ind=-1;
   }
   cout << endl << endl;
   return cover;
}


// approximate vertex cover
void greedyHeur_adjmat (graph_t graph)
{
   int nrows, ncols, d;
   int* ncovs;
   bool* is_visited;
   set<unsigned int> cover;

   nrows = ncols = graph.count_graph_nodes;
   int** arr = createMatrix (nrows, ncols); // arr will be used for computation
   copyMatrix (graph.adjmat, arr, nrows, ncols); // initialize arr with graph.adjmat
   int** temp = createMatrix (nrows, ncols);
   int** temp1 = createMatrix (nrows, ncols);
   
   cout << endl << "starting computation ..." << endl << endl;
   for(d=2; d<graph.count_graph_nodes; d++) // d-value
   {
      cout << "Finding ncs for d=" << d << endl;
      arr = multiplyMatrices (arr, graph.adjmat, nrows, ncols, nrows, ncols); // arr=arr*adjmat
      normalizeMatrix (arr, nrows, ncols); // put 1 for any non-zero element

      copyMatrix (arr, temp, nrows, ncols); // temp <- arr

      temp = multiplyMatrices (temp, temp, nrows, ncols, nrows, ncols); // temp=temp*temp
      normalizeMatrix (temp, nrows, ncols); // put 1 for any non-zero element
      
      cover = getCoverForD (graph, temp, nrows, ncols);
      cout << "for d=" << d << " cover size is=" << cover.size() << endl;

      if(cover.size()<=graph.ncs) break;
      cout << "--------------------------" << endl;
   }
   cout << endl << "for ncs=" << graph.ncs << " ... THE FINAL d-VALUE IS = " << d << endl << endl;

   //cout << "Printing the Cover : " << graph.cover.size() << endl;
   cout << endl << "Cover = {"; print_set (graph, cover); cout << "}" << endl << endl;
   return;
}
