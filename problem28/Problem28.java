/*
 * This problem is actually very possible to do with pencil and paper
 * alone. The four arms of the spiral each follow a quadratic
 * progression. You can convince yourself that each sequance has a
 * "2nd difference" of 8. Some maths gives:
 *
 * a_i = (c/2)n^2 + (b0 - 3c/2)n + (a0 - b0 + c)
 * for b0 = (a1-a0) and c = second difference.
 *
 * x_i = 4n^2 - 10n + 7 (SE)
 * y_i = 4n^2 -  8n + 5 (SW)
 * z_i = 4n^2 -  6n + 3 (NW)
 * w_i = 4n^2 -  4n + 1 (NE)
 *
 * We wish to find the sum of these terms for n = 0 to 501, and then
 * subtract 3 because the 1 at the centre will have been counted 4
 * times and we only want it once.
 *
 * X_i = x_i + y_i + z_i + w_i
 *     = 16n^2 - 28n + 16
 * SUM = 16*n(n+1)(2n+1)/6 - 28*n(n+1)/2 + 16n
 *     = (8/3) * (n^2+n)(2n+1) - 14(n^2+n) + 16n
 *     = (8/3) * (2n^3 + 3n^2 + n) - 14n^2 - 14n + 16n
 *     = (16/3)n^3 + 8n^2 + (8/3)n - 14n^2 - 14n + 16n
 *     = (16/3)n^3 - 6n^2 + (14/3)n
 * ANS = [SUM for n = 501] - 3
 *     = (16/3)*501^3 - 6*501^2 + (14/3)*501 - 3
 *     = 669171001
 */

enum Direction {
	UP, DOWN, LEFT, RIGHT;

	public static Direction rot(Direction curr) {
		switch(curr) {
		case RIGHT:
			return DOWN;
		case DOWN:
			return LEFT;
		case LEFT:
			return UP;
		case UP:
			return RIGHT;
		}

		return null;
	}
}

class Position {
	public final int x, y;
	public Position(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public Position step(Direction currDir) {
		int x = this.x;
		int y = this.y;

		switch(currDir) {
		case RIGHT:
			x += 1;
			break;
		case DOWN:
			y += 1;
			break;
		case LEFT:
			x -= 1;
			break;
		case UP:
			y -= 1;
			break;
		}

		return new Position(x, y);
	}
}

class Grid {
	public static final int hsize = 500;
	public static final int size = 1001;
	protected Integer[][] grid = new Integer[size][size];

	public Grid() {
		Direction dir = Direction.UP;
		Direction trialDir = null;
		Position pos = new Position(0, 0);
		Position trialPos = null;
		

		// Keep increasing the number and turn right if possible.
		for(int value = 1; value <= size*size; ++value) {
			add(pos, value);
			// Rotate and step and see if there is a value there
			trialDir = Direction.rot(dir);
			trialPos = pos.step(trialDir);

			// If there is no value in the grid at the trial position,
			// then we were correct to turn. Otherwise, we weren't, so
			// make a step in the non-trial direction.
			if(get(trialPos) == null) {
				pos = trialPos;
				dir = trialDir;
			} else {
				pos = pos.step(dir);
			}
		}
	}

	public void add(Position pos, int value) {
		grid[pos.y+hsize][pos.x+hsize] = value;
	}

	public Integer get(Position pos) {
		return get(pos.x, pos.y);
	}

	public Integer get(int x, int y) {
		return grid[y+hsize][x+hsize];
	}
}

public class Problem28 {
	public static void main(String[] args) {
		Grid g = new Grid();
		int total = 1; // only need to add 1 once
		for(int i = 1; i <= g.hsize; ++i) {
			total += g.get(i, i); // SE
			total += g.get(i, -i); // NE
			total += g.get(-i, -i); // NW
			total += g.get(-i, i); // SW
		}

		System.out.println(total);
	}
}
