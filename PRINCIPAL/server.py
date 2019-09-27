import socket
import sys
import time
import paho.mqtt.client as mqtt
 
#HOST = '172.18.158.3'
HOST = '192.168.8.105'   
PORT = 1234

###########################################
# Callback Function on Connection with MQTT Server
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    client.subscribe("sensorArduino/#")

# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    # print the message received from the subscribed topic
    mensaje=""
    for i in range(len(str(msg.payload))-1):
        if (i>1):
            mensaje+=str(msg.payload)[i]
            
    
    
    #client.publish(" Advertencia",mensaje)
    print ("\n"+mensaje+"\n")

    
   
    if (mensaje=="h"):
      print ("temperatura superior a 30º C")
      client.publish("Advertencia","h")
      
    if (mensaje=="c"):
      print ("temperatura normal")
      client.publish("Advertencia","c")
      
    if (mensaje=="x"):
      print ("PELIGRO DE CHOQUE CONTRA ALGÙN OBJETO")
      client.publish("Advertencia","x")
      
    if (mensaje=="p"):
      print ("PELIGRO hay un obstaculo a menos de un metro")
      client.publish("Advertencia","p") 



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("hjnnghph", "tVp3MiDwDeUt")
client.connect("soldier.cloudmqtt.com", 13129, 60)

# client.loop_forever()
client.loop_start()
time.sleep(1)
###########################################3
 
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

    sensorApp = mensaje.decode("utf-8")

    #conn.send(bytes("Se ha conectado exitosamente al servidor","utf-8"))

    #client.subscribe("sensorArduino/#")

    if ( sensorApp == "L") :
        client.publish(" Advertencia","L")
        print ("\nInclinacion hacia la izquierda \n")
        
    if ( sensorApp == "R") :
        client.publish("Advertencia","R")
        print (" \nInclinacion hacia la derecha \n")
        
    if ( sensorApp == "f") :
        client.publish("Advertencia","f")
        print (" \nCUIDADO podria caer de frente \n")
        
    if ( sensorApp == "e") :
        client.publish("Advertencia","e")
        print (" \nCUIDADO podria caer de espalda \n")

    if ( sensorApp == "d") :
        client.publish("Advertencia","d")
        print (" \nCUIDADO esta demasiado oscuro \n")

    if ( sensorApp == "b") :
        client.publish("Advertencia","b")
        print (" \nADVERTENCIA esta oscureciendo \n")
        
    if ( sensorApp == "l") :
        client.publish("Advertencia","l")
        print (" \nADVERTENCIA hay demasiada luz \n")
    
    #time.sleep(1)
     
s.close()
client.loop_stop()
client.disconnect()
