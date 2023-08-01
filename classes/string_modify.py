from typing import List
import re

class StringModification():
    def __init__(self, data: List[List[str]]):
        self.data = data

    def _string_modify(self, string: str) -> str:
        modification = (string.strip().
            replace("Pending Approval", "Pending-Approval").
            replace("United States", "United-States").
            replace("New Caledonia", "New-Caledonia").
            replace("South Africa", "South-Africa").
            replace("Saudi Arabia", "Saudi-Arabia").
            replace("New Zealand", "New-Zealand").
            replace("United Arab Emirates", "United-Arab-Emirates").
            replace("French Polynesia", "French-Polynesia").
            replace("Bosnia and Herzegovina", "Bosnia-and-Herzegovina").
            replace("French Guiana", "French-Guiana").
            replace("Sri Lanka", "Sri-Lanka").
            replace("United Kingdom", "United-Kingdom").
            replace("Sierra Leone", "Sierra-Leone").
            replace("Faroe Islands", "Faroe-Islands").
            replace("Dominican Republic", "Dominican-Republic").
            replace("Slovak Republic", "Slovak-Republic").
            replace("Reunion Island", "Reunion-Island").
            replace("Falkland Islands", "Falkland-Islands").
            replace("Solomon Islands", "Solomon-Islands").
            replace("Brunei Darussalam", "Brunei-Darussalam").
            replace("Cayman Islands", "Cayman-Islands").
            replace("Papua New Guinea", "Papua-New-Guinea").
            replace("Cocos (Keeling) Islands", "Cocos-(Keeling)-Islands").
            replace("Korea, Republic of", "Korea-Republic-of").
            replace("Isle of Man", "Isle-of-Man").
            replace("Trinidad and Tobago", "Trinidad-and-Tobago").
            replace("St. Pierre and Miquelon", "St.-Pierre-and-Miquelon").
            replace("French Southern Territories", "French-Southern-Territories").
            replace("Costa Rica", "Costa-Rica").
            replace("Hong Kong", "Hong-Kong").
            replace("Czech Republic", "Czech-Republic").
            replace(" am ", "-am ").
            replace(" pm ", "-pm ").
            replace("  ", " None ")
            )
    
        # Use re.sub() to replace spaces with dashes in date and time
        modification = re.sub(r'\s+(\d+\/\d+\/\d+\s\d+:\d+:\d+)\s+', r'-\1-', modification)

        # Use re.sub() with capturing group and backreference to modify date and time format
        modification = re.sub(r'(\d+\/\d+\/\d+)\s(\d+:\d+:\d+)', r'\1-\2', modification)

        return modification
    
    def modify(self):
        result = []

        for elements in self.data:
            mapping = map(self._string_modify, elements)
            result.extend(list(mapping))
        
        return result