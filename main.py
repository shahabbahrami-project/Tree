class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while temp is not None:
            if new_node.value == temp.value:
                return False
            if temp.value > value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
             return False
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            if temp.value > value:
                if temp.left is None:
                    return False
                temp = temp.left
            else:
                if temp.right is None:
                    return False
                temp =temp.right
        return False
tree=BST()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
print(tree.contains(17))
