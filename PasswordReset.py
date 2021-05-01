import re
from time import sleep


class Reset:

    def __init__(self, myDB, myCursor, uname, uid):
        self.myDB = myDB
        self.myCursor = myCursor
        self.user = uname
        self.usid = uid

    def userInp(self):
        pswd1 = input("Enter a new password : ")
        if self.validate(pswd1):
            pswd2 = input("Re enter the same : ")
            if pswd1 == pswd2:
                self.pswdchg(pswd1)
            else:
                print("Passwords mismatch! Exiting")
                sleep(1)

    def pswdchg(self, pswd):
        old_pswd = ''
        pswd_chk = "SELECT USER_PASSWORD FROM USERLIST WHERE UID = %d " % self.usid
        try:
            self.myCursor.execute(pswd_chk)
            getpassword_result = self.myCursor.fetchall()
            if len(getpassword_result) == 0:
                old_pswd = ''
            else:
                for item in getpassword_result:
                    old_pswd = item[0]
            if old_pswd == pswd:
                print("Old and new Passwords can't be same.")
            else:
                sql_reset_pswd = "UPDATE USERLIST SET USER_PASSWORD = '%s' WHERE UID = %d" % (pswd, self.usid)
                self.myCursor.execute(sql_reset_pswd)
                self.myDB.commit()
                print("Successfully Updated Password!!")
        except Exception as e:
            print("An error occurred -", e)

    def validate(self, password):
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters.")
            self.userInp()
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it.")
            self.userInp()
        elif re.search('[A-Z]', password) is None:
            print("Make sure your password has a capital letter in it.")
            self.userInp()
        elif re.search("[a-z]", password) is None:
            print("Make sure your password has a small letter in it.")
            self.userInp()
        elif re.search("[#!|_@$]", password) is None:
            print("Make sure your password has a special character[#!|_@$] in it.")
            self.userInp()
        else:
            return True
