#include <stdio.h>
#include <string.h>
#include <inttypes.h>


int strtoi(char *token) {
	return strtoimax(token, NULL, 10);
}

typedef struct Point {
	int x, y;
} Point;


typedef struct Triangle {
	Point p1, p2, p3;
} Triangle;


int sign(Point p1, Point p2, Point p3) {
	return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
}


int triangle_contains_origin(Triangle triangle) {
	int s1, s2, s3;
	Point origin = (Point) {0, 0};

	s1 = (sign(origin, triangle.p1, triangle.p2) < 0);
	s2 = (sign(origin, triangle.p2, triangle.p3) < 0);
	s3 = (sign(origin, triangle.p3, triangle.p1) < 0);

	return ((s1 == s2) && (s2 == s3));
}


int main(int argc, char *argv[]) {
	if(argc != 2) {
		printf("Expected just one filename, %d given", argc - 1);
		return 1;
	}

	FILE *fr;
	char line[80];
	char *fname = argv[1];

	Triangle triangle;
	int num_contain_origin = 0;

	fr = fopen (fname, "rt");
	while(fgets(line, 80, fr) != NULL) {
		triangle = (Triangle) {
			(Point) {
				strtoi(strtok(line, ",")),
				strtoi(strtok(NULL, ","))},
			(Point) {
				strtoi(strtok(NULL, ",")),
				strtoi(strtok(NULL, ","))},
			(Point) {
				strtoi(strtok(NULL, ",")),
				strtoi(strtok(NULL, ","))}};
		num_contain_origin += triangle_contains_origin(triangle);
	}

	printf("%d\n", num_contain_origin);

	return 0;
}
