import random as r

def son_me():
    son = r.randint(1, 10)
    print("1 dan 10 gacha son o'yladim). Topa olasizmi?")
    for peop in range(10):
        guess = int(input('>>> '))
        if son > guess:
            print("Xato. Men o'ylagan son bundan kattaroq")
        elif son < guess:
            print("Xato. Men o'ylagan son bundan kichikroq")
        else:
            print(f"TOPDINGIZ.{son} ni o'ylagan edim. Siz buni {peop+1} ta urinishda topdingiz. Tabriklayman")
            break
     
    return peop + 1

