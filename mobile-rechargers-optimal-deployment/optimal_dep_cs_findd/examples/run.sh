#!/bin/bash

if [ "$1" == '' ]; then
	echo 'type the following command..'
	echo 'USAGE: ./run.sh tool_z3'
       	exit
fi

cd ../src/
make -f Makefile_safety $1
cd ../examples/
echo "Executable files made.."

mv ../src/$1 .
echo "Executable files moved to the current directory.."
echo

./$1 $2
#echo "The input file for Z3 has been generated.."
./clean.sh
exit 0
