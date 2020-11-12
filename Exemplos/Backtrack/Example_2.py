import re

str = "8170180;Jessica Beatriz;F;21;912345678"

pattern = re.compile(r'^(?P<pri>.*);(?P<tlf>\d{9}$)')

if pattern.match(str):
    print("Match")
    print(pattern.sub(r"\g<pri>;00351\g<tlf>", str))

else:
    print("Doesn't match")