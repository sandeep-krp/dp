package com.ersandeepkrp.dp;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * 
 * @author sandeep-krp Implement a stack API using only a heap. A stack
 *         implements the following methods:
 * 
 *         push(item), which adds an element to the stack pop(), which removes
 *         and returns the most recently added element (or throws an error if
 *         there is nothing on the stack)
 */
public class DP154 {

	FakeHeap heap = new FakeHeap();

	public void push(Integer item) {
		Integer top = heap.pop();
		if (top == null) {
			heap.push(item);
			return;
		}

		heap.push(top);
		heap.push(top + item);

	}

	public Integer pop() {
		Integer top = heap.pop();
		if (top == null) {
			return null;
		}
		Integer secondTop = heap.pop();
		if (secondTop == null) {
			return top;
		}
		heap.push(secondTop);
		return top - secondTop;

	}

	@Override
	public String toString() {
		return "DP154 [heap=" + heap + "]";
	}

}

class FakeHeap {
	private List<Integer> heapList = new ArrayList<Integer>();

	public void push(Integer element) {
		heapList.add(element);
	}

	public Integer pop() {

		Collections.sort(heapList, Collections.reverseOrder());

		Integer high = heapList.stream().findFirst().orElse(null);
		if (high != null) {
			heapList.removeIf(i -> i == high);
		}
		return high;
	}
}
