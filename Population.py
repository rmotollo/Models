#def nb_year(p0, percent, aug, p):

p0 = 1500
percent = 0.05
aug = 100
p = 5000
countyears = 0

while p0 < p :

    p0 = p0 + (p0*percent) + aug
    countyears += 1

print(countyears)
