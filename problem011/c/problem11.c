#include <stdio.h>

#include <get_matrix.h>

#define RUNSIZE 4

int const SIZE = 20;

/**
 * In the given 2D array of integers, a starting row and col, and a
 * row and col step, calculate the product of the numbers found by
 * starting from the starting row and col, and making RUNSIZE steps.
 */
int run(int **grid, int row, int col, int row_step, int col_step) {
        int total = 1;

        for(int i = 0; i < RUNSIZE; ++i) {
                if ((row >= SIZE) || (col >= SIZE) || (row < 0) || (col < 0)) {
                        return 0;
                }
                total *= grid[row][col];
                row += row_step;
                col += col_step;
        }
        return total;
}


int max(int a, int b) {
        if (a > b) {
                return a;
        }
        return b;
}


int max_of_nums(int nums[RUNSIZE]) {
        int max_num = nums[0];
        for (int i = 1; i < RUNSIZE; ++i) {
                max_num = max(max_num, nums[i]);
        }
        return max_num;
}


int max_run_from_pos(int **grid, int row, int col) {
        int nums[RUNSIZE] = {
                run(grid, row, col, 0, 1),  // West
                run(grid, row, col, 1, 0),  // South
                run(grid, row, col, 1, 1),  // South-West
                run(grid, row, col, 1, -1)  // South-East
        };
        return max_of_nums(nums);
}


int max_run(int **grid) {
        if (!grid) {
                return -1;
        }

        int max_product = 0;
        for (int col = 0; col < SIZE; ++col) {
                for (int row = 0; row < SIZE; ++row) {
                        max_product = max(max_run_from_pos(grid, row, col), max_product);
                }
        }
        return max_product;
}


int main(int argc, char *argv[]) {
        if (argc != 2) {
                printf("Expected just one filename, %d given", argc - 1);
        }
        FILE *fr = NULL;
        char *fname = argv[1];

        int **nums;
        fr = fopen(fname, "rt");
        nums = get_grid_from_file(fr, SIZE);

        printf("%d\n", max_run(nums));
}
