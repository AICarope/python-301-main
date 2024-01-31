# Write a unittest test suite to test the rescrape module

import unittest
import rescrape



def test_get_recepie(self):
        
        test_url = "https://codingnomads.github.io/recipes/"
        result = get_data_from_url(test_url)
        self.assertIsNotNone(result, "The function should return some data.")