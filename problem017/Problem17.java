public class Problem17 {
	public static void main(String[] args) {
		int count = 0;
		int max = 1000;
		for(int i = 1; i <= max; ++i) {
			count += intToWords(i).length();
		}

		System.out.println(Integer.toString(count));
	}

	public static String intToWords(int num) {
		if(num <= 19) {
			switch(num) {
			case 0: return "";
			case 1: return "one";
			case 2: return "two";
			case 3: return "three";
			case 4: return "four";
			case 5: return "five";
			case 6: return "six";
			case 7: return "seven";
			case 8: return "eight";
			case 9: return "nine";
			case 10: return "ten";
			case 11: return "eleven";
			case 12: return "twelve";
			case 13: return "thirteen";
			case 14: return "fourteen";
			case 15: return "fifteen";
			case 16: return "sixteen";
			case 17: return "seventeen";
			case 18: return "eighteen";
			case 19: return "nineteen";
			}
		} else if(num <= 99) {
			int tens = num / 10;
			int units = num % 10;
			switch(tens) {
			case 2: return "twenty" + intToWords(units);
			case 3: return "thirty" + intToWords(units);
			case 4: return "forty" + intToWords(units);
			case 5: return "fifty" + intToWords(units);
			case 6: return "sixty" + intToWords(units);
			case 7: return "seventy" + intToWords(units);
			case 8: return "eighty" + intToWords(units);
			case 9: return "ninety" + intToWords(units);
			}
		} else if(num <= 999) {
			int hundreds = num / 100;
			int rest = num % 100;
			if(rest > 0) {
				return intToWords(hundreds) + "hundredand" + intToWords(rest);
			} else {
				return intToWords(hundreds) + "hundred";
			}
		} else if(num == 1000) {
			return "onethousand";
		}

		throw new IllegalArgumentException();
	}
}
