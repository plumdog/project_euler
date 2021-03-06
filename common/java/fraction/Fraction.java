package fraction;

public class Fraction implements Comparable<Fraction> {
	public final int num, den;
	public Fraction(int num, int den) {
		this.num = num;
		this.den = den;
	}

	public int num() {
		return num;
	}

	public int den() {
		return den;
	}

	@Override
	public boolean equals(Object other) {
		if(other instanceof Fraction) {
			Fraction otherFr = (Fraction) other;
			return compareTo(otherFr) == 0;
		}

		return false;
	}

	public Fraction lowestTerms() {
		int newNum = this.num;
		int newDen = this.den;

		int trial = 2;
		while(true) {
			if((newNum % trial == 0) && (newDen % trial == 0)) {
				newNum /= trial;
				newDen /= trial;
				trial = 2;
				continue;
			}

			if (trial == 2) {
				trial = 3;
			} else {
				trial += 2;
			}

			if ((trial > newNum) || (trial > newDen)) {
				break;
			}
		}

		return new Fraction(newNum, newDen);
	}

	/*
	 * a/b * c/d = ac/bd
	 */
	public Fraction times(Fraction other) {
		return new Fraction(this.num * other.num, this.den * other.den);
	}

	/*
	 * a/b + c/d = (ad + cb) / bd
	 */
	public Fraction add(Fraction other) {
		return new Fraction(this.num * other.den + other.num * this.den, this.den * other.den);
	}

	public Fraction subtract(Fraction other) {
		return add(other.negative());
	}

	public Fraction negative() {
		return new Fraction(-num, den);
	}

	public Fraction inverse() {
		return new Fraction(den, num);
	}

	public String toString() {
		return num + "/" + den;
	}

	public int compareTo(Fraction f) {
		int v1 = this.num * f.den;
		int v2 = f.num * this.den;
		if(v1 == v2)
			return 0;
		return (v1 > v2) ? 1 : -1;
	}

	@Override
	public int hashCode() {
		return new Double((double) num / den).hashCode();
	}
}
