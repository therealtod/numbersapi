import requests
from requests.exceptions import ConnectionError
from pytrie import StringTrie

import logging

logger = logging.getLogger()

"""
prefixes = []

with open("resources/prefixes.txt", "r") as f:
    for line in f:
        prefixes.append(line.strip())
"""


prefixes = StringTrie()

with open("resources/prefixes.txt", "r") as f:
    for line in f:
        line = line.strip()
        prefixes[line] = line


def get_business_sector(number):
    response = requests.get(f"https://challenge-business-sector-api.meza.talkdeskstg.com/sector/{number}")
    return response.json().get("sector")

def standardize_number(number_string):
    tmp_number = number_string.replace(" ", "")
    if tmp_number.startswith("+"):
        tmp_number = tmp_number[1:]
    if tmp_number.startswith("00"):
        tmp_number = tmp_number[2:]
    return tmp_number

def aggregate_telephone_numbers_naive(numbers_list):
    result = {}
    for number in numbers_list:
        standardized_number = standardize_number(number)
        for prefix in prefixes:
            if standardized_number.startswith(prefix):
                result[prefix] = result.get(prefix, {})
                try:
                    sector = get_business_sector(number)
                except ConnectionError as err:
                    result = {
                        "error": str(err)
                    }
                    return result
                result[prefix][sector] = result[prefix].get(sector, 0) + 1
                continue
    return result

def aggregate_telephone_numbers_trie(numbers_list):
    result = {}
    for number in numbers_list:
        standardized_number = standardize_number(number)
        try:
            prefix = prefixes.longest_prefix_value(standardized_number)
        except KeyError:
            logger.info("Skipping (invalid) number because it maches no prefix")
            continue
        if standardized_number.startswith(prefix):
            result[prefix] = result.get(prefix, {})
            try:
                sector = get_business_sector(number)
            except ConnectionError as err:
                result = {
                    "error": str(err)
                }
                return result
            result[prefix][sector] = result[prefix].get(sector, 0) + 1
    return result
