using System.Collections.Generic;
using System.Linq;

public class Problem1 {
	public static void Main() {
        System.Console.WriteLine(
            Enumerable.Range(1, 999)
            .Where(i => ((i % 3 == 0) || (i % 5 == 0)))
            .Sum());
    }
}
