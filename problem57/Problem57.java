import fraction.BigFraction;
import java.math.BigInteger;


public class Problem57 {
	public static void main(String[] args) {
		BigFraction one = BigFraction.ONE;
		BigFraction fr = one;

		int count = 0;
		for(int i = 1; i <= 1000; ++i) {
			fr = fr.add(one).inverse().add(one);
			if(fr.num().toString().length() > fr.den().toString().length()) {
				count++;
			}
		}

		System.out.println(count);
	}
}
