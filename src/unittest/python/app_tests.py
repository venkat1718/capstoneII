# Python code to demonstrate working of unittest 
import sys
sys.path.insert(0, '../../main/python/')
# import OBD
import app
import unittest
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt


# input_image_names = ['../resources/images/input/test.png',
# 					'../resources/images/input/Clear1.jpg',
# 					'../resources/images/input/GaussianNoise1.jpg',
# 					'../resources/images/input/saltNpepper1.jpg',]

class TestApp(unittest.TestCase): 
      
    def setUp(self): 
        pass

    # Returns True if the string contains 4 a. 
    def test_addition(self):
        result = app.addition(3,5)
        self.assertEqual(result, 8)

    # Returns True if the string is in upper case. 
    def test_division(self):
        result1 = app.division(17, 2)
        result2 = app.division(5, 19)
        self.assertEqual(result1, 8)
        self.assertEqual(result2, 3)

    def testHello(self):
        result = app.hello()
        self.assertEqual(result, "Hello World! 3 1 2")
    # Returns TRUE if the string is in uppercase 
    # else returns False. 
    # def test_Boundary(self):         
    #     self.assertEqual() 
    #     self.assertFalse('Foo'.isupper()) 

if __name__ == '__main__': 
    unittest.main() 