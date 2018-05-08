data = open('./featuresdf.csv').read()
newdata = ''

for i in range(25):
    newdata += data

open('smaller.csv', 'w+').write(newdata)
