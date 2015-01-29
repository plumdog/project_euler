import java.util.Hashtable;
import java.util.Arrays;

import primality.Primality;

public class Problem37 {
	public static void main(String[] args) {
		int count = 0;
		int total = 0;

		for(int i = 11; ; i+=2) {
			if(truncatablePrime(i)) {
				count += 1;
				total += i;

				if(count == 11) {
					break;
				}
			}
		}

		System.out.println(total);
	}

	public static boolean truncatablePrime(int num) {
		if(num < 10) {
			return false;
		}

		String str = Integer.toString(num);
		int strlen = str.length();
		String lstr = null;
		String rstr = null;
		for(int i = 1; i < strlen; ++i) {
			lstr = str.substring(0, i);
			rstr = str.substring(strlen - i);

			if(!Primality.isPrime(Integer.parseInt(lstr))) {
				return false;
			}
			if(!Primality.isPrime(Integer.parseInt(rstr))) {
				return false;
			}
		}

		// If all trucations where prime, then check if the numbers
		// itself is prime.
		return Primality.isPrime(num);
	}
}
