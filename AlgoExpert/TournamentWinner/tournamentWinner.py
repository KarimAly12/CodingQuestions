import unittest

def tournamentWinner(competitions, results):
    # Write your code here.


    comp = {}
    score = 0
    winner = ""

    for i in range(len(results)):

        if not competitions[i][0] in comp:
            comp[competitions[i][0]] = 0

        
        if not competitions[i][1] in comp:
            comp[competitions[i][1]] = 0
            

            
        if results[i] == 1:
            comp[competitions[i][0]] += 3
        if results[i] == 0:
            comp[competitions[i][1]] += 3

        if(comp[competitions[i][0]] > score):
            winner = competitions[i][0]
            score = comp[competitions[i][0]]

        if(comp[competitions[i][1]] > score):
            winner = competitions[i][1]
            score = comp[competitions[i][1]]
            
        
    return winner


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()