#!python
#Insperation from https://www.geeksforgeeks.org/doubly-linked-list/   &
#https://en.wikipedia.org/wiki/Doubly_linked_list#Open_doubly_linked_lists

class Node:
    def __init__(self, data, next=None, prev=None):
        """Initialize this node with the given data."""
        self.next = next  # reference to next node in DLL
        self.prev = prev  # reference to previous node in DLL
        self.data = data

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class DoublyLinkedList:
    # Constructor for empty Doubly Linked List
    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None
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

    def push(self, new_data):
        """Inserts a new node on the front of list, given a reference to the head of a list"""
        new_node = Node(new_data)

        # Make new node's next the head and it's previous as None (already None)
        new_node.next = self.head

        # Change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        # Move the head to point to the new node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        """Given a node as prev_node, insert a new node after the given node"""
        # Check if the given prev_node is None
        if prev_node is None:
            print ("the given previous node cannot be NULL")
            return

        new_node = Node(new_data)

        # From the node we are instering after, steal it's next reference
        new_node.next = prev_node.next

        # Inster in-front and reference as next
        prev_node.next = new_node

        # Set the new nodes previous to the one behind it
        new_node.prev = prev_node

        # Change previous of new_nodes's next node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):
        """Append a new node at the end of the DLL, given a reference to the head, and new data"""
        new_node = Node(new_data)
        new_node.next = None
        # This new node is going to be the last node, so make its next be None

        # If the Linked List is empty, then make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # Else traverse till the last node
        last = self.head
        while(last.next is not None):
            last = last.next

        # Change the next of last node to this node
        last.next = new_node

        # Make last node as previous of new node
        new_node.prev = last
        return

    def printList(self, node):
        """This function prints contents of linked list starting from the given node"""
        print ("\nTraversal in forward direction")
        while(node is not None):
            print (" % d" % (node.data))
            last = node
            node = node.next

        print ("\nTraversal in reverse direction")
        while(last is not None):
            print (" % d" % (last.data))
            last = last.prev


# Driver program to test above functions
# Start with empty list
llist = DoublyLinkedList()

# Insert 6. So the list becomes 6->None
llist.append(6)

# Insert 7 at the beginning.
# So linked list becomes 7->6->None
llist.push(7)

# Insert 1 at the beginning.
# So linked list becomes 1->7->6->None
llist.push(1)

# Insert 4 at the end.
# So linked list becomes 1->7->6->4->None
llist.append(4)

# Insert 8, after 7.
# So linked list becomes 1->7->8->6->4->None
llist.insertAfter(llist.head.next, 8)

print ("Created DLL is: ") 
print(llist)
llist.printList(llist.head)
