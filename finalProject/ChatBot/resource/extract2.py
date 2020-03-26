import re
import sys

def convert(s):
    new = ""
    for x in s:
        new += x
    return new

pattern = "[A-Za-z \s . ' , ! ? ]"

with open("silverLining.txt", "r", encoding="utf-8") as original:
    result = re.sub(r'\[.*?\]', "", original.read())
    result = re.sub(r"......\t", "", result)

    english = re.findall(pattern, result)
    final = convert(english).strip()
    final = re.sub("[^\w]", " ", final)
    print(final)