from peop import son_me
from comp import son_pc

while True:
    peop = son_me()
    comp = son_pc()                
    if comp < peop:
      print(f"Bu o'yinda kompyuter {comp} taxmin bilan yutdi. Keyingi uyinlarda omad!")
    elif comp > peop:
      print(f"Tabriklayman siz {peop} taxmin bilan g'alaba qozondingiz!")
    else:
      print('Durrang')

    savol = input("Yana o'ynaysizmi? (ha/yoq)")
    if savol == 'ha':
       continue
    else:
       break

      




           
                 
        
       