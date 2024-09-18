/*
 * Sum of all primes below 2,000,000
 */

#include<stdio.h>
#include<math.h>

int isPrime(long x) {

	double root = sqrt(x);
	long froot = floor(root);
	
	long i;
	
	for(i = 2; i <= froot; i++) {
		if (x % i == 0) {
			return 0;
		}
	}
	
	return 1;
	
	return froot;

}

int main(void) {
	
	long i;
	
	long sum = 2;
	
	for(i = 3; i < 2000000; i+= 2) {
		if(isPrime(i) == 1) {
			sum += i;
		}
	}
	printf("sum: %ld\n", sum);
		
	return 0;
}