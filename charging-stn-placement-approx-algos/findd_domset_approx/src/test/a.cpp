#include <iostream>
using namespace std;


int** copyMatrix (int** a, int**b, int nrows, int ncols)
{
  for(unsigned int i=0; i<nrows; i++)
  {
    for(unsigned int j=0; j<ncols; j++)
    {
      b[i][j]=a[i][j];
    }
  }
  return b;
}


void printMatrix (int** arr, int nrows, int ncols)
{
    for(unsigned int i=0; i<nrows; i++)
    {
      for(unsigned int j=0; j<ncols; j++)
      {
        //cout << " " << arr[i][j];
	printf(" %2d", arr[i][j]);
      }      
      cout << endl;
    }
    cout << "-----------" << endl;
    return;
}


void initializeMatrix (int** arr, int nrows, int ncols, int* arrelements)
{
  for(unsigned int i=0; i<nrows; i++)
  {
    arr[i] = (int*)malloc(sizeof(int) * ncols);
    for(unsigned int j=0; j<ncols; j++)
    {
      arr[i][j] = arrelements[i*ncols + j];
    }
  }
  return;
}


void initializeMatrix (int** arr, int nrows, int ncols, int elt)
{
  for(unsigned int i=0; i<nrows; i++)
  {
    arr[i] = (int*)malloc(sizeof(int) * ncols);
    for(unsigned int j=0; j<ncols; j++)
    {
      arr[i][j] = elt;
    }
  }
  return;
}


int** multiplyMatrices (int** a, int** b, int nrows1, int ncols1, int nrows2, int ncols2)
{
  int** sum = (int**)malloc(sizeof(int*) * nrows1);
  initializeMatrix (sum, nrows1, ncols2, 0);
  printMatrix (sum, nrows1, ncols2);

  for(unsigned int i=0; i<nrows1; i++)
  {
    for(unsigned int j=0; j<ncols2; j++)
    {
       for(unsigned int k=0; k<ncols1; k++)
       {
	  //cout << sum[i][j] << " + ";
	  //cout << "(" << res[i][k] << " x " << arr[k][j] << ")" << endl;
	  sum[i][j] += a[i][k] * b[k][j];
       }
       //cout << "sum[" << i << "][" << j << "] = " << sum[i][j] << endl << endl;
       //res[i][j] = sum;
    }
  }
  return sum;
}


int main()
{
  int nrows1=3, ncols1=2;  
  int arrelements1[] = {1,0,2,1, 10, 2};
  int** a = (int**)malloc(sizeof(int*) * nrows1);
  initializeMatrix (a, nrows1, ncols1, arrelements1);
  printMatrix (a, nrows1,  ncols1);

  int nrows2=2, ncols2=4;  
  int arrelements2[] = {1,2,1,1,2,1,1,1};
  int** b = (int**)malloc(sizeof(int*) * nrows2);
  initializeMatrix (b, nrows2, ncols2, arrelements2);
  printMatrix (b, nrows2,  ncols2); 

  cout << "=======" << endl;

  int** res = multiplyMatrices (a, b, nrows1, ncols1, nrows2, ncols2);
  printMatrix (res, nrows1, ncols2);
/*  
  int** res = (int**)malloc(sizeof(int*) * rows);
  initializeMatrix (res, rows, 1);
  printMatrix (res, rows);
  
  cout << "=======" << endl;
  for(unsigned int j=1; j<=3; j++)
  {
     copyMatrix (multiplyMatrices (res, arr, rows), res, rows);
     printMatrix (res, rows);
     cout << endl << endl;
  }
*/
  return 0;
}
