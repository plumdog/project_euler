#include <iostream>
#include <prime.h>

using namespace std;


int main() {
	int req = 10001;

	int value = 2;
	int prime_count = 0;

	while(true) {
		if(is_prime(value)) {
			++prime_count;
		}

		if(prime_count == req) {
			break;
		}

		++value;
	}

	cout << value << endl;
	return 0;
}
