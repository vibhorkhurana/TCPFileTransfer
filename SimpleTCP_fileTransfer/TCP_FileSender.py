#Client Implementation
from socket import *

def fileSender():
    file = open("/home/vibhor/IoT/Android_Examples","r")
    #print file.read(15)
    sender_socket = socket(AF_INET,SOCK_STREAM,0)
    sender_socket.connect(('localhost',6569))
  #  while 1:
        #sender_socket.send("Android_Examples")
    sender_socket.send(file.read())
    sender_socket.close()
fileSender()