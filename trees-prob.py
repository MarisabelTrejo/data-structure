class BST:

    class Node:

        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        "PROBLEM TO SOLVE: Make this binary search tree add duplicates"
        if data != node.data:
            if data < node.data:
                # The data belongs on the left side.
                if node.left is None:
                    # We found an empty spot
                    node.left = BST.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the left sub-tree.
                    self._insert(data, node.left)
            else:
                # The data belongs on the right side.
                if node.right is None:
                    # We found an empty spot
                    node.right = BST.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the right sub-tree.
                    self._insert(data, node.right)
        

    def __contains__(self, data):
  
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):

        # BASE CASE
        # STOP WHEN YOU FIND IT
        # if nonde is none of the them, return false

        if node is None:
            return False
        if data == node.data:
            return True

        
        if data < node.data:      
            # Need to keep looking. 
            # recursively on the left sub-tree.
                return self._contains(data, node.left)

        if data > node.data: 
                
            # Need to keep looking.
            # recursively on the right sub-tree.
                return self._contains(data, node.right)

    def __iter__(self):
  
        yield from self._traverse_forward(self.root)  # Start at the root

        
    def _traverse_forward(self, node):
  
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):

        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):

        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

# This is how we insert into our tree
print("\n=========== PROBLEM 1 TESTS ===========")
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(1)
for number in tree:
    print(number)  # 1, 3, 4, 5, 6, 7, 10
