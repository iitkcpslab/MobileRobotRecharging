#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<cstdlib>
using namespace std;

int main()
{
	ifstream ifp;
	ifp.open("./obstacle.txt.antlab2.20by20");
	ofstream ofp;
	ofp.open("./obstacle.txt.antlab2.22by22");
	string str, line;
	int i;

	if(ifp.is_open())
	{
		while(getline(ifp, line))
		{
			i = line.find(" ");
			string sx = line.substr(0,i);
			int xx = atoi(sx.c_str()) + 1;
			string sy = line.substr(i+1);
			int yy = atoi(sy.c_str()) + 1;
	
			cout << "" << xx << " " << yy << endl;
			ofp << "" << xx << " " << yy << endl;
		}
	}
	ofp.close();
	return 0;
}
