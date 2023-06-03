#include <iostream>
using namespace std;
int main(void)
{
    // This program will create same sequence of 
    // random numbers on every program run 
 
    for(int i = 0; i<5; i++)
        cout << rand()%620 << endl;
   
    return 0;
}
