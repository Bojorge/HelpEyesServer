import socket
import sys
 
HOST = '192.168.8.102'   
PORT = 1234 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
#realiza el bind socket
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print ('Socket bind complete')
 
#inicia  socket
s.listen(10)
print ('Socket now listening \n')
 
#now conversa con  client
while 1:
    #esperando conecccion 
    conn, addr = s.accept()
    mensaje=conn.recv(1024)
    #print(mensaje.decode("utf-8"))
    print(mensaje)
    #print ('Connected with ' + addr[0] + ':' + str(addr[1]))
     
s.close()
