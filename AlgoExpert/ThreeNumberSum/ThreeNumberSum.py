import unittest


def threeNumberSum(array, targetSum):
    resultsDic = {} 
    triplets = []
    array.sort()
    
    for i in range(len(array)):
        resultsDic[targetSum - array[i]] = array[i]
        
    for i in range(len(array)):
       for j in range(len(array)): 
           sum = array[i] + array[j]
           if sum in resultsDic:
               if array[i] != resultsDic[sum] and array[j] != resultsDic[sum] and array[i] != array[j]:
                   values = [array[i], array[j], resultsDic[sum]]
                   values.sort()
                   if values not in triplets:
                       triplets.append(values)
                   

    return triplets




class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0),
            [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]],
        )


if __name__ == "__main__":
    unittest.main()