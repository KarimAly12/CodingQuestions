import math
import copy
import unittest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):


        
    closest = math.inf
    closestNode = 0
    return findClose(tree, target, closest, closestNode)

        

    


        

def findClose(tree, target, closest, closestNode):
    
    if target == tree.value:
        return tree.value

    
    currentNode = tree
    closeValue = closest
    node = closestNode
    

    if target > currentNode.value:
        currentNode = currentNode.right
    elif target < currentNode.value:
        currentNode = currentNode.left


    if currentNode == None:
        return node
    else:
        diff = abs(currentNode.value - target)
        if  closeValue > diff:
            closeValue = diff
            node = currentNode.value

    return findClose(currentNode, target, closeValue, node)



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)
        

    

if __name__ == "__main__":
    unittest.main()