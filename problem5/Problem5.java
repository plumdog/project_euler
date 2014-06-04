public class Problem5 {
	public static void main(String[] args) {
		System.out.println(smallest_divisible(20));
	}

	public static int smallest_divisible(int by_all_up_to) {
		int val = 0;

		while(true) {
			++val;
			if(divisible_by_all_up_to(val, by_all_up_to)) {
				return val;
			}
		}
	}

	public static boolean divisible_by_all_up_to(int val, int by_all_up_to) {
		for(int i = 2; i < by_all_up_to; ++i) {
			if(val % i != 0) {
				return false;
			}
		}

		return true;
	}
}
