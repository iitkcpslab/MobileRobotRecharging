void printTimeDifference(double , double );
int generateTrajectory(prim_vec_t , prim_cost_t , pos_vec_t , workspace_t );
void optimizeTrajectory(prim_vec_t , prim_cost_t , pos_vec_t , workspace_t , int );
vector<position> getTrajectory();
void printTrajectory(vector<position> traj);
void matlab_code_generator(workspace_t, pos_vec_t, vector<position>);
