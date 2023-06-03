
struct w
{
  unsigned int length_x;
  unsigned int length_y;
  unsigned int min_x;
  unsigned int min_y; 
  unsigned int number_of_wrobs;
  unsigned int hlen;
  unsigned int recharge;
  unsigned int number_of_rechs;
  pos_vec_t rpos_start;
  pos_vec_t rpos_hlen;
};

typedef struct w workspace_t;

struct wr
{
  unsigned int fch;
  position wpos_start;
  unsigned int looplen;
  pos_vec_t looptraj;
  vector<unsigned int> req_charge;
  pos_vec_t workingtraj;
};

typedef struct wr worker_t;
typedef std::vector<worker_t> worker_vec_t;

struct z
{
  unsigned int timept;
  position pos;
};
typedef struct z visit_t;
typedef std::vector<visit_t> visit_vec_t;

struct x
{
  unsigned int worker_id;
  unsigned int rech_id;
  unsigned int timept;
  position trajpt;
};
typedef struct x rechinst_t;
typedef std::vector<rechinst_t> rechinst_vec_t;

struct y
{
  unsigned int worker_id;
  unsigned int timept;
  unsigned int charge;
  unsigned int duration;
};
typedef struct y workerhalt_t;
typedef std::vector<workerhalt_t> workerhalt_vec_t;

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
  string obs_name;
};

typedef struct a testcase_t;


typedef std::vector<Primitive> prim_vec_t;

void readObstacles(pos_vec_t &, testcase_t &);
void writeObstacles(pos_vec_t);
void readWorkspace(workspace_t &, pos_vec_t &, worker_vec_t &);
worker_t readWorkerUtil(string);
void readPrimitives(prim_vec_t & ); 
void extendObstaclesList (pos_vec_t &, worker_vec_t); //change15

void writePrimitives(prim_vec_t );
string readRechInstances (rechinst_vec_t &, worker_vec_t, string);
rechinst_vec_t readRechInstances_trajpt (rechinst_vec_t &, string);
unsigned int isWSameChargeValue (string, string);
workerhalt_t getWChargeDetails (string , worker_vec_t, workspace_t);
string readWorkerHaltDetails (workerhalt_vec_t &, workspace_t, worker_vec_t, string);
void writeWChargeDetails (workerhalt_vec_t);
pos_vec_t readWorkingTraj (string, string, string, unsigned int);
string writeWorkingTraj (worker_vec_t);

string getRechargerTraj (string, unsigned int);
position readRechargerPosition (string, unsigned int, unsigned int); //change15

unsigned int readValue (string, string);
//void matlab_code_generator (pos_vec_t, worker_vec_t, pos_vec_t);
//void matlab_code_generator (pos_vec_t, worker_vec_t, vector<pos_vec_t>);
void batch_proessing (unsigned int, unsigned int, unsigned int, double);
unsigned int tot_wait_upto_halt (string, string, unsigned int, unsigned int);
