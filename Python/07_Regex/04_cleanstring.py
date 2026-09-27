import re
def clean_string(text):
    cleaned1= re.sub(r'\s+', ' ', text)
    cleaned2= re.sub(r'^\s+|\s+$', '', text)
    result = re.sub(r'(^\s*\w|[.!?]\s*\w)', lambda m: m.group().upper(), text)
    return result, cleaned1, cleaned2

text = "  hello   world.  how are you  "
print(clean_string(text))