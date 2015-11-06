#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUMLEN 1000
#define BUFFER NUMLEN+1
#define RUNLEN 13
#define t_big long long


t_big max_run_from(int digits[NUMLEN], int start, int runlen) {
        int end = start + runlen;
        if (end >= NUMLEN) {
                return -1;
        }

        t_big product = 1;
        for(int i = start; i < end; ++i) {
                product *= digits[i];
        }
        return product;
}


t_big max(t_big a, t_big b) {
        return ((a > b) ? a : b);
}


int main(int argc, char *argv[]) {
        if (argc != 2) {
                printf("Expected just one filename, %d given", argc - 1);
        }
        FILE *fr;
        char *fname = argv[1];

        fr = fopen(fname, "rt");
        char buffer[BUFFER];
        fgets(buffer, BUFFER, fr);
        int digits[NUMLEN];
        for (int i = 0; i < NUMLEN; ++i) {
                digits[i] = (int) (buffer[i] - 48);
        }

        t_big max_product = -1;

        for (int j = 0; j < NUMLEN; ++j) {
                max_product = max(
                        max_product,
                        max_run_from(digits, j, RUNLEN));
                
        }

        printf("%lld\n", max_product);
}
