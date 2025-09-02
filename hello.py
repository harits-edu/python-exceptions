def main():
    num = get_int("What's the number? ")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            #pass
            print("It's not a number!")

main()