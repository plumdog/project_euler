public class Problem86 {
	public static final int target = 1000000;
	
	public static void main(String[] args) {
		int m = 0;
		int total = 0;
		while(true) {
			++m;

			// fix w at m, trial values for d and h, where h <= d
			// therefore h <= d <= w
			for(int d = 1; d <= m; ++d) {
				for(int h = 1; h <= d; ++h) {
					if(shortestPathIsInt(h, d, m)) {
						++total;
					}
				}
			}

			if(total > target) {
				System.out.println(m);
				return;
			}
			
		}
	}

	public static boolean shortestPathIsInt(int h, int d, int w) {
		if(h > d) {
			throw new IllegalArgumentException("h must be <= d");
		} else if(d > w) {
			throw new IllegalArgumentException("d must be <= w");
		}

		// we know that h <= d <= w we find the shortest route
		// be combining two of the sides (imagine folding out
		// the box along the side that we move over). We want
		// to combine the two smallest sides.
		int side1 = h + d;
		int side2 = w;
		return isSquare(side1*side1 + side2*side2);
	}

	public static boolean isSquare(int num) {
		int sqrt = (int) Math.sqrt(num);
		return sqrt*sqrt == num;
	}
}
