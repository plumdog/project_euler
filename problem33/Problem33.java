import fraction.Fraction;

class FakeCancelFraction extends Fraction{
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
}


public class Problem33 {
	public static void main(String[] args) {
		Fraction fr = null;
		Fraction canFr = null;
		Fraction prodFr = new FakeCancelFraction(1, 1);

		for(int num = 11; num <= 99; ++num) {
			for(int den = num + 1; den <= 98; ++den) {
				fr = new FakeCancelFraction(num, den);
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
