import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.Charset;
import java.util.List;


public class Problem11 {
        public static final int gridSize = 20;
	public static final int runLen = 4;
	public static final int[][] grid = new int[gridSize][gridSize];

	public static void main(String[] args) {
                getGrid(args[0]);
		int max = 0;
		for(int row = 0; row < gridSize; ++row) {
			for(int col = 0; col < gridSize; ++col) {
				max = Math.max(max, maxDown(row, col));
				max = Math.max(max, maxAcross(row, col));
				max = Math.max(max, maxSE(row, col));
				max = Math.max(max, maxSW(row, col));
			}
		}

		System.out.println(max);
	}

        public static void getGrid(String fname) {
                List<String> lines;
                try {
                        lines = Files.readAllLines(Paths.get(fname), Charset.forName("ascii"));
                } catch (IOException e) {
                        System.err.println("Unable to load file: " + e);
                        return;
                }

                for (int lineNum = 0; lineNum < gridSize; ++lineNum) {
                        String[] numsAsStrings = lines.get(lineNum).split(" ");
                        for (int colNum = 0; colNum < gridSize; ++colNum) {
                                grid[lineNum][colNum] = Integer.parseInt(numsAsStrings[colNum]);
                        }
                }
        }

	public static int maxDown(int row, int col) {
                return run(row, col, 0, 1);
	}

	public static int maxAcross(int row, int col) {
                return run(row, col, 1, 0);
	}

	public static int maxSE(int row, int col) {
                return run(row, col, 1, 1);
	}

	public static int maxSW(int row, int col) {
                return run(row, col, 1, -1);
	}

        public static int run(int row, int col, int xStep, int yStep) {
                int total = 1;
                int value;
                for (int i = 0; i < runLen; ++i) {
                        try {
                                value = grid[row + i * yStep][col + i * xStep];
                        } catch(ArrayIndexOutOfBoundsException e) {
                                return 0;
                        }
                        total *= value;
                }
                return total;
        }
}
