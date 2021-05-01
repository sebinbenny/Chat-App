import socket
from datetime import date


class ServerSide:
    s = socket.socket()

    def __init__(self, myDB, myCursor, name, id):
        self.myDB = myDB
        self.myCursor = myCursor
        self.name = name
        self.id = id
        self.c_date = date.today().strftime('%Y-%m-%d')

    def connect(self):
        self.s.bind(('localhost', 9999))
        self.s.listen(1)
        print("System Online")
        self.msg()


    def msg(self):

        try:
            while 1:
                c_name = ''
                c, addr = self.s.accept()
                c.send(bytes(self.name, 'utf-8'))
                c_id = c.recv(1024).decode()
                sql_get_c_name = "SELECT USER_NAME FROM USERLIST WHERE UID = %d" % int(c_id)
                self.myCursor.execute(sql_get_c_name)
                r_c_name = self.myCursor.fetchall()
                for i in r_c_name:
                    c_name = i[0]
                print("Connected to ", c_name)

                while 1:
                    to_msg = input("Enter your message : ")
                    c.send(bytes(to_msg, 'utf-8'))
                    ack = c.recv(1024).decode()
                    print(str(ack))
                    mid = self.midgenerator()

                    sql_send = "INSERT INTO MSGS() VALUES ( %d, '%s', %d, %d, '%s', %d)" \
                               % (mid, to_msg, self.id, int(c_id), self.c_date, self.id)
                    self.myCursor.execute(sql_send)

                    que = c.recv(1024).decode()
                    print("Message from %s : %s" % (str(c_name), str(que)))
                    c.send(bytes("Message Received!", 'utf-8'))
                    mid = self.midgenerator()
                    sql_recv = "INSERT INTO MSGS() VALUES ( %d, '%s', %d, %d, '%s', %d)" \
                               % (mid, str(que), int(c_id), self.id, self.c_date , int(c_id))
                    self.myCursor.execute(sql_recv)
                    self.myDB.commit()

        except Exception as e:
            print("An error occurred :", e)

        finally:
            pass

    def midgenerator(self):
        mid = 0
        sql_mid_max = 'SELECT MAX(MID) FROM MSGS'
        self.myCursor.execute(sql_mid_max)
        r = self.myCursor.fetchall()
        for i in r:
            mid = i[0]
        mid += 1
        return mid
