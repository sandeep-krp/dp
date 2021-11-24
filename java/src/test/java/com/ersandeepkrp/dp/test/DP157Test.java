package com.ersandeepkrp.dp.test;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import com.ersandeepkrp.dp.DP157;

public class DP157Test {

	private DP157 solution;

	@Before
	public void init() {
		this.solution = new DP157();
	}

	@Test
	public void test() {
		Assert.assertTrue(this.solution.hasPalindrone("a"));
	}

	@Test
	public void test2() {
		Assert.assertTrue(this.solution.hasPalindrone("aba"));
	}

	@Test
	public void test3() {
		Assert.assertTrue(this.solution.hasPalindrone("dalda"));
	}

	@Test
	public void test4() {
		Assert.assertFalse(this.solution.hasPalindrone("daldaa"));
	}
	
	@Test
	public void test5() {
		Assert.assertFalse(this.solution.hasPalindrone("sandeep"));
	}
	
	@Test
	public void test6() {
		Assert.assertTrue(this.solution.hasPalindrone("auhfuah"));
	}
	
	@Test
	public void test7() {
		Assert.assertTrue(this.solution.hasPalindrone("auhffuah"));
	}
}
