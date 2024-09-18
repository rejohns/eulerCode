#include<stdio.h>
#include<math.h>

long gaussSum(long m) {
	
	long sum = (m * (m + 1)) / 2;
	
	return sum;
	
}

int main(void) {
	
	long sqsum = pow(gaussSum(100), 2);
	
	long sumsq = 0;
	
	int i;
	
	for(i = 1; i < 101; i++) {
		sumsq += i * i;
	}
	
	long diff = sqsum - sumsq;
	
	printf("diff: %ld\n", diff);
	
	return 0;
	
}