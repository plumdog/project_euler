class Fraction {
	public final int num, den;
	public Fraction(int num, int den) {
		this.num = num;
		this.den = den;
	}

	public Fraction fakeCancel() {
		char[] numChars = Integer.toString(num).toCharArray();
		char[] denChars = Integer.toString(den).toCharArray();

		for(int numi = 0; numi <= 1; ++numi) {
			for(int deni = 0; deni <= 1; ++deni) {
				if((numChars[numi] == denChars[deni]) && numChars[numi] != '0') {
					return new Fraction(Character.getNumericValue(numChars[1-numi]),
										Character.getNumericValue(denChars[1-deni]));
				}
			}
		}

		return null;
	}

	public boolean isEqual(Fraction other) {
		return this.num * other.den == other.num * this.den;
	}

	public Fraction lowestTerms() {
		int newNum = this.num;
		int newDen = this.den;

		for(int i = this.den - 1; i >= 2; --i) {
			if((newNum % i == 0) && (newDen % i == 0)) {
				newNum /= i;
				newDen /= i;
				break;
			}
		}

		return new Fraction(newNum, newDen);
	}

	public Fraction times(Fraction other) {
		return new Fraction(this.num * other.num, this.den * other.den);
	}
}


public class Problem33 {
	public static void main(String[] args) {
		Fraction fr = null;
		Fraction canFr = null;
		Fraction prodFr = new Fraction(1, 1);

		for(int num = 11; num <= 99; ++num) {
			for(int den = num + 1; den <= 98; ++den) {
				fr = new Fraction(num, den);
				canFr = fr.fakeCancel();
				if((canFr != null) && fr.isEqual(canFr)) {
					prodFr = prodFr.times(fr);
				}
			}
		}

		prodFr = prodFr.lowestTerms();
		System.out.println(prodFr.den);
	}
}
