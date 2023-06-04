
# SMT-based Optoimal Deployment of Mobile Rechargers 

Published in: ICRA-2021 .  
Authors: Tanmoy Kundu, Indranil Saha. Both of them are with the Department of Computer Science and Engineering, IIT Kanpur.

The paper can be found in this link : https://ieeexplore.ieee.org/abstract/document/9561061


Efficient recharging is an essential requirement for
autonomous mobile robots. In an indoor robotic application,
charging stations can be installed offline. However, frequent
trips to the charging stations cause inefficiency in the performance of the mobile robots. In an outdoor environment, a
charging station cannot even be installed easily. We propose a
framework and algorithms for enabling a group of mobile wireless rechargers to fulfill the energy requirement of autonomous
mobile robots in a workspace efficiently. Our algorithm finds
the optimal trajectories for the mobile rechargers in such a way
that once there is a need for a recharge, the robots do not need
to spend significant time and energy to get access to a recharger.
Our algorithm is based on a reduction of the problems to
Satisfiability Modulo Theory (SMT) solving problems. We
present extensive experimental results to show that the optimal
trajectories for mobile rechargers can be generated successfully
for different types of robots and workspaces within a reasonable
time. Moreover, a comparison with the performance of static
charging stations establishes that mobile rechargers are more
effective in terms of allowing the autonomous robot to continue
their work for a longer time.


optimal\_dep\_cs\_findncs : Finds the value of ncs for fixed nrech and d values.   
optimal\_dep\_cs\_findd : Finds the value of d for fixed nrech and ncs values.   
optimal\_dep\_cs\_findnrech : Finds the value of nrech for fixed ncs and d values


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
     workspace.txt.bak  obstacle.txt  2d_template.txt  

c) Execute  ./run.sh tool\_z3 \<fixed\_parameter-2 value\> from ../examples'' directory.

d) Output will appear on the console.

INPUT FILE DETAILS:
------------
Following input files contain input parameters to the program. Here, we mention the attributes of each input file.

1. workspace.txt
<max x coordinate>
<max y coordinate>
<fixed parameter-1>


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
