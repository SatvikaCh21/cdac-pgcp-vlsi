import re

def find_dates(text):
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    match = re.search(pattern, text)
    if match:
        print(match.group())
    else:
        print("No date found.")
find_dates("The event is on 09-24-2026")
find_dates("Her birthday was on 12-31-1999.")
find_dates("No date here.")