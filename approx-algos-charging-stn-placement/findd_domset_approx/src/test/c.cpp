#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
  set<int> s1;
  set<int> s2;

  s1.insert(1);
  s1.insert(2);
  s1.insert(3);
  s1.insert(4);

  s2.insert(1);
  s2.insert(6);
  s2.insert(3);
  s2.insert(0);
  s2.insert(0);
  s2.insert(4);
  s2.insert(2);

set<int> intersect;
//intersect = foo(s1,s2);

set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                 	inserter(intersect, intersect.begin()));  

        // using begin() to print set
        for (auto it = intersect.begin(); it != intersect.end(); ++it)
        {
                cout << *it << ",";
        }
        //cout << endl << "Set size = " << c.size() << endl;
        cout << "  intersect size = " << intersect.size() << endl;

   int nrows=5;
   int a[nrows]; a[4]=47;
   set<unsigned int> covset[nrows];
   //covset = (set<unsigned int>*)malloc(sizeof(set<unsigned int>)*3);

   covset[0].insert(10);
   covset[0].insert(0);
   covset[0].insert(0);
   covset[0].insert(20);
   covset[0].insert(15);

        for (auto it = covset[0].begin(); it != covset[0].end(); ++it)
        {
                //cout << it << "  " << *it << ",";
                cout << "  " << *it << ",";
        }

  return 0;
}
