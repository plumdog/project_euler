import java.util.HashSet;

public class Problem23 {
	public static HashSet<Integer> getAbundants(int max) {
		HashSet<Integer> abundants = new HashSet<Integer>();
		for(int i = 1; i <= max; ++i) {
			if(isAbundant(i)) {
				abundants.add(i);
			}
		}
		return abundants;
	}
	
	public static void main(String[] args) {
		int max = 28123;
		HashSet<Integer> abundants = getAbundants(max);

		int total = 0;
		for(int j = 1; j <= max; ++j) {
			if(!sumOfTwoAbundants(j, abundants)) {
				total += j;
			}
		}

		System.out.println(total);
	}

	public static boolean sumOfTwoAbundants(int num, HashSet<Integer> abundants) {
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
