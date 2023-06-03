
void declareVariables2 (ofstream &, workspace_t, unsigned int);
bool isObstacle (pos_vec_t, position);
void writeWaypointsConstraints2 (ofstream &, workspace_t, pos_vec_t, worker_vec_t, rechinst_vec_t, workerhalt_vec_t, unsigned int);
void writeTransitionConstraints2 (ofstream &, prim_vec_t, pos_vec_t, workspace_t, unsigned int);
void minimizeWaiting2 (ofstream &, unsigned int);
void writeOutputConstraints2 (ofstream &, unsigned int, workspace_t, workerhalt_vec_t, unsigned int);
bool isObstacle (pos_vec_t, position);
void placeRecharger2 (ofstream &, worker_vec_t, pos_vec_t, unsigned int, unsigned int, unsigned int, int, int, unsigned int); 
void writeWaypointsConstraints3 (ofstream &, rechinst_vec_t);
void writeCollisionAvoidanceConstraints2 (ofstream &, workspace_t, worker_vec_t, unsigned int);
void writeCollisionAvoidanceConstraints3 (ofstream &, worker_vec_t, unsigned int);
