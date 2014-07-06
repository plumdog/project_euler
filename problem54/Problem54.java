import java.io.IOException;
import java.util.List;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;
import java.nio.charset.Charset;
import java.util.Arrays;
import java.util.Collections;
import java.util.ArrayList;
import java.util.Hashtable;


/* Gratitude must go to
 * http://www.mathblog.dk/project-euler-54-poker-hands/ for giving me
 * a reference to test against when I got the answer nearly right, but
 * not quite. */

public class Problem54 {
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
		String p1, p2;
		for(String line : lines) {
			p1 = line.substring(0, 3*5-1);
			p2 = line.substring(3*5, line.length());
			if(p1Wins(p1, p2)) {
				++count;
			}
		}
		

		System.out.println(count);
	}
		
	public static boolean p1Wins(String p1, String p2) {
		PokerHand h1 = new PokerHand(p1);
		PokerHand h2 = new PokerHand(p2);
		return (h1.compareTo(h2) > 0);
	}
}

class PokerHand implements Comparable<PokerHand> {
	Card[] cards;

	public PokerHand(String cardsString) {
		String[] cardsArray = cardsString.split(" ");
		cards = new Card[cardsArray.length];
		int num = 0;
		for(String cardString : cardsArray) {
			cards[num] = new Card(cardString);
			++num;
		}
	}

	public String toString() {
		return cards[0] + " " +
			cards[1] + " " +
			cards[2] + " " +
			cards[3] + " " +
			cards[4];
	}

	public Card highestCard() {
		int value = -1;
		Card highest = null;
		for(Card c : cards) {
			if (c.compareValue() > value) {
				highest = c;
				value = c.compareValue();
			}
		}

		return highest;
	}

	public Result getResult() {
		Result r = new Result();
		if (isStraightFlush()) {
			r.cat = ResultCat.SF;
			r.first = highestCard().compareValue();
		} else if (isFour()) {
			r.cat = ResultCat.F;
			for (int key : Collections.list(rankOccurencesHash().keys())) {
				if (rankOccurencesHash().get(key) == 4) {
					r.first = key;
					break;
				}
			}
		} else if (isFullHouse()) {
			r.cat = ResultCat.FH;
			for (int key : Collections.list(rankOccurencesHash().keys())) {
				if (rankOccurencesHash().get(key) == 3) {
					r.first = key;
					break;
				}
			}
		} else if (isFlush()) {
			r.cat = ResultCat.FL;
			int[] cardIndexes = cardIndexes();
			r.first = cardIndexes[4];
			r.second = cardIndexes[3];
			r.third = cardIndexes[2];
			r.fourth = cardIndexes[1];
			r.fifth = cardIndexes[0];
		} else if (isStraight()) {
			r.cat = ResultCat.ST;
			r.first = highestCard().compareValue();
		} else if (isThree()) {
			r.cat = ResultCat.T;
			for (int key : Collections.list(rankOccurencesHash().keys())) {
				if (rankOccurencesHash().get(key) == 3) {
					r.first = key;
					break;
				}
			}
		} else if (isTwoPair()) {
			r.cat = ResultCat.TP;
			for (int key : Collections.list(rankOccurencesHash().keys())) {
				if (rankOccurencesHash().get(key) == 2) {
					if(r.first == 0) {
						r.first = key;
					} else {
						r.second = key;
					}
				}
			}

			if (r.first < r.second) {
				int temp = r.first;
				r.first = r.second;
				r.second = temp;
			}
		} else if (isPair()) {
			r.cat = ResultCat.P;
			for (int key : Collections.list(rankOccurencesHash().keys())) {
				if (rankOccurencesHash().get(key) == 2) {
					r.first = key;
					break;
				}
			}

			int max_remaining = 0;
			for(Card c : cards) {
				if((c.cardIndex != r.first) && (c.compareValue() > max_remaining)) {
					max_remaining = c.compareValue();
				}
			}
			r.second = max_remaining;
		} else {
			r.cat = ResultCat.HC;
			r.first = highestCard().compareValue();
		}

		return r;
	}

	public ArrayList<Integer> rankOccurences() {
		return new ArrayList<Integer>(rankOccurencesHash().values());
	}

