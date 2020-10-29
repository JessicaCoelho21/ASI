import calc
from calc import soma
import show

c = 4
d = 7

r1 = soma(c, d)
r2 = calc.sub(c, d)
r3 = calc.mul(c, d)
r4 = calc.div(c, d)

show.result(r1)

print(r2, ",", r3, ",", r4)
