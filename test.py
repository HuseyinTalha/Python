'''import re

while (True):
    a_string = input("gir")

    if not (re.findall(r'[a-zA-Z]', a_string)):
        a_list = [x for x in a_string]
        mapobject = map(int, a_list)
        intlist = list(mapobject)
        for a, b in enumerate(intlist):
            continue
        else:
            print(intlist, a)
            print(type(a))


    else:
        False'''

import re
while True:
    a_string = input("gir")
    sonuc = []


    if not (re.findall(r'[a-zA-Z]', a_string)):
        a_list = [x for x in a_string]
        mapobject = map(int, a_list)
        intlist = list(mapobject)
        for i in range(len(intlist)):
            if intlist[i] % 2 != 0:
                if intlist[i+1] % 2 != 0:
                    sonuc.append(intlist[i])
                    sonuc.append("-")
                    sonuc.append(intlist[i+1])


            elif intlist[i] % 2 ==0 or intlist[i+1] % 2 !=0:
                sonuc.append(intlist[i])
                sonuc.append(intlist[i+1])
            print(sonuc)







