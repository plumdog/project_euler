/*
 * We only need to check up to 999999. We can convince ourselves that
 * numbers with seven or more digits cannot produce large enough
 * values when the digits are raised to 5th power. With seven digits,
 * the largest value possible is 7*9^5 = 413343, which cannot be large
 * enough as it does not have seven digits.
 */

public class Problem30 {
	public static void main(String[] args) {
		int max = 999999;
		int sum = 0;
		for(int i = 2; i <= max; ++i) {
			if(sumFifthPowerOfDigits(i) == i) {
				sum += i;
			}
		}

		System.out.println(sum);
	}

	public static int fifthPower(int num) {
		return num*num*num*num*num;
	}

	public static int sumFifthPowerOfDigits(int num) {
		String digits = Integer.toString(num);
		int total = 0;
		for(int i = 0; i < digits.length(); ++i) {
			total += fifthPower(Character.getNumericValue(digits.charAt(i)));
		}

		return total;
	}
}
