#Server Implementation
from socket import *
def receiver():
    fis = open("./Copied","w")
    recvServer = socket(AF_INET,SOCK_STREAM,0)
    recvServer.bind(('localhost',6569))
    recvServer.listen(5)
    recvd, addr = recvServer.accept()
    while 1:
        str = recvd.recv(1)
        if len(str) == 0:
            recvd.close()
            fis.close()
            break
        else:
            fis.write(str)
       # print file
        #recvd.close()
    recvServer.close()
receiver()