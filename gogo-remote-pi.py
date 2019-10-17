# import paho.mqtt.client as mqtt

# from classes.testGogo.py import TestGogo
# import sys
import classes.testGogo as test
import classes.gogotalk as gogotalk

import paho.mqtt.client as mqtt

messageCome = ""

def cmdProcess(msg):
    if (msg == "ledOn"):
        # gogoMqtt.ledControl(0,1)
        gogoTest.process1()
    elif (msg == "ledOff"):
        gogoTest.processNone()
        # gogoMqtt.ledControl(0,0)
    elif (msg == "beep"):
        # gogoMqtt.beep()
        gogoTest.process2()
    elif (msg == "motorOn"):
        # gogoMqtt.mOn()
        gogoTest.processNone()
    elif (msg == "motorOff"):
        # gogoMqtt.mOff()
        gogoTest.processNone()
    else:
        gogoTest.processNone()
        # gogoMqtt.processNone()


def on_connect(client, userdata, flags, rc):
    print("Connected with Code : "+ str(rc))
    print("MQTT Connected.")
    client.subscribe("remotelab")

def on_message(client, userdata,msg):
    messageCome = str(msg.payload.decode("utf-8"))
    cmdProcess(messageCome)
    # gogoTest.processCommand(messageCome)
    # print("print :"+str(msg.payload))
    print("print msg : "+messageCome)
    

if __name__=='__main__':
    gogoTest = test.testGogo()
    gogoMqtt = gogotalk.gogoTalk()
    # gogoTest.processCommand()
    print("mqtt starting")
    # mqttConnect()
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("soldier.cloudmqtt.com",14222,60)
    client.username_pw_set("obpkkwdc","1lUnSF15XpWM")
    client.loop_forever()




