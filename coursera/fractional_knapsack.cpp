#include <iostream>
#include <vector>

using std::vector;


int maxim(vector<int> v, vector<int> w,int n)
{
	double max=0.0;
	int index=-1;
	for(int i=0;i<n;i++)
	{
		if(w[i]>0 && ((v[i]*1.0)/w[i])>max)
		{
			max= (v[i]*1.0)/w[i];
			index=i;
		}
	}
	return index;
}


double get_optimal_value(int capacity, vector<int> weights, vector<int> values,int n)
{
	double value = 0.0;
	long i,a,j;
	
	for(i=0;i<n;i++)
	{
		if(capacity==0)
		return value;
		j=maxim(values,weights,n);
		if(j>-1)
		{
			a=(weights[j]>capacity)?capacity:weights[j];
			value+= (a*values[j]*1.0)/weights[j];
			weights[j]-=a;
			capacity-=a;
		}
	}
	
	return value;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values, n);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
