from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        import numpy as np
        import pandas as pd

        dic = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
                        'Jonas'], 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
               'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
               'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        res = solution(dic)

        self.assertEqual(res['name'][0], 'Jonas')
        self.assertEqual(res.shape, (1, 4))

