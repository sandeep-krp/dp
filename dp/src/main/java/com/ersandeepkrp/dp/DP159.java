package com.ersandeepkrp.dp;

import java.util.ArrayList;
import java.util.List;


/**
 * 
 * @author markov
 *	Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
 */
public class DP159 {

	public String findFirstReoccuringChar(String input) {
		String recurringElement = null;
		List<String> hasOrNot = new ArrayList<>();
		for (int i = 0; i < input.length(); i++) {

			String c = String.valueOf(input.charAt(i));
			if (hasOrNot.contains(c)) {
				recurringElement = c;
				break;
			} else {
				hasOrNot.add(c);
			}
		}
		return recurringElement;
	}
}
