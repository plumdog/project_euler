import java.util.Hashtable;
import java.util.Arrays;

import primality.Primality;

public class Problem35 {
	public static void main(String[] args) {
		int max = 1000000;
		int count = 1; // include 2
		for(int trial = 3; trial < max; trial+=2) {
			if(allRotationPrime(trial)) {
				++count;
			}
		}

		System.out.println(count);
	}

	public static boolean allRotationPrime(int trial) {
		if(!isPrimeHash(trial)) {
			return false;
		}

		char[] origDigits = toCharArray(trial);
		char[] digits = rotate(origDigits);

		while(!Arrays.equals(digits, origDigits)) {
			if(!isPrimeHash(fromCharArray(digits))) {
				return false;
			}

			digits = rotate(digits);
		}

		return true;
	}

	public static char[] toCharArray(int num) {
		return Integer.toString(num).toCharArray();
	}

	public static int fromCharArray(char[] digits) {
		return Integer.parseInt(new String(digits));
	}

	public static char[] rotate(char[] digits) {
		if(digits.length == 1) {
			return digits;
		}

		char[] newDigits = new char[digits.length];

		// Store the first char, then shuffle down all further
		// digits. Then add the first one at the end
		int len = digits.length;
		char first = digits[0];
		for(int i = 1; i < len; ++i) {
			newDigits[i-1] = digits[i];
		}

		newDigits[len - 1] = first;
		return newDigits;
	}

	public static Hashtable <Integer, Boolean> primeHashtable = new Hashtable<Integer, Boolean>();

	public static boolean isPrimeHash(int val) {
		Boolean out = primeHashtable.get(val);
		if(out == null) {
			out = Primality.isPrime(val);
			primeHashtable.put(val, out);
		}

		return out;
	}
}
