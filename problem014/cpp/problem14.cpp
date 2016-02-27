#include <iostream>
#include <unordered_map>


typedef std::unordered_map<long, long> Map;


long collatz(long n) {
    if (n % 2 == 0)
        return n / 2;
    return 3*n + 1;
}

long get_chain_length(long start, Map &map) {
    if (start == 1)
        return 1;
    if (map.count(start) > 0)
        return map[start];
    // Assign to the cache and return.
    return map[start] = 1 + get_chain_length(collatz(start), map);
}

 
int main() {
    int upto = 1000000;
    int maxkey, maxval = 0;
    long chainlen;
    Map map;
    for (int i = 1; i <= upto; ++i) {
        chainlen = get_chain_length(i, map);
        if (chainlen > maxval) {
            maxkey = i;
            maxval = chainlen;
        }
    }

    std::cout << maxkey << std::endl;
}
