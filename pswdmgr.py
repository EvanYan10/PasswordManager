def main():
    menu = """Please choose what you want to do:
1) query account / password
2) add account / password
0) exit."""

    print(menu)

    while True:
        n = int(input())
        if n == 1:
            print("Evan 123456")
            break
        elif n == 2:
            a = input()
            p = input()
            print(a, p)
            break
        elif n == 0:
            print("byebye")
            break

if __name__ == '__main__':
    main()