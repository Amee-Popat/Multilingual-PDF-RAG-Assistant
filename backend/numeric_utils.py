import re

def extract_numbers(text):
    numbers = re.findall(r'\d[\d,]*', text)
    cleaned = [int(n.replace(",", "")) for n in numbers]
    return cleaned
