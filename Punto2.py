import re


patron = re.compile(r'\(?[0-9]+\ ?(\+|\-|\*|\/)\ ?[0-9]+\)?')
while True:
    a = input("Ingrese la string: ")
    if patron.match(a):
        try:
            a = eval(a)
            print("True", a)
        except:
            b = False
            print(b, type(b))
    else:
        print("False")
