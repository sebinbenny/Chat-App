import socket
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd ='administrator')
client_cur = mydb.cursor()

c_id = 1

c = socket.socket()
c.connect(('localhost',9999))

s_name = c.recv(1024).decode()
c.send(bytes(str(c_id), 'utf-8'))

print("Connected to", s_name, "!")

while True:

    try:
        reply = c.recv(1024).decode()
        c.send(bytes("Message Received!", 'utf-8'))
        print("Message from %s : %s " % (str(s_name), str(reply)))

        que = input("Enter Message : ")
        c.send(bytes(que, 'utf-8'))
        ack = c.recv(1024).decode()
        print(str(ack))

    except Exception as e:
        print("An error occurred :", e)
        exit()

#c.close()