public class Problem21 {
	public static void main(String[] args) {
		int total = 0, sum;
		for(int i = 0; i < 10000; ++i) {
			sum = sum_proper_divisors(i);
			if((sum_proper_divisors(sum) == i) && (i != sum)) {
				total += i;
			}
		}

		System.out.println(Integer.toString(total));
	}

	public static int sum_proper_divisors(int num) {
		int sum = 1; // include 1
		for(int i = 2; i <= num / 2; ++i) {
			if(num % i == 0) {
				sum += i;
			}
		}

		return sum;
	}
}
