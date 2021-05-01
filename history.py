class ViewHistory:

    def __init__(self, myDB, myCursor, uname, uid):
        self.myDB = myDB
        self.myCursor = myCursor
        self.user = uname
        self.usid = uid

    def userHistor(self):
        sql_his = ''
        print("Hi %s, Please select one from below\n1. View Messages you sent.\n2. View messages you received."
              % self.user)
        user_ch = int(input("Enter your choice (1/2) ? : "))
        if user_ch == 1:
            sql_his = "SELECT * FROM MSGS A WHERE A.FROM_ID = %d" % self.usid
        elif user_ch == 2:
            sql_his = "SELECT * FROM MSGS A WHERE A.TO_ID = %d" % self.usid
        else:
            print("Invalid entry.")
        # Executing Query
        self.myCursor.execute(sql_his)
        history_res = self.myCursor.fetchall()
        if len(history_res) == 0:
            print("No messages yet.")
        else:
            for row in history_res:
                msg = row[1]
                f_id = row[2]
                t_id = row[3]
                s_dt = row[4]
                t_user = self.getUser(t_id)
                f_user = self.getUser(f_id)
                self.displayHist(s_dt, msg, t_user, f_user)

    def getUser(self, uid):
        user_name = ''
        sql_geUser = "SELECT USER_NAME FROM USERLIST WHERE UID = %d" % (uid)
        self.myCursor.execute(sql_geUser)
        getuser_result = self.myCursor.fetchall()
        if len(getuser_result) == 0:
            user_name = "Unknown"
        else:
            for item in getuser_result:
                user_name = item[0]
        return user_name

    def displayHist(self, s_dt, msg, t_user, f_user):
        print("----------------------------------------------------")
        print("Date = %s\nMessage = %s\nTo = %s\nFrom = %s" % (s_dt, msg, t_user, f_user))
