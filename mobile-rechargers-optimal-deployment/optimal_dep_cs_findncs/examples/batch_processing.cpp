#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
	cout << "****** Warehouse 12*12, points=10, SIMPLE ******" << endl;
	system("cp 2d_template_simple8.txt 2d_template.txt");
	system("./clean.sh ; time ./run.sh  tool_z3");

	cout << "=============================================================" << endl;
        cout << "****** Warehouse 12*12, points=10, QUADCOPTER ******" << endl;
        system("cp 2d_template_quad.txt 2d_template.txt");
        system("./clean.sh ; time ./run.sh  tool_z3");

	return 0;
}
