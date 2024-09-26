#include <iostream>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

long int euclidean_GCD(long int a,long int b)
{
	long int c;
	if(b==0)
	{
		return a;
	}
	c=a%b;
	return euclidean_GCD(b,c);
}

long long lcm_smart(long int a,long int b)
{
	long long lcm;
	lcm=a/euclidean_GCD(a,b);
	lcm*=b;
	return lcm;
}

int main() {
  long int a, b;
  std::cin >> a >> b;
  //std::cout << lcm_naive(a, b) << std::endl;
  std::cout << lcm_smart(a, b) << std::endl;
  return 0;
}
