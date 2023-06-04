
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
  unsigned int dubin_number_of_uavs;
};

typedef struct w workspace_t;


struct d
{  
  unsigned int length_x;
  unsigned int length_y;
  unsigned int number_of_uavs;
  unsigned int perc_obs;
};

typedef struct d dimension_t;


struct c
{
  float max_cost;
  float min_cost;
  float min2_cost;
  float min_cost_diff;
  float min2_min_cost_diff;
};

typedef struct c prim_cost_t;

 
typedef std::vector<Primitive> prim_vec_t;


void readPrimitives(prim_vec_t & ); 
void writePrimitives(prim_vec_t );
void readObstacles(pos_vec_t & );
void writeObstacles(pos_vec_t );
void writeObstaclesToFile(pos_vec_t );
int find_pos(pos_vec_t &posvec, position pos);
//void readWorkspace(workspace_t &);
//void readWorkspace1(workspace_t &ws);
void readWorkspace(workspace_t &workspace, pos_vec_t &ob);
void writeWorkspace(workspace_t);
void readDimension(dimension_t &);
void writeDimension(dimension_t);
void writeDimensionToFile(dimension_t );
void getPrimitiveCost(prim_vec_t , prim_cost_t & );
void writePrimitiveCost(prim_cost_t & );
void readCTLSpec(string &ctlspec);
