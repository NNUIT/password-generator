import random

def main():
    print("Welcome to Password Generator v.1")
    print("Please configure settings")

    lenght = int(input("Length: "))
    is_num = int(input("Should it contain numbers? (0-1): "))
    is_cap = int(input("Should it contain capital letters? (0-1): "))
    is_spec = int(input("Should it contain special symbols? (0-1): "))
    num = int(input("Number of passwords: "))

    allowed_symbols = "abcdefghijklmnopqrstuvwxyz"

    if is_num:
        allowed_symbols += '0123456789'
    if is_cap:
        allowed_symbols += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if is_spec:
        allowed_symbols += "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


    with open('passwords.txt', 'w') as file:
        for _ in range(num):
            password = ''.join(random.choice(allowed_symbols) for _ in range(lenght))
            file.write(password + '\n')
    
    print(f"Done. {num} passwords generated and written in 'passwords.txt'.")


if __name__ == "__main__":
    main()