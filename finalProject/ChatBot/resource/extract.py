import re

pattern = r"([A-Za-z \s \n]*)"

with open("corona.txt", "r", encoding="utf-8") as original:
    text = original.read()
    extract = re.findall(pattern, text)
    for i in range(len(extract)):
        print(extract[i], end="")

