import java.math.BigInteger;

public class Problem55 {
	public static void main(String[] args) {
		System.out.println(countLychrel(10000, 50));
	}

	public static int countLychrel(int upto, int maxIterations) {
		int count = 0;
		for(int i = 1; i < upto; ++i) {
			if (isLychrel(new BigInteger(Integer.toString(i)), maxIterations)) {
				count++;
			}
		}

		return count;
	}

	public static boolean isLychrel(BigInteger num, int maxIterations) {
		for(int i = 1; i < maxIterations; ++i) {
			num = num.add(reverseBigInteger(num));
			if (isPalindrome(num.toString())) {
				return false;
			}
		}

		return true;
	}

	public static String reverseString(String s) {
		return new StringBuilder(s).reverse().toString();
	}

	public static boolean isPalindrome(String s) {
		return reverseString(s).equals(s);
	}

	public static BigInteger reverseBigInteger(BigInteger num) {
		return new BigInteger(reverseString(num.toString()));
	}
}
