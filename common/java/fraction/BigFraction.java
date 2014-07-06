package fraction;

import java.math.BigInteger;

public class BigFraction {
	public static final BigFraction ONE = new BigFraction(new BigInteger("1"), new BigInteger("1"));

	public final BigInteger num, den;
	
	public BigFraction(BigInteger num, BigInteger den) {
		this.num = num;
		this.den = den;
	}

	public BigInteger num() {
		return num;
	}

	public BigInteger den() {
		return den;
	}

	public boolean isEqual(BigFraction other) {
		return this.num.multiply(other.den).equals(other.num.multiply(this.den));
	}

	public BigFraction lowestTerms() {
		BigInteger newNum = this.num;
		BigInteger newDen = this.den;

		BigInteger trial = new BigInteger("2");
		while(true) {
			if((newNum.mod(trial).equals(0)) && (newDen.mod(trial).equals(0))) {
				newNum = newNum.divide(trial);
				newDen = newDen.divide(trial);
				trial = new BigInteger("2");
				continue;
			}

			if (trial.equals(new BigInteger("2"))) {
				trial = new BigInteger("3");
			} else {
				trial = trial.add(new BigInteger("2"));
			}

			if ((trial.compareTo(newNum) > 0) || (trial.compareTo(newDen) > 0)) {
				break;
			}
		}

		return new BigFraction(newNum, newDen);
	}

	/*
	 * a/b * c/d = ac/bd
	 */
	public BigFraction times(BigFraction other) {
		return new BigFraction(this.num.multiply(other.num), this.den.multiply(other.den));
	}

	/*
	 * a/b + c/d = (ad + cb) / bd
	 */
	public BigFraction add(BigFraction other) {
		return new BigFraction(this.num.multiply(other.den).add(other.num.multiply(this.den)), this.den.multiply(other.den));
	}

	public BigFraction subtract(BigFraction other) {
		return add(other.negative());
	}

	public BigFraction negative() {
		return new BigFraction(num.negate(), den);
	}

	public BigFraction inverse() {
		return new BigFraction(den, num);
	}

	public String toString() {
		return num + "/" + den;
	}
}
