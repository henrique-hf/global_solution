from src.AVLTreeNode import AVLTreeNode


class AVLTree(object):

    def __init__(self, items_objs=None):
        """Initialize this AVL tree and insert the given items."""
        self.root = None
        self.size = 0
        if items_objs is not None:
            for e in items_objs:
                self.insert(e[0], e[1])

    def __str__(self, node=None):
        """Return a visual string representation of this binary search tree.
        Performs depth-first traversal starting at the given node or root."""
        if node is None:
            if self.is_empty():  # Special case
                return 'root -> None'
            else:  # Start recursion at root node
                return '\n'.join(self.__str__(self.root))
        strings = []  # Accumulate separate strings since we need to pad them
        if node.right is not None:  # Descend right subtree, if it exists
            for right_string in self.__str__(node.right):
                # Left-pad strings and replace ambiguous root with right link
                strings.append(5 * ' ' + right_string.replace('->', '/-', 1))
        strings.append('-> ({})'.format(repr(node.data)))  # This node's string
        if node.left is not None:  # Descend left subtree, if it exists
            for left_string in self.__str__(node.left):
                # Left-pad strings and replace ambiguous root with left link
                strings.append(5 * ' ' + left_string.replace('->', '\\-', 1))
        return strings

    def __repr__(self):
        """Return a string representation of this AVL tree."""
        return 'AVLTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node)."""
        # Check if root node has a value and if so calculate its height
        return self.root.height()

    def search(self, item):
        """Return an item in this tree matching the given item,
        or None if the given item is not found."""
        nodes_list = []
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root, nodes_list)
        # Return the node's data if found, or None
        return (node.data, node.obj, nodes_list) if node else (None, nodes_list)

    def insert(self, item, obj, node=None):
        """Insert the given item in order into this tree."""
        if self.is_empty():
            self.root = AVLTreeNode(item, obj)
            self.size += 1
            return

        if node is None:
            node = self.root
            self.size += 1

        if item == node.data:
            self.size -= 1
            return
        elif item < node.data:
            if node.contains_left_node():
                added_subtree = self.insert(item, obj, node.left)
                if added_subtree is not None:
                    node.left = added_subtree
            else:
                added_node = AVLTreeNode(item, obj)
                node.left = added_node
        else:
            if node.contains_right_node():
                added_subtree = self.insert(item, obj, node.right)
                if added_subtree is not None:
                    node.right = added_subtree
            else:
                added_node = AVLTreeNode(item, obj)
                node.right = added_node
        node.get_height()
        return self.balance(node)

    def balance(self, node):
        bf = node.get_balance()
        if 2 > bf > -2:
            return None
        if bf < -1:
            if node.left.get_balance() < 0:
                new_root = node.right_rotation()
            else:
                node.left = node.left.left_rotation()
                new_root = node.right_rotation()
        else:
            if node.right.get_balance() > 0:
                new_root = node.left_rotation()
            else:
                node.right = node.right.right_rotation()
                new_root = node.left_rotate()
        if node is self.root:
            self.root = new_root
        return new_root

    def _find_node_recursive(self, item, node, nodes_list):
        """Return the node containing the given item in this tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        else:
            nodes_list.append(node.data)
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Recursively descend to the node's left child, if it exists
                return self._find_node_recursive(item, node.left, nodes_list)
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Recursively descend to the node's right child, if it exists
                return self._find_node_recursive(item, node.right, nodes_list)


if __name__ == '__main__':
    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    obj = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
    print(len(items) == len(obj))

    tree = AVLTree()

    for i in range(len(items)):
        tree.insert(items[i], obj[i])

    print(tree)

    print(tree.search(10))