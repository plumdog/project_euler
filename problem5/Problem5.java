public class Problem5 {
	public static void main(String[] args) {
		System.out.println(smallestDivisible(20));
	}

	public static int smallestDivisible(int byAllUpTo) {
		int val = 0;
		int step = stepSize(byAllUpTo);

		while(true) {
			val += step;
			if(divisibleByAllUpTo(val, byAllUpTo)) {
				return val;
			}
		}
	}

	public static boolean divisibleByAllUpTo(int val, int byAllUpTo) {
		for(int i = 2; i < byAllUpTo; ++i) {
			if(val % i != 0) {
				return false;
			}
		}

		return true;
	}

	public static int stepSize(int byAllUpTo) {
		int step = 1;
		for(int i = 2; i <= byAllUpTo; ++i) {
			if(isPrime(i)) {
				step *= i;
			}
		}

		return step;
	}

	public static boolean isPrime(int val) {
		int upto = (int) Math.round(Math.sqrt(val));

		for(int i = 2; i <= upto; ++i) {
			if(val % i == 0) {
				return false;
			}
		}

		return true;
	}
}
