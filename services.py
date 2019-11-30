import requests
from requests.exceptions import ConnectionError

prefixes = []

with open("resources/prefixes.txt", "r") as f:
    for line in f:
        prefixes.append(line.strip())

def get_business_sector(number):
    result = {}
    try:
        response= requests.get(f"https://challenge-business-sector-api.meza.talkdeskstg.com/sector/{number}")
    except ConnectionError:
        result

    return response.json().get("sector")

def standardize_number(number_string):
    tmp_number = number_string.replace(" ", "")
    if tmp_number.startswith("+"):
        tmp_number = tmp_number[1:]
    if tmp_number.startswith("00"):
        tmp_number = tmp_number[2:]
    return tmp_number

def aggregate_telephone_numbers(numbers_list):
    result = {}
    for number in numbers_list:
        standardized_number = standardize_number(number)
        for prefix in prefixes:
            if standardized_number.startswith(prefix):
                result[prefix] = result.get(prefix, {})
                sector = get_business_sector(number)
                result[prefix][sector] = result[prefix].get(sector, 0) + 1
                continue
    return result
