package fraction;

class Fraction {
	public final int num, den;
	public Fraction(int num, int den) {
		this.num = num;
		this.den = den;
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
