import time
import os
os.system('cls')

def gyertya (x):
    if (x==1):
        print(r"""
 ___)__
| Béke |
|      |
|      |
|      |
'------'
 """)

    elif (x==2):
        print(r"""
 ___)__   ___)__
| Béke | | Hit  |
|      | |      |
|      | |      |
|      | |      |
'------' '------'
 """)

    elif (x==3):
        print(r"""
 ___)__   ___)__   ___)__
| Béke | | Hit  | |Szere-|
|      | |      | |  tet |
|      | |      | |      |
|      | |      | |      |
'------' '------' '------'
 """)

    elif (x==4):
        print(r"""
 ___)__   ___)__   ___)__   ___)__ 
| Béke | | Hit  | |Szere-| |Remény|
|      | |      | |  tet | |      |
|      | |      | |      | |      |
|      | |      | |      | |      |
'------' '------' '------' '------'
 """)

    else:
        print("Max 4 gyertya lehet!!!")


nap = input('December hanyadika van? ')
nap = int(nap)

kari = 24-nap
print(f"\n{kari} nap van még karácsonyig. ÉRTED??? MÉG {kari} NAP VAN!!!\n ")

input('A továbblépéshez üss le egy ENTERT! ')

if (kari<6):
    for x in range(4):
        os.system('cls')
        gyertya(x+1)
        time.sleep(1)
elif (5<kari<13):
    for x in range(3):
        os.system('cls')
        gyertya(x+1)
        time.sleep(1)
elif (12<kari<20):
    for x in range(2):
        os.system('cls')
        gyertya(x+1)
        time.sleep(1)
else :
        os.system('cls')
        gyertya(1)
        time.sleep(1)
