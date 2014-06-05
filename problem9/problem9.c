#include <stdio.h>

int is_pythagorean(int i, int j, int k) {
	int a, b, c;
	if(i > j && i > k) {
		c = i;
		a = j; b = k;
	} else if(j > i && j > k) {
		c = j;
		a = i; b = k;
	} else {
		c = k;
		a = i; b = j;
	}

	return (a*a + b*b == c*c);
	
}

int find_pythagorean(int num) {
	int i, j, k;

	for(i = 1; i < num; ++i) {
		for(j = i + 1; j < num - i - 1; ++j) {
			k = num - i - j;

			

			if(is_pythagorean(i, j, k)) {
				return i * j * k;
			}
		}
	}
}

int main() {
	int result = find_pythagorean(1000);
	printf("%d\n", result);

	return 0;
}
