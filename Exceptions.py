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






