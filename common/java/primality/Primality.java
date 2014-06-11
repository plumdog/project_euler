package primality;

public class Primality {

	public static boolean isPrime(int val) {
		if(val == 2) {
			return true;
		}

		if((val < 2) || (val % 2 == 0)) {
			return false;
		}

		int upto = (int) Math.round(Math.sqrt(val));

		for(int i = 3; i <= upto; i+=2) {
			if(val % i == 0) {
				return false;
			}
		}

		return true;
	}
}
