import re
import sys

pattern = "([A-Za-z]+.)\t"
pattern2 = "(.*)\t"

with open("silverLining.txt", "r", encoding="utf-8") as original:
    reader = original.read()
    extracted = re.findall(pattern2, reader)
    for i in range(len(extracted)):
        print(extracted[i])