import java.util.HashSet;

public class Problem23 {
	public static HashSet<Integer> abundants = new HashSet<Integer>();

	public static void buildAbundants(int max) {
		for(int i = 1; i <= max; ++i) {
			if(isAbundant(i)) {
				abundants.add(i);
			}
		}
	}
	
	public static void main(String[] args) {
		int max = 28123;
		buildAbundants(max);

		int total = 0;
		for(int j = 1; j <= max; ++j) {
			if(!sumOfTwoAbundants(j)) {
				total += j;
			}
		}

		System.out.println(total);
	}

	public static boolean sumOfTwoAbundants(int num) {
		for(int ab : abundants) {
			if(abundants.contains(num - ab)) {
				return true;
			}
		}

		return false;
	}

	public static boolean isAbundant(int num) {
		int sum = 0;
		for(int i = 1; i <= num / 2; ++i) {
			if(num % i == 0) {
				sum += i;
			}
		}

		return sum > num;
	}
}
