#include <iostream>
#include <prime.h>

using namespace std;


int main() {
	int top = 2000000;
	int trial;

	long long total = 2; // include 2

	for(int trial = 3; trial < top; ++trial) {
		if(is_prime(trial)) {
			total += trial;
		}
	}

	cout << total << endl;
}
