#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER 80

/**
 * Given a 2D array and a file, populate the array with the numbers
 * from the file, reading rows separated by newlines and columns
 * separated by spaces.
 */
int **get_grid_from_file(FILE *fr, int size) {
        if (!fr) {
                return NULL;
        }
        
        int **grid;

        grid = (int **) malloc(size * sizeof(int*));
        for (int row = 0; row < size; ++row) {
                grid[row] = (int *) malloc(size * sizeof(int));
                for (int col = 0; col < size; ++col) {
                        grid[row][col] = 0;
                }
        }

        char line[BUFFER];
        int value;
        char *num;
        char *token;
        char *rest;

        int row = 0;
        int col = 0;

        while(fgets(line, BUFFER, fr) != NULL) {
                // Replace newline terminated string with null
                // terminated string.
                char *pos;
                if ((pos = strchr(line, '\n')) != NULL) {
                        *pos = '\0';
                }
                col = 0;
                rest = line;
                for (token = strtok_r(line, " ", &rest); token; token = strtok_r(NULL, " ", &rest)) {
                        grid[row][col] = atoi(token);
                        col++;
                }
                row++;
        }
        return grid;
}
