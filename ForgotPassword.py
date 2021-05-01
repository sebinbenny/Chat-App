from time import sleep
import PasswordReset

class UserAssist:

    def __init__(self, myDB, myCursor):
        self.myDB = myDB
        self.myCursor = myCursor

    def assist(self):
        usr_mob = int(input("Enter your mobile number : "))
        sql_get_mno = "SELECT UID, USER_NAME FROM USERLIST WHERE MOBILE_NO= %d" % usr_mob
        try:
            self.myCursor.execute(sql_get_mno)
            res = self.myCursor.fetchall()
            if len(res) == 0:
                print("Mobile number you entered is not registered with us. Please check and try again!")
                print("Re-directing back to home. Please wait!")
                sleep(2)
            else:
                for row in res:
                    uid = row[0]
                    unm = row[1]
                    p = PasswordReset.Reset(self.myDB, self.myCursor, unm, uid)
                    p.userInp()
        except Exception as e:
            print("An error occurred -", e)
