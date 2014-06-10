import primality.Primality;

public class Problem46 {
	public static void main(String[] args) {
		for(int i = 3; ; i+=2) {
			if(!Primality.isPrime(i)) {
				if(!sumOfPrimeAndTwiceSquare(i)) {
					System.out.println(i);
					return;
				}
			}
		}
	}

	public static boolean sumOfPrimeAndTwiceSquare(int num) {
		for(int sq = 1; sq*sq < num ; ++sq) {
			if(Primality.isPrime(num - 2*(sq*sq))) {
				return true;
			}
		}

		return false;
	}
}
