public class Problem27 {
	public static void main(String[] args) {
		int lim = 999;
		int max = 0;
		int count = 0;
		int maxa = 0, maxb = 0;

		for(int a = -lim; a <= lim; ++a) {
			for(int b = -lim; b <= lim; ++b) {
				count = polyPrimesCount(a, b);
				if(count > max) {
					max = count;
					maxa = a;
					maxb = b;
				}
			}
		}

		System.out.println(maxa * maxb);
	}

	/* Returns the number of consecutive prime values from n^2 + an +
	 * b for values of n starting at 0. */
	public static int polyPrimesCount(int a, int b) {
		int polyv;
		for(int n = 0; n < 80; ++n) {
			polyv = polyValue(a, b, n);
			if(!isPrime(polyv)) {
				return n;
			}
		}

		throw new IllegalArgumentException();
	}

	public static int polyValue(int a, int b, int n) {
		return n*n + b*n + a;
	}

	public static boolean isPrime(int val) {
		if(val <= 0) {
			return false;
		}

		int upto = (int) Math.round(Math.sqrt(val));
		for(int i = 2; i <= upto; ++i) {
			if(val % i == 0) {
				return false;
			}
		}
		return true;
	}
}
