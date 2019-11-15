#!python
#Replace and Delete Function Inspired by https://github.com/ablades/CS-1.2-Intro-Data-Structures/blob/master/Code/linkedlist.py
#Swap Function Inspired by https://www.geeksforgeeks.org/swap-nodes-in-a-linked-list-without-swapping-data/

class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def traverse_length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Loops through all items once till the end"""
        # TODO: Loop through all nodes and count one for each
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length
        
    def iterable_length(self):
        length = 0
        for _ in self:
            length += 1
        return length

    def recursive_length(self, node):
        """Return the length of this linked list by counting number of nodes recursively."""
        if (not node):  # Base case
            return 0
        else:
            return 1 + self.recursive_length(node.next)

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) static function always run the same amount"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        node = Node(item)
        if self.is_empty():
            self.head = node
        if self.tail is not None:
            self.tail.next = node
        self.tail = node

        """
        node = Node(item)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        """

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) static function always run the same amount"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_head = Node(item)
        if self.is_empty():
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head = new_head

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) Function only runs once finding head
        TODO: Worst case running time: O(n) Function runs through n loops of length"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head

        while node is not None:
            if quality(node.data):
                return node.data
            else:
                node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Function only runs once cause there's nothing or it finds the head
        TODO: Worst case running time: O(n) Function runs through n loops of length"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        #set starting points
        current = self.head
        prev = None
        print("\n---------DELETE ITEM {}-------------".format(item))
        # Search for the item to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (current is not None):
            if current.data == item:
                #item we want to remove is at head
                if prev is None:
                    print("Remove the head")
                    self.head = self.head.next
                    print("Head is also tail remove it")
                    if current.next is None:
                        self.tail = prev
                #item we want to remove is at tail
                elif current.next is None:
                    print("Updating Tail from {} to {}".format(self.tail, prev))
                    prev.next = None
                    self.tail = prev
                else:
                    #item we want to remove is not an edge case
                    #make previous node point to next node
                    print("\nChange Link [{} --> {}] To new link, [{} --> {}]".format(current, current.next, prev, current.next))
                    prev.next = current.next
                print("\nAfter Deleteing new list is: ", self)
                print("Head: {}, Tail: {}".format(self.head, self.tail))
                return
            else:
                #item has not been found yet advance pointers
                prev = current
                current = current.next
        raise ValueError(f'Item not found: {item}')

    def replace(self, old_item, new_item):
        """Replace an old item in the list with a new item"""
        curr = self.head

        while curr is not None:

            if curr.data == old_item:
                curr.data = new_item
                return
            curr = curr.next

    def find_spot(self, item):
        # Search for item (keep track of prev and Curr)
        prev = None
        curr = self.head
        while curr != None and curr.data != item:
            prev = curr
            curr = curr.next
        return [prev, curr]

    def swap(self, prev, curr):
        # If previous is not head of linked list
        if prev != None:
            prev.next = curr
        else:  # make previous the new head
            self.head = curr

    def swap_nodes(self, first, second):
        """Swap two item in linked list by changin links """
        # Nothing to do if x and y are same
        if first == second:
            return

        # Search for first (keep track of prev and Curr)
        first_spot = self.find_spot(first)
        # Search for second (keep track of prev and curr)
        second_spot = self.find_spot(second)
        fprev = first_spot[0]
        fcurr = first_spot[1]
        sprev = second_spot[0]
        scurr = second_spot[1]
        # If either first or second are not present, nothing to do
        if fcurr == None or scurr == None:
            return

        self.swap(fprev, scurr)
        self.swap(sprev, fcurr)

        # Swap next pointers
        temp = fcurr.next
        fcurr.next = scurr.next
        scurr.next = temp

def test_linked_list():
    ll = LinkedList()
    # print('list: {}'.format(ll))

    # print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        # print('append({!r})'.format(item))
        ll.append(item)
    print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length by traversing: {}'.format(ll.traverse_length()))
    print('length by recursive: {}'.format(ll.recursive_length(ll.head)))
    print('length by iterable: {}'.format(ll.iterable_length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.iterable_length()))

    replace_implemented = False
    if replace_implemented:
        print("\nTesting replace:")
        print('list: {}'.format(ll))
        old_item = input("old item to replace: ")
        new_item = input("new data for item: ")
        ll.replace(old_item, new_item)
        print('list: {}'.format(ll))

    swap_implemented = False
    if swap_implemented:
        print("\tTesting replace:")
        print("list: {}".format(ll))
        first_item = input("first item to be swapped: ")
        second_item = input("second item: ")
        ll.swap_nodes(first_item, second_item)
        print('list: {}'.format(ll))

    iterable_implemented = True
    if iterable_implemented:
        print("\nTesting iterable")
        # print("list: {}".format(ll))
        for item in ll:
            print(item)


if __name__ == '__main__':
    test_linked_list()
