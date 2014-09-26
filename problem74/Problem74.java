import java.util.ArrayList;


public class Problem74 {
	public static void main(String[] args) {
		int count = 0;
		for(int i = 0; i < 1000000; ++i) {
			if(chainLength(i) == 60) {
				++count;
			}
		}

		System.out.println(count);
	}

	public static int chainLength(int num) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		list.add(num);
		Integer nextStep = step(num);
		int index = 0;

		while(true) {
			index = list.indexOf(nextStep);
			if(index == -1) {
				list.add(nextStep);
				nextStep = step(nextStep);
			} else {
				return list.size();
			}
		}
	}

	public static int step(int num) {
		int total = 0;
		while(true) {
			total += factorial(num % 10);
			num /= 10;
			if(num == 0)
				return total;
		}
	}

	public static int factorial(int num) {
		if((num == 0) || (num == 1))
			return 1;
		return num * factorial(num - 1);
	}
}
