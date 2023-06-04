
struct w
{
  unsigned int length_x;
  unsigned int length_y;
  unsigned int number_of_uavs;
  position *pos_start;
  position *pos_end;
  unsigned int number_of_points;
  unsigned int number_of_cs;
  string total_cost;
  pos_vec_t csvec;
  pos_vec_t boundary;
};

typedef struct w workspace_t;

typedef std::vector<Primitive> prim_vec_t;

struct x
{
  unsigned int xmax;
  unsigned int ymax;
  string obs_name;
  string prims_name;
  unsigned int fixed_param;
  unsigned int derived_param;
  string trajectory;
  string elapsed_time;
};

typedef struct x testcase_t;

void readPrimitives(prim_vec_t & , testcase_t &); 
void writePrimitives(prim_vec_t );
void readObstacles(pos_vec_t &, testcase_t &);
void writeObstacles(pos_vec_t );
void writeObstaclesToFile(pos_vec_t );
int find_pos(pos_vec_t &posvec, position pos);
void readWorkspace(workspace_t &workspace, pos_vec_t &ob, testcase_t &);
void writeWorkspace(workspace_t);
void readRechPrimitives (prim_vec_t &);
