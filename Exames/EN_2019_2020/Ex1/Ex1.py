import re
str="joaosilva@gmail.com,BrIncaR2017!,23/12/2019"
data = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
pattern = re.compile(r'^([\w]*@[a-z]*.[a-z]*),([\w\!\_\?]*),(?P<dia>\d{2})/(?P<mes>\d{2})/(?P<ano>\d{4})$')
res = pattern.match(str)

print(res.group(1, 2, 'dia', 'mes', 'ano'))

if res:
	if int(res.group('ano')) > 1970 and int(res.group('ano')) < 2020 and int(res.group('mes')) > 0 and int(res.group('mes')) < 13 and int(res.group('dia')) <= data[res.group('mes')]:
		print( "OK")
	else:
		print("NOK")
		
else:
	print("falhou")
	