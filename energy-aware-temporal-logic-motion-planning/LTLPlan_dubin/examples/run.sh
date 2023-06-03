#!/bin/bash

if [ "$1" == '' ]; then
	echo 'USAGE: ./run.sh tool_z3'
       	exit
fi

cd ../src/ltlparser
make
cd ../../examples/
echo "LTL parser made.."

cd ../src/ltl
make
cd ../../examples/
echo "Executable files made.."

mv ../src/ltlparser/formula_simplifier .
mv ../src/ltlparser/constraints_generator .
mv ../src/ltl/$1 .
echo "Executable files moved to the current directory.."

./$1

#time z3 constraints.smt2

exit 0
