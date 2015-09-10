import java.io.IOException;
import java.util.List;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;
import java.nio.charset.Charset;


public class Problem42 {
	public static void main(String[] args) {
		String path = null;
		
		try {
			path = args[0];
		} catch(ArrayIndexOutOfBoundsException e) {
			System.out.println("No filename given.");
			return;
		}

		Path fullPath = Paths.get(path);

		List<String> lines = null;
		try {
			lines = Files.readAllLines(fullPath, Charset.defaultCharset());
		} catch(IOException e) {
			System.out.println("File not loaded");
			return;
		}

		int count = 0;

		for(String line : lines) {
			if(isTriangular(stringValue(line))) {
				++count;
			}
		}

		System.out.println(count);
	}

	public static int stringValue(String st) {
		int total = 0;
		for(char ch : st.toCharArray()) {
			total += ((int) ch) - 64;
		}

		return total;
	}

	/* From num = n(n+1)/2 we get n = (-1 + sqrt(1+8*num))/2
	 * So we require that 1+8*num is an odd square, so that
	 * is what we test for.
	 */
	public static boolean isTriangular(int num) {
		int val = 1+8*num;
		int sqrt = (int) Math.sqrt(1+8*num);
		return (val == sqrt*sqrt) && (sqrt % 2 == 1);
	}
}
