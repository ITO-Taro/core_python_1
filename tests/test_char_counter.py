import unittest
from python_core_exercise import PythonCoreExercise

class PythonCoreExerciseCharCounterTests(unittest.TestCase):
    testInput = "P@#yn26at^&i5ve"

    @classmethod
    def setUpClass(cls):
        cls.func = PythonCoreExercise()
    
    def test_char_counter(self):
        """ tests if the returned values are correct """
        res = self.func.char_counter(self.testInput)
        self.assertEqual((res['chars'], res['digits'], res['symbol']), (8,3,4))



if __name__ == '__main__':
    unittest.main()