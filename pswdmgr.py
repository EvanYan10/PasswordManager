def main():
    print("Please choose what you want to do. 1 for querying the passwords. 2 for adding passwords. 0 for exit.")
    n = int(input())
    if n == 1:
        print("Evan 123456")
    elif n == 2:
        a = input()
        p = input()
        print(a, p)
    elif n == 0:
        print("byebye")
    else:
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