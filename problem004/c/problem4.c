#include <stdio.h>
#include <math.h>
#include <string.h>


int is_palindrome(int num) {
        char str[10];
        sprintf(str, "%d", num);
        int length = strlen(str);
        // If our string is n characters long, we need to check that
        // str[0] == str[n-1], str[1] == str[n-1]...
        for (int i = 0; i < (length / 2); ++i) {
                if (str[i] != str[length - i - 1]) {
                        return 0;
                }
        }
        return 1;
}


int largest_palindromic_product(int min, int max) {
        int largest = 0;
        int product;
        for (int i = min; i <= max; ++i) {
                for (int j = min; j <= max; ++j) {
                        product = i * j;
                        if (is_palindrome(product) && (product > largest)) {
                                largest = product;
                        }
                }
        }
        return largest;
}


int main() {
        printf("%d\n", largest_palindromic_product(100, 999));
	return 0;
}
