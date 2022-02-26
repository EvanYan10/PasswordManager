import os

def main():
    menu = """Please choose what you want to do:
1) query account / password
2) add account / password
0) exit."""

    while True:
        print(menu)
        n = int(input())
        os.system('cls')
        if n == 1:
            print("Your status: QUERYING")
            print("Please input the key.")
            key = input()
            print("Your account is: Evan \nYour password is: 123456")
        elif n == 2:
            print("Your status: ADDING")
            print("Please input the key.")
            k = input()
            print("Please input the account.")
            a = input()
            print("Please input the password.")
            p = input()
            print("Your key is:", k, "Your account is:", a,"Your password is:", p)
        elif n == 0:
            print("byebye")
            break
        else:
            print("input error")
            os.system('cls')

if __name__ == '__main__':
    main()