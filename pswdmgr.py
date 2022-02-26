def main():
    menu = """Please choose what you want to do:
1) query account / password
2) add account / password
0) exit."""

    while True:
        print(menu)
        n = int(input())
        if n == 1:
            print("Please input the key.")
            key = input()
            print("Evan 123456")
        elif n == 2:
            print("Please input the account.")
            a = input()
            print("Please input the password.")
            p = input()
            print(a, p)
        elif n == 0:
            print("byebye")
            break
        else:
            print("input error")

if __name__ == '__main__':
    main()