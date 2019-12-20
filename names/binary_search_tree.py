class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Time complexity: O(log n) avg
    def insert(self, value):
        # if there is no root
        if not self.value:
            self.value = value
        # if value is smaller, go left
        elif value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # if value is greater, go right
        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    
    # Time complexity: O(log n) avg
    def contains(self, target):
        current = self
        # base case
        if target == self.value:
            return True 
        elif target < self.value:
            if self.left == None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right == None:
                return False
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()