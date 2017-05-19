from socket import *
def receiver():
    recv_socket=socket(AF_INET,SOCK_STREAM)
    recv_socket.bind(('localhost',6552))
    recv_socket.listen(5)
    conn, addr = recv_socket.accept()
    while 1:
        print "Data Received : "+conn.recv(1024)
        if (conn.recv == "bye"):
            break
        st = raw_input("Enter Data to send ")
        conn.send(st)

    print "closing"
    conn.close()
    recv_socket.close()
receiver()