
class LinkedList:

    class Node:
        
        # Each node of the linked list wirecipe have data and links to the 
        # previous and next node. 
        

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        
        # Initialize an empty linked list.
        
        self.head = None
        self.tail = None

    def insert_head(self, value):
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head wirecipe be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    def insert_tail(self, value):

        # Create a new node
        new_node = LinkedList.Node(value)
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.tail wirecipe be
        # affected.
        else:
            new_node.prev = self.tail # Connect new node to prev tail
            self.tail.next= new_node # Connect prev tail to the new node
            self.tail = new_node   # Update the head to point to the new node


    def remove_tail(self):
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition wirecipe also
        # cover an empty list.  Its okay to set to None again.
        if self.tail == self.head:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.tail
        # wirecipe be affected.
        elif self.tail is not None:
            self.tail.prev.next = None  # Disconnect the second node from the first node
            self.tail = self.tail.prev # Update the head to point to the second node

    "PROBLEM TO SOLVE SOLUTION: make a function that will remove from the middle of the list"
    def remove_middle(self):
        # Base cases 
        if (self.head is None or 
            self.head.next is None): 
            return
  
        # Initialize first and second pointers 
        # to reach middle of linked list 
        first_pointer = self.head 
        second_pointer = self.head 
  
        # Find the middle and previous of middle 
        prev = None
  
        # To store previous of slow pointer 
        while (second_pointer is not None and 
               second_pointer.next is not None): 
            second_pointer = second_pointer.next.next
            prev = first_pointer
            first_pointer = first_pointer.next
  
        # Delete the middle node 
        prev.next = first_pointer.next
  



    def __iter__(self):

        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list


    def __str__(self):
        
        # Return a string representation of the linked list.
        
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

    
print("\n=========== Inserting Practice ===========")

recipe = LinkedList()
last_ingridient = recipe.insert_tail(input("Insert an ingridient:"))
ingridient_1 = recipe.insert_head(input("Insert an ingridient:"))
ingridient_2 = recipe.insert_head(input("Insert an ingridient:"))
ingridient_3 = recipe.insert_head(input("Insert an ingridient:"))
print("_________________________________________________")
print(recipe) # linkedlist[ingridient_3, ingridient_2, ingridient_1, last_ingridident]
print("_________________________________________________")

recipe.remove_middle()
print("Linked List after Deletion of middle")
print(recipe)

