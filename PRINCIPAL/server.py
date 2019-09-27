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

    
   
    if (mensaje=="hot"):
      print ("temperatura superior a 30º C")
      client.publish("Advertencia","hot")
      
    if (mensaje=="cold"):
      print ("temperatura normal")
      client.publish("Advertencia","cold")
      
    if (mensaje=="beat"):
      print ("PELIGRO DE CHOQUE CONTRA ALGÙN OBJETO")
      client.publish("Advertencia","beat")
      
    if (mensaje=="warn"):
      print ("PELIGRO hay un obstaculo a menos de un metro")
      client.publish("Advertencia","warm") 



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

    if ( sensorApp == "incL") :
        client.publish(" Advertencia","incL")
        print ("\nInclinacion hacia la izquierda \n")
        
    if ( sensorApp == "incR") :
        client.publish("Advertencia","incR")
        print (" \nInclinacion hacia la derecha \n")
        
    if ( sensorApp == "frte") :
        client.publish("Advertencia","frte")
        print (" \nCUIDADO podria caer de frente \n")
        
    if ( sensorApp == "esp") :
        client.publish("Advertencia","esp")
        print (" \nCUIDADO podria caer de espalda \n")

    if ( sensorApp == "dark") :
        client.publish("Advertencia","dark")
        print (" \nCUIDADO esta demasiado oscuro \n")

    if ( sensorApp == "black") :
        client.publish("Advertencia","black")
        print (" \nADVERTENCIA esta oscureciendo \n")
        
    if ( sensorApp == "light") :
        client.publish("Advertencia","light")
        print (" \nADVERTENCIA hay demasiada luz \n")
    
    #time.sleep(1)
     
s.close()
client.loop_stop()
client.disconnect()
