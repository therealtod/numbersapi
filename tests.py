from unittest import TestCase
from unittest import mock

from services import *


class TestServices(TestCase):
    def test_standardize_numbers_with_plus(self):
        number = "+9872349"
        standardized_number = standardize_number(number)
        self.assertEqual(standardized_number,"9872349")
    
    def test_standardize_numbers_with_spaces(self):
        number = "1 7490276403"
        standardized_number = standardize_number(number)
        self.assertEqual(standardized_number,"17490276403")
    
    def test_standardize_numbers_with_plus_and_spaces(self):
        number = "+1 7490276403"
        standardized_number = standardize_number(number)
        self.assertEqual(standardized_number,"17490276403")
    
    def test_standardize_numbers_with_prependend_00(self):
        number = "001382355"
        standardized_number = standardize_number(number)
        self.assertEqual(standardized_number,"1382355")
    
"""
    def test_aggregate_telephone_numbers(self):
        numbers = ["+1983248", "001382355", "+147 8192", "+4439877"]
        expected = {
            "1": {
                "Technology": 2,
                "Clothing": 1
                },
                "44": {
                    "Banking": 1
                    }
                }
        aggregated_numbers = aggregate_telephone_numbers(numbers)
        self.assertEqual(aggregated_numbers, expected)
"""