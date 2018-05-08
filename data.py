data = open('./featuresdf.csv').read()
newdata = ''

for i in range(100):
    newdata += data

open('hi.csv', 'w+').write(newdata)
