import java.util.HashSet;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;
import java.util.ArrayList;

import primality.Primality;


public class Problem88 {
	public static final int from = 2;
	public static final int to = 12000;
	
	public static void main(String[] args) {
		int prodsumlength;
		Integer[] minprodsums = new Integer[to+1];

		int sum_facts;
		int num_facts;

		for(int i = from; i <= to*2; ++i) {
			for(HashMap<Integer, Integer> facts : Primality.factorisations(i)) {
				sum_facts = 0;
				num_facts = 0;

				for (Map.Entry<Integer, Integer> entry : facts.entrySet()) {
					Integer fact = entry.getKey();
					Integer count = entry.getValue();
					sum_facts += fact * count;
					num_facts += count;
				}
				
				if(sum_facts > i) {
					continue;
				}

				prodsumlength = num_facts + (i - sum_facts);

				if(!(prodsumlength > to) && (minprodsums[prodsumlength] == null)) {
					minprodsums[prodsumlength] = i;
				}
			}
		}

		// make sure we ignore 0 and 1
		minprodsums[0] = null;
		minprodsums[1] = null;

		Integer total = 0;
		HashSet<Integer> uniq = new HashSet<Integer>(Arrays.asList(minprodsums));
		uniq.remove(null);

		for(Integer k : uniq) {
			total += k;
		}

		System.out.println(total);
	}
}
