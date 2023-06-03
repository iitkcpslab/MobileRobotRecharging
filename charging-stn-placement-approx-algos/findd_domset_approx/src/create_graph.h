bool isObstacle (position, pos_vec_t);
bool isValidMove (position, pos_vec_t, pos_vec_t, workspace_t);
void getBoundaryNodes (graph_t&, workspace_t);
void printBoundaryNodes (vector<unsigned int>);
string getNid (position, unsigned int);
node_t* createNode (position, int);

void printIncidentNodes (graph_t, int);
void createNodesForObsFreeLocations (set<int>, pos_vec_t, graph_t&);
void createAdjMatrix (graph_t&, prim_vec_t, pos_vec_t, workspace_t);

set<unsigned int> set_union(set<unsigned int>, set<unsigned int>);
set<unsigned int> set_minus(set<unsigned int>, set<unsigned int>);
void print_set (graph_t, set<unsigned int>);
void print_set (set<unsigned int>);
set<unsigned int> makeSet_AllIndices (unsigned int);

void greedyHeur_adjmat (graph_t);

