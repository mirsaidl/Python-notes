#Libraries learned from lesson
import random
import statistics
import sys

coin = random.choice(["H" , "T"]) # randomize list
number = random.randint(1, 100) # nums

cards = ["jack", "quenn", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)

print(coin , number , sep = "/")


print("\n", statistics.mean([100,95])) 

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is " , arg)
 

