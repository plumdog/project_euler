import fraction.Fraction;
import java.util.Set;
import java.util.TreeSet;


public class Problem71 {
	public static void main(String[] args) {
		int max_d = 1000000;
		Fraction target = new Fraction(3, 7);
		Fraction trial = null;
		Fraction best = null;

		for(int d = 1; d <= max_d; ++d) {
			trial = null;

			int upper = d;
			int lower = 0;
			int gap = upper - lower;

			while(gap > 1) {
				if(gap <= 2) {
					trial = linearCheck(lower, upper, d, target);
					break;
				} else {
					trial = new Fraction((upper + lower)/2, d);
					if(trial.compareTo(target) > 0) {
						upper -= gap / 2;
					} else {
						lower += gap / 2;
					}

					gap = upper - lower;
				}
			}

			if((best == null) || ((trial != null) && (trial.compareTo(best) > 0))) {
				best = trial;
			}
			
		}

		System.out.println(best.lowestTerms().num);
	}

	public static Fraction linearCheck(int lower, int upper, int d, Fraction target) {
		Fraction trial = null;

		for(int n = upper; n >= lower; --n) {
			trial = new Fraction(n, d);
			if(trial.compareTo(target) < 0) {
				return trial;
			}
		}

		return null;
	}
}
