import unittest

def sortedSquaredArray(array):
    # Write your code here.


    start = 0
    end = len(array) - 1

    squaredList = [0] * len(array)

    i = len(array) -1
    
    while(i >= 0):
        

        if abs(array[start]) > abs(array[end]):
            squaredList[i] = array[start] ** 2
            start += 1
        else:
            squaredList[i] = array[end] ** 2
            end -= 1
        

        i -= 1
        
            

        
    return squaredList


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()