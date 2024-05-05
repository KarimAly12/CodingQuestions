import unittest


def transposeMatrix(matrix):

    transposedMatrix = []
    rows = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if rows != len(matrix[i]):
                transposedMatrix.append([])
                rows += 1
            transposedMatrix[j].append(matrix[i][j])


    
    return transposedMatrix


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        actual = transposeMatrix(input)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()