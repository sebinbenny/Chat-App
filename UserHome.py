import main
import history
import PasswordReset
from time import sleep

class Home:

    def __init__(self, myDB, myCursor, uname, uid, umob):
        self.myDB = myDB
        self.myCursor = myCursor
        self.user = uname
        self.usid = uid
        self.umob = umob

    def viewhome(self):
        print("-------------------------------------------------\n---------------Hey", self.user,
              "--------------------\n-------------------------------------------------")
        print("Choose what to do today : ")
        print("1. Start Chat\n2. View History\n3. Change Password\n4. Log out")
        uch = int(input("Enter your choice (1/2/3/4) : "))
        self.choice(uch)


    def choice(self, uch):
        if uch == 1:
            s = main.ServerSide(self.myDB, self.myCursor, self.user, self.usid)
            s.connect()
            # In the middle of chat, one should be able to disconnect and come back here. Add that later.
            self.viewhome()
        elif uch == 2:
            v = history.ViewHistory(self.myDB, self.myCursor, self.user, self.usid)
            v.userHistor()
            self.viewhome()
        elif uch == 3:
            p = PasswordReset.Reset(self.myDB, self.myCursor, self.user, self.usid)
            p.userInp()
            self.viewhome()
        elif uch == 4:
            print("Logging you out. Please wait.")
            sleep(3)
        else:
            print("Invalid Entry")
            self.viewhome()
