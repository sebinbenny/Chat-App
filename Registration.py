from time import sleep
import random

class Home:
    def __init__(self, myDB, myCursor):
        self.myDB = myDB
        self.myCursor = myCursor

    def homeview(self):
        mob_no = int(input("Enter a 10 digit mobile number : "))
        if self.mobcheck(mob_no):
            if self.mobduplicatechk(mob_no):
                print("This mobile number is already registered.")
                sleep(2)
            else:
                user = input("Enter a username for you : ")
                print("Generating password for you. Please wait!")
                sleep(3)
                pswd_gen = self.pswdgen()
                print("Your password is", pswd_gen, "(note this securely and change later.)")
                user_op = input("Do you want to continue? (Y/N) : ")
                if user_op == 'Y':
                    self.reg(user, pswd_gen, mob_no)
        else:
            print("You entered an invalid Mobile number.")
            sleep(2)


    def pswdgen(self):
        small_letters = 'abcdefghijklmnopqrstuvwxyz'
        cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
        nums = '1234567890'
        sym = '!@#$_'
        s = small_letters + cap_letters + nums + sym
        l = 10
        pswd = "".join(random.sample(s, l))
        return pswd

    def reg(self, user, pswd, mno):
        uid = 0
        try:
            sql_c_check = "SELECT MAX(UID) FROM USERLIST"
            self.myCursor.execute(sql_c_check)
            r = self.myCursor.fetchall()
            for i in r:
                uid = i[0]
            uid += 1
            sql_reg = "INSERT INTO USERLIST (UID,USER_NAME,USER_PASSWORD,MOBILE_NO) VALUES " \
                      "(%d, '%s', '%s', '%s')" % (uid, user, pswd, mno)
            self.myCursor.execute(sql_reg)
            self.myDB.commit()
        except Exception as e:
            print("An error occurred", e)
        else:
            print("Record created successfully.")
        finally:
            print("You are being redirected to homepage..")
            sleep(3)

    def mobcheck(self, mno):
        c = 0
        while mno > 0:
            c += 1
            mno = mno // 10
        if c == 10:
            return True
        else:
            return False

    def mobduplicatechk(self, mno):
        sql_get_dupliates = "SELECT COUNT(*) FROM USERLIST WHERE MOBILE_NO= %d" %mno
        try:
            m_cnt = -1
            self.myCursor.execute(sql_get_dupliates)
            results = self.myCursor.fetchall()
            for row in results:
                m_cnt = row[0]
            if m_cnt != 0:
                return True
            else:
                return False
        except Exception as e:
            print("An error occurred -", e)
