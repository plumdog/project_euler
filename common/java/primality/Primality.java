package primality;

public class Primality {

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
