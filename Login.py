from time import sleep
import UserHome


class LogUser:
    def __init__(self, myDB, myCursor):
        self.myDB = myDB
        self.myCursor = myCursor

    def action(self):
        try:
            user = input("Enter your username : ")
            sql_username = "SELECT * FROM USERLIST WHERE USER_NAME ='%s'" % user
            self.myCursor.execute(sql_username)
            username_res = self.myCursor.fetchall()
            if len(username_res) == 0:
                print("Invalid Username.")
                sleep(2)
            else:
                uid, umob = 0, 0
                pswd = input("Enter your password : ")
                sql_login = "SELECT * FROM USERLIST WHERE USER_NAME ='%s' AND USER_PASSWORD='%s' " % (user, pswd)
                self.myCursor.execute(sql_login)
                results = self.myCursor.fetchall()
                if len(results) == 0:
                    print("Incorrect Password.")
                else:
                    for rows in results:
                        uid = rows[0]
                        umob = rows[3]
                    print("Logged in.")
                    print("You are being directed to Home...")
                    sleep(3)
                    h1 = UserHome.Home(self.myDB, self.myCursor, user, uid, umob)
                    h1.viewhome()
        except Exception as e:
            print("An error occurred -", e)
