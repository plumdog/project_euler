public class Problem1 {
	public static void main(String[] args) {
		System.out.println(divBy3Or5(1000));
	}

	public static int divBy3Or5(int upto) {
		int val = 0;
        for (int i = 0; i < 1000; ++i) {
            if (i % 3 == 0 || i % 5 == 0) {
                val += i;
            }
        }
        return val;
	}
}
