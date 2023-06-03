#!/bin/bash

if [ "$1" == '' ]; then
	echo 'type the following command..'
	echo './run.sh model_approx'
       	exit
fi

cd ../src/
make -f Makefile_safety $1
cd ../examples/
echo "Executable files made.."

mv ../src/$1 .
echo "Executable files moved to the current directory.."

./$1
echo "The input file for Z3 has been generated.."

rm *.o model_approx
cd ../src/
rm *.o
echo "Temporary files removed.."

exit 0
