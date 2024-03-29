#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:32:41 2019

@author: manuel
"""

import time
import paho.mqtt.client as mqtt

# Callback Function on Connection with MQTT Server
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    client.subscribe("Test/#")

# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    # print the message received from the subscribed topic
    print ( str(msg.payload) )

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("hjnnghph", "tVp3MiDwDeUt")
client.connect("soldier.cloudmqtt.com", 13129, 60)

# client.loop_forever()
client.loop_start()
time.sleep(1)
while True:
    client.publish("Test","ON")
    print ("Message Sent")
    time.sleep(4)
    client.publish("Test","OFF")
    time.sleep(10)

client.loop_stop()
client.disconnect()
