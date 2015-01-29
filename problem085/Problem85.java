public class Problem85 {
	public static final int target = 2000000;

	public static void main(String[] args) {
		long trial = 0;
		long bestGuess = -1;
		int bestGuessX = 0;
		int bestGuessY = 0;

		int targetOver = (int) (target * 1.1);

		for(int x = 1; ; x++) {
			// if even at the first trial, we are far past
			// the target, then x is too large to give
			// possible improvements
			if(countRectangles(x, 1) > targetOver) {
				break;
			}

			for(int y = 1; y <= x ; y++) {
				trial = countRectangles(x, y);
				if(Math.abs(target - trial) < Math.abs(target - bestGuess)) {
					// if the trial number is
					// better than the current
					// best guess, then update it.

					bestGuess = trial;
					bestGuessX = x;
					bestGuessY = y;
				}

				// if we our trial value is far above
				// the target, then there is nothing
				// to be gained by increasing y, so
				// break and start a new x
				if(trial > targetOver) {
					break;
				}
			}
		}

		System.out.println(bestGuessX * bestGuessY);
	}

	public static long countRectangles(int x, int y) {
		// of width one, height one, there are x*y
		// of width one, height two, there are x*(y-1)
		// of width one, height three, there are x*(y-2)
		// ...
		// of width one, height n, there are x*(y-n+1)

		// of width two, height one, there are (x-1)*y
		// of width three, height one, there are (x-2)*y

		// of width n, height m, there are (x-n+1)*(y-m+1)
		long total = 0;
		for(int w = 1; w <= x; w++) {
			for(int h = 1; h <= y; h++) {
				total += (x-w+1)*(y-h+1);
			}
		}

		return total;
	}
}
