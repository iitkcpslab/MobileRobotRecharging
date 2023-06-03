
# Mobile Recharger Path Planning and Recharge Scheduling in a Multi-Robot Environment

Published in: IROS-2021\\
Authors: Tanmoy Kundu, Indranil Saha

In many multi-robot applications, mobile worker
robots are often engaged in performing some tasks repetitively
by following pre-computed trajectories. As these robots are
battery-powered, they need to get recharged at regular intervals. We envision that, in the future, a few mobile recharger
robots will be employed to supply charge to the energy-deficient
worker robots recurrently to keep the overall efficiency of
the system optimized. In this setup, we need to find the time
instants and locations for the meeting of the worker robots and
recharger robots optimally. We present a Satisfiability Modulo
Theory (SMT)-based approach that captures the activities of
the robots in the form of constraints in a sufficiently long finitelength time window (hypercycle) whose repetitions provide their
perpetual behavior. Our SMT encoding ensures that for a
chosen length of the hypercycle, the total waiting time of the
worker robots due to charge constraints is minimized under
certain condition, and close to optimal when the condition
does not hold. Moreover, the recharger robots follow the
most energy-efficient trajectories. We show the efficacy of our
approach by comparing it with another variant of the SMTbased method which is not scalable but provides an optimal
solution globally, and with a greedy algorithm.

PREREQUISITES:
--------------
1. UNIX environment
2. g++
3. make
4. SMT solver Z3 (Installation link: https://github.com/Z3Prover/z3)

HOW TO RUN:
-----------
a) Move to directory  ``mobile-recharger-path-planning-scheduling/<approach-name>/examples''.

b) Following input files are needed in the ``mobile-recharger-path-planning-scheduling/<approach-name>/examples'' directory:
     workspace.txt  obstacle.txt  2d_template.txt  rob1_traj.txt  rob2_traj.txt  rob3_traj.txt  rob4_traj.txt  rob5_traj.txt  rob6_traj.txt .

b.a) Some input directories are already available in ``mobile-recharger-path-planning-scheduling/<approach_name>/examples'' directory. Files can be copied from these directories to  ``mobile-recharger-path-planning-scheduling/<approach-name>/example'' directory.  

c) Execute  ./run.sh tool_z3  from ``IROS2021-Submission-52/<approach-name>/examples'' directory.

d) Output will appear on the console.

INPUT FILE DETAILS:
------------
Following input files contain input parameters to the program. Here, we mention the attributes of each input file.

1. workspace.txt
<max x coordinate>
<max y coordinate>
<no. of worker robots>
<original hyperloop length>
<max. recharge amount per unit time>
<no. of recharger robots>


2. rob1_traj.txt (contains worker-1 details, similar input files for other worker robots)
<full charge amount>
<no. of trajectory points>
<position of trajectory point 1>
<position of trajectory point 2> 
and so on ...
<charge cost for moving from point-1 to point-2>
<charge cost for moving from point-2 to point-3>
and so on ...


3. obstacle.txt contains obstacle grid positions (2-D)


4. 2d_template.txt contains motion primitive details
<primitive id>
<initial velocity>
<final velocity>
<displacement of [x, y] distance from current position>
<cost of applying this primitive>
<time required to apply this primitive>
<swath locations from the current location, while applied>

Similarly, details of other primitives are captured.

