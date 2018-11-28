num = 413234
splitnum = []
strnum = str(num)
listsquare = []
numstr = ''
for i in strnum: splitnum.append(int(i))
for n in splitnum: listsquare.append(n**2)
for j in listsquare: numstr = numstr + str(j)

print (int(numstr))

