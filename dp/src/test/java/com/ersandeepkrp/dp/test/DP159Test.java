package com.ersandeepkrp.dp.test;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import com.ersandeepkrp.dp.DP159;

public class DP159Test {

	private DP159 solution;

	@Before
	public void init() {
		solution = new DP159();
	}

	@Test
	public void test1() {
		String input = "adflkjladadf";
		String ans = this.solution.findFirstReoccuringChar(input);
		Assert.assertEquals(ans, "l");
	}
	
	@Test
	public void test2() {
		String input = "Whichletter";
		String ans = this.solution.findFirstReoccuringChar(input);
		Assert.assertEquals(ans, "h");
	}
	
	@Test
	public void testNoReoccuringLetter() {
		String input = "asdfghjkl";
		String ans = this.solution.findFirstReoccuringChar(input);
		Assert.assertNull(ans);;
	}
}
