import Percentage
import ReadLogFile
import Stats

# a)
# out = Percentage.calculoPercentagem()
# print(out)


# b)
mod = ReadLogFile.ler()
#print(mod)

# c)
# Stats.Alarm()

# d)
t, o = Stats.Total(mod)
print(t)
print(o)