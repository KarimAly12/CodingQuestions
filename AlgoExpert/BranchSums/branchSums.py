import unittest

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):

    total = 0
    
    list = []

    branchSum(root, total, list)

    return list
    




def branchSum(node, total, list):
    
    total += node.value
    
    if node.left == None and node.right == None:
        list.append(total)
        return

    if node.left != None:
        branchSum(node.left, total, list)

    if node.right != None:
        branchSum(node.right, total, list)
        
        
