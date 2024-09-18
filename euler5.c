/*
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
 * without any remainder.
 * What is the smallest positive number that is evenly divisible by all of the numbers 
 * from 1 to 20?
 */
 
#include<stdio.h>
 
int main(void) {
	
	// 2, 3, 5, 7, 11, 13, 17, 19
	// 4 -> 2
	// 6 ->
	// 8 -> 2
	// 10 ->
	// 12 ->
	// 14 ->
	// 15 ->
	// 16 -> 2
	// 18 -> 3
	// 20 -> 
	
	int i = 2*3*5*7*11*13*17*19*2*2*2*3;
	printf("%d\n",i);


	return 0;
	
}