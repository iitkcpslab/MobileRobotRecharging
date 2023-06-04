# Charging Station Placement for Indoor Robotic Applications

Published in: ICRA-2018 .  
Authors: Tanmoy Kundu, Indranil Saha. Both of them are with the Department of Computer Science and Engineering, IIT Kanpur.

The paper can be found in this link : https://ieeexplore.ieee.org/document/8461006

For an autonomous mobile robot, when the available power goes below a certain threshold, 
the robot needs to abort its current task and move towards a charging station to recharge its battery. 
The efficiency of an autonomous mobile robot depends significantly on the location of the charging stations. 
In this paper, we address the charging station placement problem for mobile robots in a controlled workspace. 
We propose two algorithms to place a number of charging stations so that a robot is always capable of reaching 
one of the charging stations from any obstacle-free location in the workspace without aborting its task too early. 
We reduce the charging-station placement problem to a series of Satisfiability Modulo Theory (SMT) problems and 
use the off-the-shelf SMT solver Z3 to implement our algorithm. The algorithm produces as output the locations of 
the charging stations in the workspace and the trajectories from any obstacle-free locations to one of the charging stations. 
Our experimental results show how our algorithm can efficiently find the locations of the charging stations and robot 
trajectories to reach the charging stations. We demonstrate through simulation how the generated trajectories can be 
effectively used by a robot to reach a charging stations autonomously without getting depleted with power.


PREREQUISITES:
--------------
1. UNIX environment
2. g++
3. make
4. SMT solver Z3 (Installation link: https://github.com/Z3Prover/z3)

HOW TO RUN:
-----------
a) Move to directory  ``energy-aware-temporal-logic-motion-planning/<approach-name>/examples''.

b) Following input files are needed in the ``charging-stn-placement-smt/<approach-name>/examples'' directory:
     workspace.txt  obstacle.txt  2d_template.txt input

c) Execute the following from ../examples directory.

 ./run.sh tool\_z3 \<perturbation\>  for  csp-findncs-turt-quad  and  csp-findncs-dubin
 ./run.sh tool\_z3 \<fixed_ncs_value>\ \<perturbation\>  for  csp-findd-turt-quad  and  csp-findd-dubin
 
 ./run.sh tool\_z3 \<fixed_param_value>\>  for  csp-naive-findd-turt-quad, csp-naive-findd-dubin and csp-naive-findncs-turt-quad 
 ./run.sh tool\_z3  for  csp-naive-findd-dubin  and  csp-naive-findncs-dubin


d) Output will appear on the console.

INPUT FILE DETAILS:
------------
Following input files contain input parameters to the program. Here, we mention the attributes of each input file.

1. workspace.txt
<max x coordinate>
<max y coordinate>



2. obstacle.txt contains obstacle grid positions (2-D)


3. 2d_template.txt contains motion primitive details
<primitive id>
<initial velocity>
<final velocity>
<displacement of [x, y] distance from current position>
<cost of applying this primitive>
<time required to apply this primitive>
<swath locations from the current location, while applied>


Similarly, details of other primitives are captured.

For any query, kindly contact Dr. Tanmoy Kundu at tanmoy1040@gmail.com .

