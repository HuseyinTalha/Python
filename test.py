import re

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
        False






