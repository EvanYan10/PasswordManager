import os
import filemgr

def main():
    menu = """Please choose what you want to do:
1) query account / password
2) add account / password
0) exit."""

    while True:
        print(menu)
        try:
            n = int(input())
            os.system('cls')
            if n == 1:
                print("Your status: QUERY")
                print("Please input the key.")
                key = input()
                print("Your account is: Evan \nYour password is: 123456")
            elif n == 2:
                print("Your status: ADD")
                print("Please input the key.")
                while True:
                    k1 = input()
                    k2 = input()
                    if k1 == k2:
                        break
                    os.system('cls')
                    print("Please input the same keys.")
                print("Please input the account.")
                while True:
                    a1 = input()
                    a2 = input()
                    if a1 == a2:
                        break
                    os.system('cls')
                    print("Please input the same accounts.")
                print("Please input the password.")
                while True:
                    p1 = input()
                    p2 = input()
                    if p1 == p2:
                        break
                    os.system('cls')
                    print("Please input the same passwords.")
                print("Your key is:", k1, "Your account is:", a1,"Your password is:", p1)
            elif n == 0:
                print("byebye")
                break
        except:
            print("Opps! Sounds like the thing you input is wrong. Byebye!")
            break

if __name__ == '__main__':
    if filemgr.open_db():
        main()
    else:
        print("Opps! Sounds like something's wrong. Byebye!")