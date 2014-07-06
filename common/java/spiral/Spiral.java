package spiral;

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

public class Spiral {
	public final int hsize;
	public final int size;
	protected Integer[][] grid;

	public Spiral(int hsize) {
		this.hsize = hsize;
		size = hsize * 2 + 1;
		grid = new Integer[size][size];

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
