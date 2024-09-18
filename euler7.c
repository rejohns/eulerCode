#include<stdio.h>

int isPrime(long m) {

	int i;
	
	for(i = 2; i <= m/2; i++) {
		if (m % i == 0) {
			return 0;
		}
	}
	return 1;

}

int main(void) {
	
	int count = 0;
	
	long i = 2;
	
	while(count < 10001) {
		if (isPrime(i) == 1) {
			count++;
			printf("count: %d; i: %ld\n", count, i);
		}
		i++;
	}
	
	return 0;
	
}