import unittest

def twoNumberSum(array, targetSum):

    differences = {
        
    }

    for i in range(len(array)):
        differences[array[i]] = True


    for i in range(len(array)):
        x = targetSum - array[i]

        if(x in differences and x != array[i]): return [x, array[i]]
        
    

    

    
    return []



class TestTwoNumberSumFunction(unittest.TestCase):
    def test_1(self):
        output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)




if __name__ == "__main__":
    unittest.main()