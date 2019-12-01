from unittest import TestCase
from unittest import mock
import timeit

from services import *


class TestServices(TestCase):
    def test_standardize_numbers_with_plus(self):
        number = "+9872349"
        standardized_number = standardize_number(number)
        self.assertEqual(standardized_number, "9872349")

    def test_standardize_numbers_with_spaces(self):
        number = "1 7490276403"
        standardized_number = standardize_number(number)
        self.assertEqual(standardized_number, "17490276403")

    def test_standardize_numbers_with_plus_and_spaces(self):
        number = "+1 7490276403"
        standardized_number = standardize_number(number)
        self.assertEqual(standardized_number, "17490276403")

    def test_standardize_numbers_with_prepend_00(self):
        number = "001382355"
        standardized_number = standardize_number(number)
        self.assertEqual(standardized_number, "1382355")

    @mock.patch("services.get_business_sector")
    def test_aggregate_telephone_numbers(self, mock_get_busines_sector):
        def get_business_sector_side_effect(n):
            if n in ("+1983248", "001382355"):
                return "Technology"
            if n == "+147 8192":
                return "Clothing"
            if n == "+4439877":
                return "Banking"

        mock_get_busines_sector.side_effect = get_business_sector_side_effect

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
        aggregated_numbers = aggregate_telephone_numbers_trie(numbers)
        self.assertEqual(aggregated_numbers, expected)
    

    def test_aggregate_telephone_numbers_performance(self):
        elapsed_time = timeit.timeit(self.test_aggregate_telephone_numbers, number=100)/100
        print (elapsed_time)
