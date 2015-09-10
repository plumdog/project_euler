#include <math.h>
#include <stdio.h>

int pentagonal(int n) {
	return n * (3*n - 1) / 2;
}

int is_pentagonal(int number) {
	int temp = 1 + 24*number;
	int sq = (int) sqrt(temp);
	return (sq*sq == temp) && (sq % 6 == 5);
}

int pentagonal_sum_and_difference(int i1, int i2) {
	int p1 = pentagonal(i1);
	int p2 = pentagonal(i2);
	if (is_pentagonal(p1 - p2) && is_pentagonal(p1 + p2)) {
		return p1 - p2;
	} else {
		return 0;
	}
}

int main(int argc, char *argv[]) {
	int x = 1, y = 1;
	int trial = 0;

	while(1) {
		// Iterate over x and y, with y <= x
		if((x == y) && (x % 2 == 1)) {
			++x; ++y;
		} else if(x == y) { // if x is even, move down
			--y;
		} else if((y == 1) && (x % 2 == 0)) {
			++x;
		} else if(x % 2 == 0) {
			--y;
		} else {
			++y;
		}

		if(trial = pentagonal_sum_and_difference(x, y)) {
			printf("%d\n", trial);
			break;
		}
	}

	return 0;
}
