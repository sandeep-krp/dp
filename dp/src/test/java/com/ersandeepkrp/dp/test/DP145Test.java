package com.ersandeepkrp.dp.test;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import com.ersandeepkrp.dp.DP145;
import com.ersandeepkrp.dp.ds.LinkedList;
import com.ersandeepkrp.dp.ds.Node;

public class DP145Test {
	private DP145 solution;

	@Before
	public void init() {
		this.solution = new DP145();
	}

	@Test
	public void test1() {
		LinkedList<Integer> list = new LinkedList<>();
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);

		Node<Integer> newHead = this.solution.swapEveryTwoNodes(list.getHead());

		Assert.assertEquals(Integer.valueOf(2), newHead.getValue());
		Assert.assertEquals(Integer.valueOf(1), newHead.getNext().getValue());

	}

	@Test
	public void test2() {
		LinkedList<Integer> list = new LinkedList<>();
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);

		Node<Integer> newHead = this.solution.swapEveryTwoNodes(list.getHead());

		Node<Integer> first = newHead;
		Node<Integer> second = first.getNext();
		Node<Integer> third = second.getNext();
		Node<Integer> fourth = third.getNext();

		Assert.assertEquals(Integer.valueOf(4), third.getValue());
		Assert.assertEquals(Integer.valueOf(3), fourth.getNext().getValue());

	}
}
