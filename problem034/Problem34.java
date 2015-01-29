/*
 * A number with n digits has minimum value of 10^(n-1), and a maximum
 * sumOfFactorialOfDigits values of 9!*n. As 10^(n-1) is exponential
 * whereas 9!*n is linear, once the exponential is larger, it will
 * stay larger forever. Wolfram Alpha tells u that these values are
 * equal at approx 7.43. Therefore, we need to check for all values of
 * n upto and including 8.
 */

public class Problem34 {
	protected static int[] factorials = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};

	public static int factorial(int num) {
		return factorials[num];
	}

	public static int sumOfFactorialOfDigits(int num) {
		char[] chars = Integer.toString(num).toCharArray();
		int sum = 0;
		for(char ch : chars) {
			sum += factorial(Character.getNumericValue(ch));
		}

		return sum;
	}

	public static boolean isCurious(int num) {
		return sumOfFactorialOfDigits(num) == num;
	}

	public static void main(String[] args) {
		int sum = 0;
		int max = 10000000; // 10^7
		for(int i = 3; i < max; ++i) {
			if(isCurious(i)) {
				sum += i;
			}
		}

		System.out.println(sum);
	}
}

