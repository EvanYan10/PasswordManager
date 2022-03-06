db_file = 'pwdmgr.db'

def open_db() -> bool:
    try:
        with open(db_file) as f:
            content = f.readlines()
            if (len(content) != 0):
                mp = input("Please input the master password: ")
                if mp == content[0]:
                    print("Password is correct!")
                    return True
                else:
                    print("Password incorrect!")
                    return False
            else:
                raise Exception("master password does not exist!")
    except:
        with open(db_file, 'w') as f:
            print(f"Init {db_file}")
            while True:
                p1 = input("Please input the master password: ")
                p2 = input("Please input the master password again: ")
                if p1 == p2:
                    break
                else:
                    print("Please input the same passwords.")
            f.write(p1)
            print("The password has been written in the file.")
        return True


if __name__ == '__main__':
    open_db()
