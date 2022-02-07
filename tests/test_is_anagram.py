import unittest
from python_core_exercise import PythonCoreExercise

class PythonCoreExerciseCharCounterTests(unittest.TestCase):
    testStrings = """arc = car
    brag = grab
    bored = robed
    cat = act
    cider = cried
    dusty = study
    elbow = below
    inch = chin
    night = thing
    peach = cheap
    players = parsley
    sadder = dreads
    save = vase
    state = taste"""

    @classmethod
    def setUpClass(cls):
        cls.func = PythonCoreExercise()
    
    def clean_text(self):
        return [i.replace(" ", "").split("=") for i in self.testStrings.replace("\n", "").split("   ")]

    
    def test_cis_anagram(self):
        """ tests if it correctly converts the first value to the second in testInput1 """
        strings = self.clean_text()
        for i in strings:
            return self.assertEqual(self.func.is_anagram(i[0], i[1]), True)

   
if __name__ == '__main__':
    unittest.main()