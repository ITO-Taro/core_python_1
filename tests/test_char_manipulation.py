import unittest
from python_core_exercise import PythonCoreExercise

class PythonCoreExerciseCharCounterTests(unittest.TestCase):
    testInput0 = ["python", "Python"]
    testInput1 = ["geek", "gesek"]
    testInput2 = ["cut", "cat"]
    testInput3 = ["sunday", "saturday"]
    testInput4 = ["money", "monkey"]

    @classmethod
    def setUpClass(cls):
        cls.func = PythonCoreExercise()
    
    def test_char_manipulatuon0(self):
        """ tests if it correctly converts the first value to the second in testInput1 """
        self.assertEqual(self.func.char_manupilation(self.testInput0[0], self.testInput0[0]), "python")

    def test_char_manipulation1(self):
        """ tests if it correctly converts the first value to the second in testInput1 """
        self.assertEqual(self.func.char_manupilation(self.testInput1[0], self.testInput1[1]), "gesek")
    
    def test_char_manipulation2(self):
        """ tests if it correctly converts the first value to the second in testInput2 """
        self.assertEqual(self.func.char_manupilation(self.testInput2[0], self.testInput2[1]), "cat")
    
    def test_char_manipulation3(self):
        """ tests if it correctly converts the first value to the second in testInput2 """
        self.assertEqual(self.func.char_manupilation(self.testInput3[0], self.testInput3[1]), "saturday")
    
    def test_char_manipulation4(self):
        """ tests if it correctly converts the first value to the second in testInput2 """
        self.assertEqual(self.func.char_manupilation(self.testInput4[0], self.testInput4[1]), "monkey")

if __name__ == '__main__':
    unittest.main()