
void declareVariables_workers (ofstream & , workspace_t, worker_vec_t);
void declareVariables_workers2 (ofstream & , workspace_t, worker_vec_t, workerhalt_vec_t, unsigned int);

void instantiateVariables_workers (ofstream & , workspace_t, worker_vec_t);
void instantiateVariables_workers2 (ofstream & , workspace_t, worker_vec_t, workerhalt_vec_t, unsigned int);

void writeMatchingConstraints_workers (ofstream &, workspace_t, worker_vec_t);
void writeMatchingConstraints_workers2 (ofstream &, workspace_t, worker_vec_t, workerhalt_vec_t, unsigned int, unsigned int);

void writeTrajectoryToLoopMapping_workers (ofstream &, workspace_t, worker_vec_t);
void placeRecharger1 (ofstream &, worker_vec_t, unsigned int, unsigned int, unsigned int, int, int); 

void writeTransition_workers (ofstream &, workspace_t, worker_vec_t);
void writeTransition_workers2 (ofstream &, workspace_t, worker_vec_t, workerhalt_vec_t, unsigned int);

void minimizeWaiting_workers (ofstream &, workspace_t, worker_vec_t);
void minimizeRecharging_workers (ofstream &, workspace_t, worker_vec_t, workerhalt_vec_t, unsigned int);

void writeOutputConstraints_workers (ofstream &, workspace_t, worker_vec_t);
void writeOutputConstraints_workers2 (ofstream &, workspace_t, worker_vec_t, workerhalt_vec_t, unsigned int);
