
sub = 75958264
plu = 589617596
lis = []


def encoder(what):

    for l in what:
        l = ord(l)
        l = l + plu - sub
        lis.append(l)

    return list(lis)


def decoder(now_what):

    xter = []

    for l1 in now_what:

        l1 = chr(l1 - plu + sub)

        xter.append(l1)

    nxter = str(xter).translate(str.maketrans("", "", "[],\'")).replace("  ", '^').replace(" ", '').replace("^", ' ')

    return str(nxter)


