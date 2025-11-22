n = input()
if n[-1] == '0' or n[-1] == '5' or n[-1] == '7' or (n[-1] == '2' and n != '2') or int(n) % 7 == 0:
    print('да')
else:
    print('нет')