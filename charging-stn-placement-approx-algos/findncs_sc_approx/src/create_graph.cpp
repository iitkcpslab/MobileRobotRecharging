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

typedef pair<unsigned int, unsigned int> pairs;

// prints the headers.
void printHeaders (graph_t graph)
{
  for (unsigned int i=0; i<graph.count_graph_nodes; i++)
  {
    cout << graph.adj[i]->nid << " " << graph.adj[i]->pos.x << " " << graph.adj[i]->pos.y << "; " << graph.adj[i]->vel << endl;
  }
}


// prints the nodes of a given list.
void printList (node_t* head)
{
  node_t* temp = head;

  cout << "Printing the list:" << endl;
  while (temp!=NULL)
  {
    cout << temp->nid << ";" << temp->pos.x << "_" << temp->pos.y << ";" << temp->vel << " -> ";
    temp = temp->next;
  }
  cout << "NULL" << endl;
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


// checks if a move from a source node, on applying a primitive, ends up in an obstacle-free location (i.e., valid move). Returns true if a valid move.
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
string generateNid (position pos, unsigned int vel)
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
  temp->nid = generateNid (pos, vel);
  temp->pos = pos; 
  temp->vel = vel; temp->next = NULL;

  return temp;
}


// inserts a new node in the second position in a given list
// calls createNode (pos, q_f.velocity)
void insertNodeAtSecondPosition (node_t* head, position pos, state q_f)
{
  if(head==NULL) return;

  node_t* temp = createNode (pos, q_f.velocity);
  temp->next = head->next;
  head->next = temp;
}


// inserts new nodes in individual lists.
// calls isValidMove (source, swath, obstacles) and insertNodeAtSecondPosition (adj[i], pos, q_f)
void createLists (graph_t& graph, prim_vec_t prims, pos_vec_t obstacles, workspace_t workspace)
{
  node_t** adj=graph.adj;
  unsigned int count_lists = graph.count_graph_nodes;

  int flag=0;
  // for all lists
  for (unsigned int i=0; i<count_lists; i++)
  {
    position source = adj[i]->pos;
    int head_vel = adj[i]->vel;

    // for a single list
    for (unsigned int j=0; j<prims.size(); j++)
    {
      // capturing properties of a primitive
      state q_i = prims[j].get_q_i();
      state q_f = prims[j].get_q_f();
      position offset = prims[j].get_pos_f();
      pos_vec_t swath = prims[j].get_swath();

      if (head_vel==q_i.velocity) // if init vel of head node matches q_i
      {
        if (isValidMove (source, swath, obstacles, workspace))
        {
          position pos;
          pos.x = source.x + offset.x;
          pos.y = source.y + offset.y;
          insertNodeAtSecondPosition (adj[i], pos, q_f);
          flag=1;
        }
      }
    }
    if(flag==0) graph.adj[i]->visited=true; // change v3
  }
}


// creates list(array) of header nodes. changes attributes of the graph.
// calls createNode (pos, vel)
void createNodesForObsFreeLocations (set<int> velset, pos_vec_t obsfree, graph_t& graph)
{
  node_t** adj;
  position pos;
  int vel;
  unsigned int listcount=0, velcount=0;

  set<int>::iterator it = velset.begin();
  for ( ; it!=velset.end(); it++)
    velcount++;

  graph.count_vel = velcount;
  graph.count_graph_nodes = listcount = obsfree.size()*velcount;
  adj = (node_t**) malloc(sizeof(node_t*) * listcount);

  listcount=0;
  // for each obsfree location
  for (unsigned int i=0; i<obsfree.size(); i++)
  {
    pos.x = obsfree[i].x; pos.y = obsfree[i].y;   
    // for each velocity
    it = velset.begin();
    for ( ; it!=velset.end(); it++)
    {
      vel = *it;
      node_t* temp = createNode (pos, vel); // unique 'nid' for all
      adj[listcount] = temp;
      graph.umap[temp->nid] = listcount;
      listcount++;
    }
  }
  graph.adj = adj;
}


//======Set related======


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


// printing a set
void print_set(set<unsigned int> myset)
{
        // using begin() to print set
        for (auto it = myset.begin(); it != myset.end(); ++it)
	{
                cout << *it << ",";
	}
	cout << endl;
        return;
}


// print covered node set size by each node
void printCoverableSizes (graph_t graph)
{
   for(unsigned int i=0; i<graph.count_graph_nodes; i++)
   {
      cout << (graph.adj[i]->coverable).size() << " ";
   }
   return;
}


// isolated nodes are set as covered beforehand,
// as they wont be visited. initialization.
unsigned int processIsolatedNodes (graph_t& graph)
{
   unsigned int count=0;
   for(unsigned int i=0; i<graph.count_graph_nodes; i++)
   {
     // 'coverable' set must be null or the same element is present
     if((graph.adj[i]->coverable).size()<=1)
     {
             graph.adj[i]->coverable.clear(); // making it empty
	     count++;
     }
   }
   return count;
}