	public Hashtable<Integer, Integer> rankOccurencesHash() {
		Hashtable<Integer, Integer> ht = new Hashtable<Integer, Integer>();
		Integer current;
		for(Card card : cards) {
			current = ht.get(card.cardIndex);
			if (current == null) {
				current = 0;
			}

			current++;
			ht.put(card.cardIndex, current);
		}
		return ht;
	}

	public boolean isStraightFlush() {
		return isStraight() && isFlush();
	}

	public boolean isFour() {
		return Collections.max(rankOccurences()) == 4;
	}

	public boolean isFullHouse() {
		return hasPair() && hasThree();
	}

	public boolean isFlush() {
		Character suit = null;
		for(Card card : cards) {
			if (suit == null) {
				suit = card.suit;
			} else if (suit != card.suit) {
				return false;
			}
		}

		return true;
	}

	protected int[] cardIndexes() {
		int[] indexes = new int[5];
		int ind = 0;
		for(Card card : cards) {
			indexes[ind] = card.cardIndex;
			++ind;
		}

		Arrays.sort(indexes);
		return indexes;
	}

	public boolean isStraight() {
		int[] indexes = cardIndexes();
		int min = indexes[0];
		for(int i = 1; i < 5; ++i) {
			if (min + i != indexes[i]) {
				return false;
			}
		}

		return true;
	}

	public boolean isThree() {
		return Collections.max(rankOccurences()) == 3;
	}

	public boolean isPair() {
		return Collections.max(rankOccurences()) == 2;
	}

	public boolean isTwoPair() {
		int pairCount = 0;
		for(int cardCount : rankOccurences()) {
			if (cardCount == 2) {
				++pairCount;
			}
		}

		return pairCount == 2;
	}

	public boolean hasPair() {
		return rankOccurences().contains(2);
	}

	public boolean hasThree() {
		return rankOccurences().contains(3);
	}

	@Override
	public int compareTo(PokerHand other) {
		return getResult().compareTo(other.getResult());
	}
}

/*
 * High card: first is the value of the high card.
 *
 * OnePair: first is the index of the pair, second is the highest
 * remaining card.
 *
 * TwoPair: first is the index of the top pair, second is the
 * index of the second pair, ternary is the value of the remaining
 * card.
 *
 * Three of a Kind: first is the index of the three.
 *
 * Straigth: first is the value of the highest card.
 *
 * Flush: first is highest index, second is second and so on.
 *
 * Full House: first is the index of the three.
 *
 * Four of a Kind: first is the index of the four.
 *
 * Straight Flush: first is the value of the highest card.
 */
class Result implements Comparable<Result> {
	ResultCat cat;
	int first;
	int second;
	int third;
	int fourth;
	int fifth;

	public String toString() {
		return cat.toString() + " " + first + " " + second + " " + third + " " + fourth + " " + fifth;
	}

	@Override
	public int compareTo(Result other) {
		if(cat != other.cat) {
			return cat.ordinal() > other.cat.ordinal() ? 1 : -1;
		} else if(first != other.first) {
			return first - other.first;
		} else if(second != other.second) {
			return second - other.second;
		} else if(third != other.third) {
			return third - other.third;
		} else if(fourth != other.fourth) {
			return fourth - other.fourth;
		} else if(fifth != other.fifth) {
			return fifth - other.fifth;
		}
		return 0;
	}
}

enum ResultCat {
	HC, P, TP, T, ST, FL, FH, F, SF
}

class Card {
	int cardIndex;
	char suit;
	char rank;

	public Card(String cardString) {
		rank = cardString.charAt(0);
		cardIndex = cardLetterToInt(cardString.charAt(0));
		suit = cardString.charAt(1);
	}

	public String toString() {
		return new StringBuilder().append(rank).append(suit).toString();
	}

	public static int cardLetterToInt(char ch) {
		switch(ch) {
		case '2': return 2;
		case '3': return 3;
		case '4': return 4;
		case '5': return 5;
		case '6': return 6;
		case '7': return 7;
		case '8': return 8;
		case '9': return 9;
		case 'T': return 10;
		case 'J': return 11;
		case 'Q': return 12;
		case 'K': return 13;
		case 'A': return 14;
		}
		return 0;
	}

	public int compareValue() {
		return (cardIndex - 2) * 4 + suitToInt(suit);
	}

	public static int suitToInt(char suit) {
		switch(suit) {
		case 'C': return 1;
		case 'D': return 2;
		case 'H': return 3;
		case 'S': return 4;
		}
		return 0;
	}
}
