#include<stdio.h>
#include<math.h>

long getNumDivisors(long x) {

	float root = sqrt(x);
	long froot = floor(root);

	long numDivisors = 1;
	
	long i;
	
	while(x ) {
		for(i = 2; i <= froot; i++) {
			
			if (x % i == 0) {
				
				numDivisors++;
				x = x % i;
				
			}
			
		}	
	}
	
	return numDivisors;
	
}

int main(void) {

	long num = 0;
	long i;
	
	for(i = 1; i < 100; i++) {
		num += i;
		//if(getNumDivisors(num) > 500){
			printf("num: %5ld; divisors: %ld\n", num, getNumDivisors(num));
		//	return num;
		//}
	}
	
	return 0;

}