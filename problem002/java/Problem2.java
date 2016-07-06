public class Problem2 {
	public static void main(String[] args) {
		System.out.println(sumEvenFibsUpto(4000000));
	}

    public static int fib(int n) {
        if (n <= 1) {
            return 1;
        }
        return fib(n-1) + fib(n-2);
    }

    public static int sumEvenFibsUpto(int upto) {
        int sum = 0;
        int fibVal;
        for (int i = 0; ; ++i) {
            fibVal = fib(i);
            if (fibVal > upto) {
                break;
            }

            if (fibVal % 2 == 0) {
                sum += fibVal;
            }
        }
        return sum;
    }
}
