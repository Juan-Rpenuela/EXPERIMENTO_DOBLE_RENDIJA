import unittest
import matplotlib.pyplot as plot
import saltoalocuant as sac
import math

class TestSalto_Clasico_Cuantico(unittest.TestCase):
    def test_experimentorendijas(self):
                blancos1 = 5
                rendijas1 = 2
                resultm = ([[0, 0, 0, 0, 0, 0, 0, 0], [0.5, 0, 0, 0, 0, 0, 0, 0], [0.5, 0, 0, 0, 0, 0, 0, 0], [0, 0.33, 0, 1, 0, 0, 0, 0], [0, 0.33, 0, 0, 1, 0, 0, 0], [0, 0.33, 0.33, 0, 0, 1, 0, 0], [0, 0, 0.33, 0, 0, 0, 1, 0], [0, 0, 0.33, 0, 0, 0, 0, 1]], [0.0, 0.0, 0.0, 0.165, 0.165, 0.33, 0.165, 0.165])
                resultc = sac.ExperimentoRendijas(blancos1,rendijas1)
                self.assertEqual(resultm, resultc)

    def test_experimentorendijas_2(self):
                blancos2 = 6
                rendijas2 = 3
                resultm = ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0.33, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0.33, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0.33, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0.5, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0.5, 0.5, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0.5, 0.5, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0.5, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], [0.0, 0.0, 0.0, 0.0, 0.165, 0.33, 0.33, 0.165, 0.0, 0.0])
                resultc = sac.ExperimentoRendijas(blancos2,rendijas2)
                self.assertEqual(resultm, resultc)
                
if __name__ == "__main__":
        unittest.main()
