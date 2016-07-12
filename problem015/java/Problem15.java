import java.util.HashMap;
import java.math.BigInteger;


/**
 * A pair of ints.
 *
 * Overrides hashCode and equals so it can be used as a key in a
 * HashMap.
 *
 * Overrides toString for convenience.
 */
class Coord {
    final int x, y;

    public Coord(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int hashCode() {
        return (int)Math.pow(2, x) + (int)Math.pow(3, y);
    }

    @Override
    public boolean equals(Object other) {
        return (other instanceof Coord) &&
            (((Coord)other).x == this.x) &&
            (((Coord)other).y == this.y);
    }

    @Override
    public String toString() {
        return "(" + this.x + ", " + this.y + ")";
    }
}


class LatticeCounter {
    HashMap<Coord, BigInteger> cache;
    int size;

    public LatticeCounter(int size) {
        this.cache = new HashMap<Coord, BigInteger>();
        this.size = size;
    }

    public BigInteger count() {
        return this.count(this.size, this.size);
    }

    /**
     * Count the number of paths from the given coordinates to the
     * start point.
     */
    public BigInteger count(int x, int y) {
        BigInteger result;

        result = this.cache.get(new Coord(x, y));
        if (result != null) {
            return result;
        }

        if (x == 0 || y == 0) {
            result = BigInteger.ONE;
        } else {
            result = this.count(x - 1, y).add(this.count(x, y - 1));
        }
        cache.put(new Coord(x, y), result);
        return result;
    }
}


public class Problem15 {
	public static void main(String[] args) {
        System.out.println((new LatticeCounter(20).count()));
	}
}
