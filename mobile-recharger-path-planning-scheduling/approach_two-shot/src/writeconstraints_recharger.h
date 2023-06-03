unsigned int get_max_intrech_timept (workerhalt_vec_t);

void declareVariables_rechargers (ofstream &, workspace_t);
void declareVariables_rechargers2 (ofstream &, workspace_t, workerhalt_vec_t, unsigned int, unsigned int);

void writeTransitionConstraints_rechargers (ofstream &, prim_vec_t, pos_vec_t, workspace_t, unsigned int);
void writeTransitionConstraints_rechargers2 (ofstream &, prim_vec_t, pos_vec_t, workspace_t, unsigned int, unsigned int, workerhalt_vec_t);

void writeCollisionAvoidanceConstraints (ofstream &, prim_vec_t, workspace_t);
void writeCollisionAvoidanceConstraints_rechargers2 (ofstream &, workspace_t, worker_vec_t, unsigned int, unsigned int);

void writeOutputConstraints_rechargers (ofstream &, workspace_t);
void writeOutputConstraints_rechargers2 (ofstream &, workspace_t, workerhalt_vec_t, unsigned int, unsigned int);

void minimizeWaiting_rechargers (ofstream &, workspace_t, worker_vec_t);
string floatToReal(string);
template <typename T> string tostr(const T&);
