import java.math.BigInteger;

import fraction.BigFraction;


public class Problem65 {
	public static void main(String[] args) {
		BigFraction e = eApprox(100);
		int total = 0;
		for(char ch : e.num.toString().toCharArray()) {
			total += Character.getNumericValue(ch);
		}
		System.out.println(total);
	}

	public static int contFracValue(int pos) {
		if (pos == 1) {
			return 2;
		} else if (pos % 3 == 0) {
			return (pos / 3) * 2;
		} else {
			return 1;
		}
	}

	public static BigFraction eApprox(int pos) {
		BigFraction frac = new BigFraction(contFracValue(pos), 1);
		
		while(pos > 1) {
			pos -= 1;
			frac = frac.inverse();
			frac = frac.add(new BigFraction(contFracValue(pos), 1));
		}
		return frac;
	}
}
