#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int> & stops,int n) {
    int numref=0,currentref=0,lastref=0,i;
	int x[n+2];
    x[0]=0;
    for(i=1;i<n+1;i++)
    x[i]=stops[i-1];
    x[n+1]=dist;
    
    while(currentref<n+1)
    {
		lastref=currentref;
    	while(currentref<n+1 && (x[currentref+1]-x[lastref])<tank+1)
    	currentref++;
    	
    	if(currentref==lastref)
		return -1;
		
		if(currentref<n+1)
		numref++;
	}
	return numref;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops,n) << "\n";

    return 0;
}
