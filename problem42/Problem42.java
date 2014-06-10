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

	/* This is very lazy and slow. */
	public static boolean isTriangular(int num) {
		for(int i = 1; i <= num; ++i) {
			if(i*(i+1) / 2 == num) {
				return true;
			}
		}

		return false;
	}
}
