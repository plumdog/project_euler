package primality;

import java.util.HashMap;
import java.util.List;
import java.util.HashSet;
import java.util.Arrays;

public class Primality {

	public static boolean isPrime(int val) {
		if(val == 2) {
			return true;
		}

		if((val < 2) || (val % 2 == 0)) {
			return false;
		}

		int upto = (int) Math.round(Math.sqrt(val));

		for(int i = 3; i <= upto; i+=2) {
			if(val % i == 0) {
				return false;
			}
		}

		return true;
	}

	public static HashMap<Integer, Integer> primeFactors(int num) {
		HashMap<Integer, Integer> prime_divs = new HashMap<Integer, Integer>();

		int trial = 2;
		int num_ = num;
		int top = (int) Math.round(Math.sqrt(num_));

		while(true) {
			if(trial > top) {
				HashMap<Integer, Integer> d = new HashMap<Integer, Integer>();
				d.put(num_, 1);
				return d;
			} else if(num_ % trial == 0) {
				HashMap<Integer, Integer> parent = primeFactors(num_ / trial);
				Integer current = parent.get(trial);
				if(current == null) {
					current = 0;
				}
				parent.put(trial, current + 1);
				return parent;
			} else {
				if(trial == 2) {
					++trial;
				} else {
					trial += 2;
				}
			}
		}
	}

	/*
	public static ArrayList<ArrayList<Integer>> factorisations(int num) {
		//ArrayList<Integer> skip = new ArrayList<Integer>();
		return factorisations(num, ski);
	}
	*/

	public static HashSet<HashMap<Integer, Integer>> factorisations(int num) {
		if(num == 1) {
			HashSet<HashMap<Integer, Integer>> l = new HashSet<HashMap<Integer, Integer>>();
			l.add(new HashMap<Integer, Integer>());
			return l;
		}

		HashSet<HashMap<Integer, Integer>> fs = new HashSet<HashMap<Integer, Integer>>();
		for(int i = 2; i <= num / 2; ++i) {
			if(num % i != 0) {
				continue;
			}

			for(HashMap<Integer, Integer> l : factorisations(num / i)) {
				if(l.get(i) == null) {
					l.put(i, 1);
				} else {
					l.put(i, l.get(i) + 1);
				}
				fs.add(l);
			}
		}

		for(HashMap<Integer, Integer> l : factorisations(1)) {
			if(l.get(num) == null) {
				l.put(num, 1);
			} else {
				l.put(num, l.get(num) + 1);
			}
			fs.add(l);
		}

		return fs;
	}
}
