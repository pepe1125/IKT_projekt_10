x = int(input('Mennyi az idő? '))
if 7 < x < 14:
    print('nyitva még:', 14 - x , 'óráig...')
else:
    print('zárva')
    if x>14:
        print(31 - x , 'óra múlva lesz nyitva!')
    else:
        print( 7 - x , 'óra múlva lesz nyitva!')
