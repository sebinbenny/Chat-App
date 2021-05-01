from datetime import date, datetime
import Registration
import Login
import ForgotPassword
import mysql.connector

# AppHome, ForgotPassword, history, Login, main, PasswordReset, receiver, Registration, UserHome.

myDB = mysql.connector.connect(host="localhost", user="root", passwd="administrator", database="MSG_APP")
myCursor = myDB.cursor()

class UI:
    def __init__(self):
        pass

    def options(self):
        print("---------------------------------------\n---------------WELCOME-----------------"
              "\n---------------------------------------")
        c_date = date.today().strftime("%B %d, %Y")
        c_time = datetime.now().strftime("%H:%M")
        print("Start Time : ", c_date, c_time)
        print("\nWelcome to CHAT-BOT!!")
        print("Your Options\n-----------------------")
        print("1. Registration\n2. Login\n3. Forget Password\n4. Exit")
        user_op = int(input("Enter 1/2/3 : "))
        self.further_action(user_op)

    def further_action(self, user_op):
        if user_op == 1:
            h = Registration.Home(myDB, myCursor)
            h.homeview()
        elif user_op == 2:
            l1 = Login.LogUser(myDB, myCursor)
            l1.action()
        elif user_op == 3:
            f = ForgotPassword.UserAssist(myDB, myCursor)
            f.assist()
        elif user_op == 4:
            exit()
        else:
            print("You entered a wrong option!")
            user_action = input("Do you want to exit? (Y/N) : ")
            if user_action == 'Y':
                exit()
            elif user_action == 'N':
                self.options()
            else:
                exit()


if __name__ == '__main__':
    u = UI()
    while True:
        u.options()
