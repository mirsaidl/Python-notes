import random as r

def son_pc():
    comp_guess = list(range(1,11))
    comp = 0
    input("Son o'ylagan bo'lsangiz hohlagan tugmangizni bosing!")
    ishora = True
    while ishora:
       comp += 1
       guess1 = r.choice(comp_guess)
       savol = input(f"Siz {guess1} sonini o'yladingiz. to'gri (T) , men o'ylagan son bundan kattaroq (+) , men o'ylagan son bundan kichikroq (-)")
       if savol == 'T':
           print(f"Tabriklayman topdingiz. Siz buni {comp} taxminlar bilan topdingiz.")
           ishora = False
       elif savol == '+': 
           comp_guess = [x for x in comp_guess if x > guess1]
       elif savol == '-':
            comp_guess = [x for x in comp_guess if x < guess1]
     
    return comp

