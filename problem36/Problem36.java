import java.util.Hashtable;
import java.util.Arrays;

public class Problem36 {
	public static void main(String[] args) {
		int total = 0;
		int max = 1000000;

		for(int i = 1; i < max; ++i) {
			if(isPalindrome(Integer.toString(i, 10)) && isPalindrome(Integer.toString(i, 2))) {
				total += i;
			}
		}

		System.out.println(total);
	}

	public static boolean isPalindrome(String str) {
		int l = str.length();
		int halfl = l / 2;
		for(int i = 0; i < halfl; ++i) {
			if(str.charAt(i) != str.charAt(l - i - 1)) {
				return false;
			}
		}

		return true;
	}
}
