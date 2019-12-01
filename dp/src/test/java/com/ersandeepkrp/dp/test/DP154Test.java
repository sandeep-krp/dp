package com.ersandeepkrp.dp.test;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import com.ersandeepkrp.dp.DP154;

public class DP154Test {

	private DP154 solution;

	@Before
	public void init() {
		solution = new DP154();
	}

	@Test
	public void test1() {
		solution.push(3);
		solution.push(6);
		solution.push(2);
		solution.push(7);
		solution.push(8);

		Assert.assertEquals(Integer.valueOf(8), solution.pop());
	}

	@Test
	public void test2() {
		solution.push(3);
		solution.push(6);
		solution.push(2);
		solution.push(7);
		solution.push(8);

		Assert.assertEquals(Integer.valueOf(8), solution.pop());
		Assert.assertEquals(Integer.valueOf(7), solution.pop());
	}
	
	@Test
	public void test3() {
		solution.push(3);
		solution.push(6);
		solution.push(2);
		solution.push(7);
		solution.push(8);
		solution.pop();

		Assert.assertEquals(Integer.valueOf(7), solution.pop());
		Assert.assertEquals(Integer.valueOf(2), solution.pop());
		Assert.assertEquals(Integer.valueOf(6), solution.pop());
		
	}
	
	
	@Test
	public void test4() {
		solution.push(3);
		solution.push(6);
		solution.push(2);
		solution.push(7);
		solution.push(8);
		solution.pop();

		Assert.assertEquals(Integer.valueOf(7), solution.pop());
		Assert.assertEquals(Integer.valueOf(2), solution.pop());
		Assert.assertEquals(Integer.valueOf(6), solution.pop());
		solution.push(20);
		Assert.assertEquals(Integer.valueOf(20), solution.pop());
		
	}
	
}
