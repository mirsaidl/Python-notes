<<<<<<< HEAD
def get_in(prompt):
    while True:     
        try:
            return int(input(prompt))
        except ValueError:
            pass
    
def main():
    x = get_in("What's x? ")
    print(f"x is {x}")

main()






=======
def get_in(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
    
def main():
    x = get_in("What's x? ")
    print(f"x is {x}")

main()






>>>>>>> 28945ad6dfd40fd5155079a8e96b4aa711615d98
