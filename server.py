import socket
import sys
 
#HOST = '172.18.158.3'
HOST = '192.168.8.100'   
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

    sensorState = mensaje.decode("utf-8")

    if ( sensorState == "incL") :
        print ("Inclinacion hacia la izquierda")
        
    if ( sensorState == "incR") :
        print ("Inclinacion hacia la derecha")
        
    if ( sensorState == "frte") :
        print ("CUIDADO podria caer de frente")
        
    if ( sensorState == "esp") :
        print ("CUIDADO podria caer de espalda")
    
    

    #print(sensorState)

    #print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    conn.send(bytes("Se ha conectado exitosamente al servidor","utf-8"))
    
     
s.close()
