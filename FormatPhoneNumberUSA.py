def FormatPhones:
    
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    code = ''
    prefix = ''
    suffix = ''

    for c in n[0:3]: code = code + str(c)
    for p in n[3:6]: prefix = prefix + str(p)
    for s in n[6:]: suffix = suffix + str(s)

    return("({}) {}-{}".format(code,prefix,suffix))

