import re

str = "8170180;Jessica Beatriz;F;21;912345678"

pattern = re.compile(r'^(.*);(\d{9}$)')

if pattern.match(str):
    print("Match")
    print(pattern.sub(r"\1;00351\2", str))

else:
    print("Doesn't match")