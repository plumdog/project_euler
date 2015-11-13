#include <stdio.h>

#include <get_matrix.h>

// 100 * 10^50 = 52
#define DIGITS 52
#define REQDIGITS 10
int const NUMLEN = 50;
int const NUMS = 100;

int main(int argc, char *argv[]) {
        if (argc != 2) {
                printf("Expected just one filename, %d given", argc - 1);
        }
        int **nums;
        nums = get_grid_from_file_separator(argv[1], NUMLEN, NUMS, "");

        int sum[DIGITS] = {0};
        long digit_total = 0;
        long carry = 0;

        for (int i = 0; i < DIGITS; ++i) {
                for (int j = 0; j < NUMS; ++j) {
                        int num = nums[j][NUMLEN - i - 1];
                        digit_total += num;
                }
                sum[i] = digit_total % 10;
                // Carry to the next digit
                digit_total = digit_total / 10;
        }

        // TODO: check that any remaining carry is correctly applied

        int start = -1;
        for (int i = DIGITS - 1; i >= 0; --i) {
                if (sum[i]) {
                        start = i;
                        break;
                }
        }

        for (int i = start; i > start - REQDIGITS; --i) {
                printf("%d", sum[i]);
        }
        printf("\n");
}
