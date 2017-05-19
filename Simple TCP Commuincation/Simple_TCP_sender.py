from socket import *

def sender():
    send_socket = socket(AF_INET,SOCK_STREAM) #defining a socket
    send_socket.connect(('localhost', 6552))
    while 1:
        st=raw_input("Enter Data to send")
        send_socket.send(st)
        #conn,addr = send_socket.accept()
        print "Data Received : "+send_socket.recv(1024)
        if(st == "bye"):
            print "Closing connection"
            break
    send_socket.close()
sender()