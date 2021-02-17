import ephem
import datetime

now = datetime.datetime.now()
data = now.strftime('%Y/%m/%d')
print(data)
print(ephem._libastro.builtin_planets())
b = 'Jupiter'
c = getattr(ephem, b)
print(c)
print(ephem.constellation(c(data)))



