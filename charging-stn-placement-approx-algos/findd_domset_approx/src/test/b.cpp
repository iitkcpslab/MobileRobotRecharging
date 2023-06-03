// C++ implementation of the approach 
#include <bits/stdc++.h> 
using namespace std; 
  
class Graph { 
  
    // Number of vertex 
    int v; 
  
    // Number of edges 
    int e; 
  
    // Adjacency matrix 
    int** adj; 
  
public: 
    // To create the initial adjacency matrix 
    Graph(int v, int e); 
  
    // Function to insert a new edge 
    void addEdge(int start, int e); 
  
    // Function to display the DFS traversal 
    void DFS(int start, vector<bool>& visited, int, int&); 
}; 
  
// Function to fill the empty adjacency matrix 
Graph::Graph(int v, int e) 
{ 
    this->v = v; 
    this->e = e; 
    adj = new int*[v]; 
    for (int row = 0; row < v; row++) { 
        adj[row] = new int[v]; 
        for (int column = 0; column < v; column++) { 
            adj[row][column] = 0; 
        } 
    } 
} 
  
// Function to add an edge to the graph 
void Graph::addEdge(int start, int e) 
{ 
  
    // Considering a bidirectional edge 
    adj[start][e] = 1; 
    //adj[e][start] = 1; 
} 
  
// Function to perform DFS on the graph 
void Graph::DFS(int start, vector<bool>& visited, int d, int& end) 
{ 
 
    // Print the current node 
    d++;
    int flag=0;
    cout << "visiting : " << start  << " d=" << d << endl; 
  
    // Set current node as visited 
    visited[start] = true; 
  
    // For every node of the graph 
    for (int i = 0; i < v; i++) { 
  
        // If some node is adjacent to the current node 
        // and it has not already been visited 
        if (adj[start][i] == 1 && (!visited[i]) && d<2) { 
	  //if(start!=i)	d++;
	  if(flag==0) end=i;
	  flag=1; cout << "farthest=" << end << endl;
	  DFS(i, visited, d, end); 
        }
        else{
		cout << "alrdy vstd/no edge : " << i << " (start: " << start << ")" << " d=" << d << endl;
	}	
    } 
} 
  
// Driver code 
int main() 
{ 
    int v = 5, e = 4; 
  
    // Create the graph 
    Graph G(v, e); 
    G.addEdge(0, 1); G.addEdge(0, 2); G.addEdge(0, 4); G.addEdge(0, 3);
    G.addEdge(2, 3); 
    G.addEdge(3, 4); 
  
    // Visited vector to so that 
    // a vertex is not visited more than once 
    // Initializing the vector to false as no 
    // vertex is visited at the beginning 
    vector<bool> visited(v, false); 
  
    // Perform DFS
    int end; 
    visited[3] = true;

    G.DFS(0, visited, -1, end); 
    cout << "farthest node : " << end << endl;
} 
