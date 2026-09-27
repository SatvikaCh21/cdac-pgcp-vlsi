import re
import string
def remove_punctuation(text):
    no_punct = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text)
    cleaned = re.sub(r'\s+', ' ', no_punct)
    return cleaned.strip()
text = "Hello,World!This is amazing...isn't it?"
print(remove_punctuation(text))