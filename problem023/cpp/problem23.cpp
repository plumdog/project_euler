#include <iostream>
#include <unordered_set>


typedef std::unordered_set<int> IntSet;


bool isSumOfTwoAbundants(int n, IntSet &abundants) {
    for (int f : abundants) {
        if(abundants.count(n - f)) {
            return true;
        }
    }
    return false;
}


bool isAbundant(int n) {
    int sum = 0;
    for(int i = 1; i <= n / 2; ++i) {
        if(n % i == 0) {
            sum += i;
        }
    }
    return sum > n;
}


IntSet getAbundants(int max) {
    IntSet abundants;
    for(int i = 1; i <= max; ++i) {
        if (isAbundant(i)) {
            abundants.insert(i);
        }
    }
    return abundants;
}


int sumNumsNotSumOfTwoAbundants(int upto) {
    IntSet abundants = getAbundants(upto);
    int total = 0;

    for(int i = 1; i <= upto; ++i) {
        if(!isSumOfTwoAbundants(i, abundants)) {
            total += i;
        }
    }
    return total;
}


int main() {
    int upto = 28123;
    std::cout << sumNumsNotSumOfTwoAbundants(upto) << std::endl;
}
