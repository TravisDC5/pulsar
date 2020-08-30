import pandas as pd 

clever = ["Eric"]
ascValue = []

for name in clever:
    for ch in name:
        ascValue.append(ord(ch))

charCount = len(ascValue)
valSum = sum(ascValue)

value = valSum/charCount

print(value)