// covers all the nodes associated to a single location and different velocities
void getCoverageForAllVels (graph_t& graph, unsigned int v, set<unsigned int>& covered, unsigned int precision)
{
  string nid = graph.adj[v]->nid;
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


// DFT from a given node v and within a given bound. initialize.
void DFSUtil(graph_t& graph, unsigned int v, unsigned int bound, set<unsigned int>& covered)
{
    // when bnd exceeds bound then it comes back
    // to the previous level (i.e., bnd-1)
    static int bnd=0;
    if(bnd > bound)
    {
      bnd--;
      return;
    }
    getCoverageForAllVels(graph, v, covered, 2);

    // recur for all the vertices adjacent to this vertex
    int nxt_index;
    node_t* temp = graph.adj[v]->next;

    while(temp!=NULL)
    {
       nxt_index = graph.umap[temp->nid]; // finding int index from address
       bnd++;
       DFSUtil(graph, nxt_index, bound, covered);
       temp = temp->next;
    }
    bnd>=1? --bnd:bnd;
    return;
}


// compute coverable nodes for all nodes. initialization.
void computeCoverablesForBoundaryNodes (graph_t& graph, workspace_t workspace)
{
   int x,y;
   ostringstream oss;
   int precision = 2;
   unsigned int node;

   for(unsigned int i=0; i<workspace.boundary.size(); i++)
   {
      x = workspace.boundary[i].x; y = workspace.boundary[i].y;
      for(unsigned int vel=0; vel<graph.count_vel; vel++)
      {
	// get the node index of a boundary vertex
  	oss << setw(precision) << setfill('0') << x << setw(precision) << y << setw(precision) << vel;
	node = graph.umap[oss.str()]; // get node index
	graph.boundary.push_back(node);  // insert node to boundary set

	// get coverables by a boundary node
      	DFSUtil(graph, node, workspace.d, graph.adj[node]->coverable);

	oss.str("");
      }
   }
   return;
}

// compute coverable nodes for all nodes. initialization.
void computeCoverablesForAllNodes (graph_t& graph, unsigned int d)
{
   for(unsigned int i=0; i<graph.count_graph_nodes; i++)
   {
      DFSUtil(graph, i, d, graph.adj[i]->coverable);
   }
   return;
}


// get the node index with maximum covering size
unsigned int getMaxCoveringNode (graph_t graph)
{
        int maxsize=0, setsize, maxind=0;
	unsigned int node;
        // maximum set size and index among all vertices
        for(unsigned int i=0; i<graph.boundary.size(); i++)
        {
	   node = graph.boundary[i]; // get node index
           setsize = (graph.adj[node]->coverable).size();
           if(maxsize < setsize)
           {
                maxsize = setsize;
                maxind = node;
           }
        }
        return maxind;
}


// are all the nodes covered ?
int isCoveredAll (graph_t graph)
{
        int flag=1;
        for(unsigned int i=0; i<graph.count_graph_nodes; i++)
        {
           if((graph.adj[i]->coverable).size() > 1) // self node may still remain
           {
                flag=0;
                break;
           }
        }
        return flag;
}


// show details of the problem instance
void printDetails (graph_t graph, unsigned int d)
{
        cout << "graph nodes: " << graph.count_graph_nodes << endl;
        cout << "velocities: " << graph.count_vel << endl;
	cout << "d = " << d << endl;
        cout << endl;
        return;
}


void printVector(std::vector<unsigned int> vec)
{
  unsigned int count;
  for(count = 0; count < vec.size(); count++)
  {
    cout << " " << vec[count];
  }
  cout << endl << "vector size: " << vec.size() << endl;
}


// greedy heuristic for finding the minimum vertex cover
void greedyHeur_VC (graph_t graph, workspace_t workspace)
{
  unsigned int maxind;
  set<unsigned int> cover;
  printDetails(graph, workspace.d);

  // compute coverable nodes for bondary the nodes
  computeCoverablesForBoundaryNodes(graph, workspace);

  unsigned int isolated_count = processIsolatedNodes(graph);
  cout << endl;
  cout << "isolated nodes: " << isolated_count << endl << endl;

  set<unsigned int> myset;
  while(!isCoveredAll(graph)) // continue until all are covered
  {
    cout << endl << "-------------" << endl;
    // change heur3
    maxind = getMaxCoveringNode(graph); // select from boundary nodes

    // select the node with maximum coverable
    // set minus maximum coverables from all other coverables
    cout << "selected the max covering vertex: " << maxind;
    cout << " with " << (graph.adj[maxind]->coverable).size();
    cout << " nodes covered." << endl;
    cout << " with " << graph.adj[maxind]->nid;
    cover.insert(maxind);

    myset.clear();
    myset = graph.adj[maxind]->coverable;
    for(unsigned int i=0; i<graph.count_graph_nodes; i++)
    {
        graph.adj[i]->coverable = set_minus(graph.adj[i]->coverable, myset);
    }
  }   
  cout <<  endl << "COVER SIZE: " << cover.size();
  cout << endl << endl;

  return; 
}

