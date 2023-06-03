void printHeaders (graph_t);
void printList (node_t*);
bool isObstacle (position, pos_vec_t);
bool isValidMove (position, pos_vec_t, pos_vec_t, workspace_t);
string generateNid (position, unsigned int);
node_t* createNode (position, int);
void insertNodeAtSecondPosition (node_t*, position, state);
void createLists (graph_t&, prim_vec_t, pos_vec_t, workspace_t);
void createNodesForObsFreeLocations (set<int>, pos_vec_t, graph_t&);

set<unsigned int> set_union(set<unsigned int>, set<unsigned int>);
set<unsigned int> set_minus(set<unsigned int>, set<unsigned int>);
void print_set (set<unsigned int>);
void DFSUtil(graph_t&, unsigned int, unsigned int, set<unsigned int>&);
void greedyHeur_VC (graph_t, workspace_t);

