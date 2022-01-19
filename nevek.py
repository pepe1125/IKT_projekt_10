user = ["Alex", "Martin", "Sanyi", "Réka"]
list_size = len(user)
chk =  [None] * list_size

print(f'\nAdd meg a {list_size} megfelelő nevet!\n')

while True:
    name = input("Név? ")
    if not name in user: 
        print('--- Nem megfelelő név!  ÚJRA! ---')
    for i in range(list_size):
        if name == user[i]: 
            chk[i] = True
        if chk[i]:
            print(i+1, end="")
            print(". név:", user[i])
    if all(chk):
        print('\n---- Belépés engedélyezve: ----\nSziasztok',', '.join(user),'!','\n-------------------------------\n')
        break
