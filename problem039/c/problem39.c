#include <stdio.h>

int is_pythagorean(int a, int b, int c) {
	return (a*a + b*b == c*c);
}

int main(int argc, char *argv[]) {
	int upto = 1000;
	int maxcount = 0;
	int maxfor = 0;
	int count = 0;
	int c = 0;

	for(int n = 3; n < upto; ++n) {
		count = 0;
		// This method of iteration means that a <= b <= c
		for(int a = 1; a <= n/3; ++a) {
			for(int b = a; b <= (n-a)/2; ++b) {
				if(is_pythagorean(a, b, n - a - b)) {
					++count;
				}
			}
		}

		if(count >= maxcount) {
			maxcount = count;
			maxfor = n;
		}
	}

	printf("%d\n", maxfor);

	return 0;
}
