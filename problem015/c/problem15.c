#include <stdio.h>
#include <math.h>

/* We want to store results and not have to recalculate. We do this by
 * storing an array. We need to map keys from {1..20} x {1..20} to ints,
 * which we do with the hash function.
 */
int size = 20;
long long cached[401]; // max hash = 400 from 20*19 + 20

int hash(int x, int y) {
	if(x > y) {
		return size*(y - 1) + x;
	} else {
		return size*(x - 1) + y;
	}
}

void insert(int x, int y, long long result) {
	int hash_val = hash(x, y);
	cached[hash_val] = result;
}

long long get(int x, int y) {
	int hash_val = hash(x, y);
	return cached[hash_val];
}

/* Use recursion. From any grid point, there are two choices: go down
 * or go right. The number of paths from that point is just the sum of
 * the number of paths from either of the two next steps. However, if
 * we have reached x = 0 or y = 0, then there is just one path.
 */
long long paths_from(int x, int y) {
	if((x == 0) || (y == 0)) {
		return 1;
	}

	long long result = get(x, y);

	/* If we found a result in the cached results, then return it,
	 * otherwise, calculate the result, store it in the cache,
	 * then return that. */
	if(!result) {
		result = (paths_from(x - 1, y) + paths_from(x, y - 1));
		insert(x, y, result);
		return result;
	}

	return result;
}

int main() {
	printf("%lld\n", paths_from(size, size));
	return 0;
}
