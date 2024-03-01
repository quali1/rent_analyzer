import json
import re


class DataAnalyzer:
    @staticmethod
    def extract_numbers(text):
        numbers = re.findall(r'\d+\.*\d*', text)
        return [float(num) for num in numbers]

    @staticmethod
    def calculate_profitability(apartments, finish=None):
        # Calculate profitability...
        for apartment in apartments:
            apartment['price'] = DataAnalyzer.extract_numbers(apartment['price'])[0]
            apartment['price_per_sqm'] = DataAnalyzer.extract_numbers(apartment['price_per_sqm'])[0]

        sorted_apartments = sorted(apartments, key=lambda x: x['price_per_sqm'])

        return sorted_apartments[:finish]

    @staticmethod
    def analyze_apartments(path):
        data = open(path, "r")
        otodom_data = json.loads(data.read())["otodom_data"]

        apartments = []
        for page_data in otodom_data.values():
            if isinstance(page_data, list):
                apartments.extend(page_data)

        most_profitable = DataAnalyzer.calculate_profitability(apartments, 5)
        return most_profitable
