package com.ersandeepkrp.dp;

import java.util.HashMap;

/**
 * 
 * @author sandeep-krp Given a string, determine whether any permutation of it
 *         is a palindrome.
 */
public class DP157 {

	/*
	 * 
	 * 
	 */
	public Boolean hasPalindrone(String input) {
		HashMap<Character, Integer> wc = new HashMap<>();
		// Find the word count of each character
		for (int i = 0; i < input.length(); i++) {
			char charAt = input.charAt(i);
			if (!wc.containsKey(charAt)) {
				wc.put(charAt, Integer.valueOf(0));
			}
			wc.put(charAt, wc.get(charAt) + 1);
		}
		// If the number of odd occurences of work in more than one, the string can not
		// have palindrome
		return wc.values().stream().filter(item -> {
			return !(item % 2 == 0);
		}).count() <= 1;

	}
}
