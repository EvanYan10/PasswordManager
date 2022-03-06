class PasswordDB():
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.content = []

    def read_db(self) -> bool:
        """
        Read db file, and ask for the master password.
        If file or master password not exist, init the db file.
        """
        try:
            with open(self.file_path) as f:
                self.content = f.readlines()
                if self.content and len(self.content[0]) > 0:
                    mp = input("Please input the master password: ")
                    if mp == self.content[0]:
                        print("Password is correct!")
                        return True
                    else:
                        mp = input("Please try again: ")
                        if mp == self.content[0]:
                            print("Password correct!")
                            return True
                        else:
                            print("Password incorrect!")
                            return False
                else:
                    raise Exception("master password does not exist!")
        except:
            with open(self.file_path, 'w') as f:
                print(f"Init {self.file_path}...")
                while True:
                    p1 = input("Please input the master password: ")
                    p2 = input("Please input the master password again: ")
                    if p1 == p2:
                        break
                    else:
                        print("Please input the same password.")
                f.write(p1)
                print("Password DB file initialized.")
            return True

    def query_db(self, key) -> tuple[str, str]:
        return ('', '')

    def insert_db(self, key, account, pwd) -> bool:
        return False


if __name__ == '__main__':
    pdb = PasswordDB('pwdmgr.db')
    if not pdb.read_db():
        pdb.init_db()
