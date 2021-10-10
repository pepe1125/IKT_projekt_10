def osszeg(a,b):
    print('A két szám összege: ', a+b)

# Input1
while True:
    szam1 = input('Add meg az egyik számot: ')
    try:
        # Convert it into integer
        val = int(szam1)
        print("OK -» ez egy egész szám = ", val)
        szam1 = val
        break
    except ValueError:
        try:
        # Convert it into float
            val = float(szam1)
            print("OK -» ez egy tizedes szám = ", val)
            szam1 = val
            break
        except ValueError:
            print("Számot írj már be! ")

# Input2
while True:
    szam2 = input('Add meg a másik számot: ')
    try:
        # Convert it into integer
        val = int(szam2)
        print("OK -» ez egy egész szám = ", val)
        szam2 = val
        break
    except ValueError:
        try:
        # Convert it into float
            val = float(szam2)
            print("OK -» ez egy tizedes szám = ", val)
            szam2 = val
            break
        except ValueError:
            print("Számot írj már be! ")

osszeg(szam1,szam2)