#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER 80


int **get_grid_from_file_separator(char *fname, int width, int height, char *separator) {
        FILE *fr = NULL;
        fr = fopen(fname, "rt");
        if (!fr) {
                return NULL;
        }
        
        int **grid;

        grid = (int **) malloc(height * sizeof(int*));
        for (int row = 0; row < height; ++row) {
                grid[row] = (int *) malloc(width * sizeof(int));
                for (int col = 0; col < width; ++col) {
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

                if (strlen(separator)) {
                        col = 0;
                        rest = line;
                        for (token = strtok_r(line, separator, &rest); token; token = strtok_r(NULL, separator, &rest)) {
                                grid[row][col] = atoi(token);
                                col++;
                        }
                } else {
                        for (col = 0; col < strlen(line); ++col) {
                                grid[row][col] = line[col] - 48;
                        }
                }
                row++;
        }
        return grid;
}


/**
 * Given a 2D array and a file, populate the array with the numbers
 * from the file, reading rows separated by newlines and columns
 * separated by spaces.
 */
int **get_grid_from_file(char *fname, int width, int height) {
        return get_grid_from_file_separator(fname, width, height, " ");
}
