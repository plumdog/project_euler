import primality.Primality;


public class Problem58 {
	public static void main(String[] args) {
		int n = 0;
		Result res = null;

		while(true) {
			res = fracPrimeOnDiagonals(res, n);
			if((n > 0) && (res.frac() < 0.1)) {
				System.out.println(2*n + 1);
				break;
			}

			n++;
		}
	}

	public static Result fracPrimeOnDiagonals(Result prev, int n) {
		if(n == 0) {
			return new Result(0, 1);
		}

		Result res = prev.clone();
		n = n + 1;

		int x = 4*n*n - 10*n + 7;
		int y = 4*n*n -  8*n + 5;
		int z = 4*n*n -  6*n + 3;
		int w = 4*n*n -  4*n + 1;

		if(Primality.isPrime(x)) {
			res.primes++;
		}
		if(Primality.isPrime(y)) {
			res.primes++;
		}
		if(Primality.isPrime(z)) {
			res.primes++;
		}
		if(Primality.isPrime(w)) {
			res.primes++;
		}
		res.total += 4;

		return res;
	}
}

class Result {
	int primes;
	int total;

	public Result(int primes, int total) {
		this.primes = primes;
		this.total = total;
	}

	public String toString() {
		return primes + "/" + total;
	}

	public Result clone() {
		return new Result(primes, total);
	}

	public double frac() {
		return ((double) primes) / total;
	}
}
