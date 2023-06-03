#include <string>
#include <set>
#include <vector>
#include <unordered_map>

struct w
{
  unsigned int length_x;
  unsigned int length_y;
  unsigned int min_x=0;
  unsigned int min_y=0;
  unsigned int ncs;
  unsigned int number_of_locs;
  position *pos_start;  
  pos_vec_t boundary;
};
typedef struct w workspace_t;


struct x
{
  string nid; // a derived info from pos and vel 
  position pos;
  int vel;
  unsigned int outdeg;
  //struct x* next;
  bool visited;
};
typedef struct x node_t;


struct y
{
  node_t** nodes; 
  int** adjmat; 
  bool* visit_list; 
  unsigned int ncs; 		// newly added
  set<unsigned int> covrd;
  set<unsigned int> notcovrd;
  set<unsigned int> cover;
  unsigned int count_graph_nodes;
  unsigned int count_vel;
  unordered_map<string, unsigned int> umap;
  std::vector<unsigned int> boundary;
};
typedef struct y graph_t;


struct z
{
  unsigned int timept;
  position pos;
};
typedef struct z visit_t;


typedef std::vector<visit_t> visit_vec_t;


struct a
{
  unsigned int dim;
  unsigned int wcount;
  unsigned int rcount;
  unsigned int unitrech;
  unsigned int orig_hlen;

  unsigned int ext_hlen;
  unsigned int wait_idle;
  unsigned int intrechcount;
  unsigned int lastrechcount;
  double hardeffic;
  double softeffic;

  string elapsed_time;
  string consolid_wtrajs;
  string consolid_rtrajs;
  string rechinstances;
  string lastrechs;
};
typedef struct a testcase_t;


typedef std::vector<Primitive> prim_vec_t;

void readObstacles (pos_vec_t & );
void writePositions (pos_vec_t);
void readWorkspace (workspace_t &, pos_vec_t);
void readPrimitives (prim_vec_t & ); 
void writePrimitives (prim_vec_t );
pos_vec_t findBoundaryPoints(workspace_t, pos_vec_t);

unsigned int isWSameChargeValue (string, string);
pos_vec_t readWorkingTraj (string, string, string, unsigned int);

string getRechargerTraj (string, unsigned int); //change15
position readRechargerPosition (string, unsigned int, unsigned int); //change15

unsigned int readValue (string, string);
void batch_proessing (unsigned int, unsigned int, unsigned int, double);
unsigned int tot_wait_upto_halt (string, string, unsigned int, unsigned int);

set<int> getVelocityDistinct (prim_vec_t);
void printVelocityDistinct (set<int>);
int find_pos(pos_vec_t, position);
pos_vec_t getFreeLocations (workspace_t, pos_vec_t);

