/*
 * We only need to check up to 999999. We can convince ourselves that
 * numbers with seven or more digits cannot produce large enough
 * values when the digits are raised to 5th power. With seven digits,
 * the largest value possible is 7*9^5 = 413343, which cannot be large
 * enough as it does not have seven digits.
 */

public class Problem31 {
	public static void main(String[] args) {
		int value = 0;
		int count = 0;
		for(int p200 = 0; p200 <= 1; ++p200) {
			for(int p100 = 0; p100 <= 2; ++p100) {
				for(int p50 = 0; p50 <= 4; ++p50) {
					for(int p20 = 0; p20 <= 10; ++p20) {
						for(int p10 = 0; p10 <= 20; ++p10) {
							for(int p5 = 0; p5 <= 40; ++p5) {
								for(int p2 = 0; p2 <= 100; ++p2) {
									value = p200 * 200 + p100 * 100 + p50 * 50 + p20 * 20 + p10 * 10 + p5 * 5 + p2 * 2;
									if(value >= 0 && value <= 200) {
										// then we can do the rest with 1ps
										++count;
									}
								}
							}
						}
					}
				}
			}
		}

		System.out.println(count);
	}
}
