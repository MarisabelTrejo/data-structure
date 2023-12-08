# Trees
- [Back to Welcome Page](https://github.com/MarisabelTrejo/data-structure/blob/main/Welcome.md)
# Introduction
Just like linked lists nodes are connected together by pointers, so are **Trees**. The difference is that a tree can connect to multiple different nodes. 
## Types of Trees
- Binary Trees
- Binary Search Trees (BST)
- Binary Balanced Search Trees

# Big O Notation with BST
**insert(value)**	Insert a value into the tree.  - Recursively search the subtrees to find the next available spot | **remove(value)**	Remove a value from the tree.	- Recursively search the subtrees to find the value and then remove it. This will require some cleanup of the adjacent nodes |**contains(value)**	Determine if a value is in the tree. - Recursively search the subtrees to find the value. This would fall under O(logn). Because the BST is divided into section of greater than or less than we are able to cut our search in half; Thus, cutting the time in half.

traverse_forward	Visit all objects from smallest to largest.	 - Recursively traverse the left subtree and then the right subtree. |
traverse_reverse	Visit all objects from largest to smallest.	 - Recursively traverse the right subtree and then the left subtree. |
height(node)	Determine the height of a node. If the height of the tree is needed, the root node is provided.	- Recursively find the height of the left and right subtrees and then return the maximum height. This functions would fall under O(n) because we need to visit every node until we find n.
## Example - Family Tree
This family tree has a certain order it needs to go in. Nonetheless, they are all connected.

- ![fam tree](Images/family-tree.jpeg)

# Binary Search Trees
The parent node is the first node that is on top. If the tree is blank and we are **adding** a value to the tree, then the first added value would become the **parent** node. As we add more values, we compare them to the parent node. If they a **greater** then the value would go on the right subtree. If it is **less** than the parent node, then it will go on the left side. **Duplicates** can go on either side.
**We always start at the root node and compare the new value with it. We keep comparing until we have found an empty place for the new node.**

# Lets Work Together
Lets practice how to insert nodes in our BST!

# Problem to Solve
Lets practice how to add duplicates to our binary search tree.
