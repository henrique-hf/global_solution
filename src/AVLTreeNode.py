class AVLTreeNode(object):

    def __init__(self, data, obj):
        """Initialize this avl tree node with the given data."""
        self.data = data
        self.obj = obj
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        """Return a string representation of this avl tree node."""
        return 'AVLTreeNode({!r})'.format(self.data)

    def contains_left_node(self):
        """Returns true/false if there is a left node"""
        if self.left is None:
            return False
        else:
            return True

    def contains_right_node(self):
        """Returns true/false if there is a right node"""
        if self.right is None:
            return False
        else:
            return True

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        if self.left or self.right:
            return False
        else:
            return True

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        if self.left or self.right:
            return True
        else:
            return False

    def get_balance(self):
        """Similar to get height, if a None child is passed,
        its children are equally balanced so balance factor is 0"""
        if self.is_leaf():
            return 0
        elif self.contains_right_node() is False:
            return -self.left.height - 1
        elif self.contains_left_node() is False:
            return self.right.height + 1
        else:
            return self.right.height - self.left.height

    def get_height(self):
        """calculate/update node height"""
        if self.is_leaf():
            self.height = 0
        elif not self.contains_left_node():
            self.height = self.right.height + 1
        elif not self.contains_right_node():
            self.height = self.left.height + 1
        else:
            if self.left.height > self.right.height:
                self.height = self.left.height + 1
            else:
                self.height = self.right.height + 1

    def add_height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node)."""
        if self.is_leaf():
            self.height = 0
        elif not self.contains_left_node():
            self.height = self.right.height + 1
        elif not self.contains_right_node():
            self.height = self.left.height + 1
        else:
            if self.left.height > self.right.height:
                self.height = self.left.height + 1
            else:
                self.height = self.right.height + 1

    def left_rotation(self):
        """ Set the original root as the left child of the original roots right
        child. Then return the original roots right child as the new root. """
        right_child = self.right
        self.right = right_child.left
        right_child.left = self
        self.get_height()
        right_child.get_height()
        return right_child

    def right_rotation(self):
        # Same as left_rotation just reversed
        left_child = self.left
        self.left = left_child.right
        left_child.right = self
        self.get_height()
        left_child.get_height()
        return left_child