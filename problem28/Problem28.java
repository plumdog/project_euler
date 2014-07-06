/*
 * This problem is actually very possible to do with pencil and paper
 * alone. The four arms of the spiral each follow a quadratic
 * progression. You can convince yourself that each sequance has a
 * "2nd difference" of 8. Some maths gives:
 *
 * a_i = (c/2)n^2 + (b0 - 3c/2)n + (a0 - b0 + c)
 * for b0 = (a1-a0) and c = second difference.
 *
 * x_i = 4n^2 - 10n + 7 (SE)
 * y_i = 4n^2 -  8n + 5 (SW)
 * z_i = 4n^2 -  6n + 3 (NW)
 * w_i = 4n^2 -  4n + 1 (NE)
 *
 * We wish to find the sum of these terms for n = 0 to 501, and then
 * subtract 3 because the 1 at the centre will have been counted 4
 * times and we only want it once.
 *
 * X_i = x_i + y_i + z_i + w_i
 *     = 16n^2 - 28n + 16
 * SUM = 16*n(n+1)(2n+1)/6 - 28*n(n+1)/2 + 16n
 *     = (8/3) * (n^2+n)(2n+1) - 14(n^2+n) + 16n
 *     = (8/3) * (2n^3 + 3n^2 + n) - 14n^2 - 14n + 16n
 *     = (16/3)n^3 + 8n^2 + (8/3)n - 14n^2 - 14n + 16n
 *     = (16/3)n^3 - 6n^2 + (14/3)n
 * ANS = [SUM for n = 501] - 3
 *     = (16/3)*501^3 - 6*501^2 + (14/3)*501 - 3
 *     = 669171001
 */

import spiral.Spiral;

public class Problem28 {
	public static void main(String[] args) {
		Spiral g = new Spiral(500);
		int total = 1; // only need to add 1 once
		for(int i = 1; i <= g.hsize; ++i) {
			total += g.get(i, i); // SE
			total += g.get(i, -i); // NE
			total += g.get(-i, -i); // NW
			total += g.get(-i, i); // SW
		}

		System.out.println(total);
	}
}
