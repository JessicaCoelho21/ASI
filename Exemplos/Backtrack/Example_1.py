import re

str = "8170180;Jessica Beatriz"

pattern = re.compile(r'^(?P<numero>.*);(?P<nome>.*)$')
print(pattern.sub(r"\g<nome>;\g<numero>", str))