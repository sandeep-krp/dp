package com.ersandeepkrp.dp.ds;

public class LinkedList<T> {
	private Node<T> head;
	private Node<T> last;

	public void add(T item) {
		Node<T> node = new Node<T>(item);
		if (head == null) {
			head = node;
			last = head;
			return;
		}

		last.setNext(node);
		this.last = node;
	}

	public Node<T> getHead() {
		return this.head;
	}

	@Override
	public String toString() {
		Node<T> node = head;
		StringBuilder sb = new StringBuilder();
		sb.append("[");
		sb.append(head.getValue());
		sb.append(",");
		while (node.getNext() != null) {
			sb.append(node.getNext());
			sb.append(",");
			node = node.getNext();
		}
		sb.append("]");
		return sb.toString();
	}

}
