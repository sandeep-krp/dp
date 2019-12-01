package com.ersandeepkrp.dp;

import com.ersandeepkrp.dp.ds.Node;

/**
 * 
 * @author sandeep-krp
 * Given the head of a singly linked list, swap every two nodes and return its head.
 *
 */
public class DP145 {

	public Node<Integer> swapEveryTwoNodes(Node<Integer> head) {
		Node<Integer> currentNode = head;
		Node<Integer> second = null;
		Node<Integer> third = null;
		Node<Integer> newHead = null;
		Node<Integer> transitionNode = null;
		int position = 0;
		while (currentNode != null) {
			second = currentNode.getNext();
			third = second.getNext();

			if (position % 2 == 0) {
				currentNode.setNext(third);
				second.setNext(currentNode);
				if (transitionNode != null) {
					transitionNode.setNext(currentNode);
				}
			} else {
				transitionNode = currentNode;
			}

			currentNode = second;

			if (newHead == null) {
				newHead = second;
			}
			position++;
		}

		return newHead;

	}
}
