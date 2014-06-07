#include <stdio.h>

FILE *fr;

int chscore(char ch) {
	return (int) ch - 64;
}

int namescore(char *line) {
	int score = 0;
	char ch;
	while(*line != '\n') {
		ch = *line++;
		score += chscore(ch);
	}

	return score;
}



int main(int argc, char *argv[]) {
	if(argc != 2) {
		printf("Expected just one filename, %d given", argc - 1);
		return 1;
	}

	char line[80];
	char *fname = argv[1];
	int total = 0;
	int linenum = 1;

	fr = fopen (fname, "rt");
	while(fgets(line, 80, fr) != NULL) {
		total += namescore(line) * linenum;
		++linenum;
	}

	printf("%d\n", total);

	return 0;
}


