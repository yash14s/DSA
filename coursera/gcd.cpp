#include <iostream>

int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
}

int euclidean_GCD(long int a,long int b)
{
	long int c;
	if(b==0)
	{
		return a;
	}
	c=a%b;
	return euclidean_GCD(b,c);
}

int main() {
  long int a, b;
  std::cin >> a >> b;
  //std::cout << gcd_naive(a, b) << std::endl;
  std::cout<<euclidean_GCD(a,b)<<std::endl;
  return 0;
}
