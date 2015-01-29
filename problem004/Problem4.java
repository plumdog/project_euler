public class Problem4 {
	public static void main(String[] args) {
		int min = 100, max = 999;
		int largest = 0;
		int prod;
		String s;
		for(int i = min; i <= max; ++i) {
			for(int j = i; j <= max; ++j) {
				prod = i * j;
				s = Integer.toString(prod);
				if(is_palindrome(s)) {
					if(prod > largest) {
						largest = prod;
					}
				}
			}
		}

		System.out.println(largest);
	}

	public static boolean is_palindrome(String s) {
		int len = s.length();
		for(int i = 0; i < len; ++i) {
			if(s.charAt(i) != s.charAt(len - i - 1)) {
				return false;
			}
		}

		return true;
	}
}
