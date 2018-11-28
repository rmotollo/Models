decimal =[255,255,255]
listhex = []
while decimal >= 16:
    listhex.append(decimal % 16)
    decimal = decimal // 16
listhex.append(decimal)
listhex.reverse()
for i in listhex:
    if i == 10: listhex[listhex.index(i)] = 'A'
    elif i == 11: listhex[listhex.index(i)] = 'B'
    elif i == 12: listhex[listhex.index(i)] = 'C'
    elif i == 13: listhex[listhex.index(i)] = 'D'
    elif i == 14: listhex[listhex.index(i)] = 'E'
    elif i == 15: listhex[listhex.index(i)] = 'F'
    else: continue
hexadecimal = ''

for x in list: hexadecimal += x

print(hexadecimal)
