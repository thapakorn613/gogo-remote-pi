# from classes.testGogo.py import TestGogo
import classes.testGogo as test
import classes.gogotalk as gogotalk

import paho.mqtt.client as mqtt
import time

messageCome = ""
debugMode = False

def cmdProcess(message):
    print('command '+message)
    msg = message.split(" ")
    if (msg[0] == "ledOn"):
        gogoMqtt.ledControl(0,1)
    elif (msg[0] == "ledOff"):
	gogoMqtt.ledControl(0,0)
    elif (msg[0] == "beep"):
        gogoMqtt.beep()
    elif (msg[0] == "motorOn"):
	print("motor : on")
        gogoMqtt.mOn()
    elif (msg[0] == "motorOff"):
	print("motor : off")
	gogoMqtt.mOff()
    elif (msg[0] == "motorRD"):
	gogoMqtt.mRD()
    elif (msg[0] == "motorCW"):
	gogoMqtt.mCW()
    elif (msg[0] == "motorCCW"):
	gogoMqtt.mCCW()
    elif (msg[0] == "talkToMotor"):
	print("talk to motor : "+msg[1])
	gogoMqtt.talkToMotor(msg[1])
    elif (msg[0] == "setPower"):
	gogoMqtt.setPower(msg[1])
    elif (msg[0] == "setServoDuty"):
	gogoMqtt.setServoDuty(msg[1])
    elif (msg[0] == "runStop"):
	gogoMqtt.LogoControl(2)
    else:
	#gogoTest,processNone()
        gogoMqtt.processNone()


def on_connect(client, userdata, flags, rc):
    print("Connected with Code : "+ str(rc))
    print("MQTT Connected.")
    client.subscribe("remotelab/Lab2")

def on_message(client, userdata,msg):
    messageCome = str(msg.payload.decode("utf-8"))
    cmdProcess(messageCome)
    
    # gogoTest.processCommand(messageCome)
    # print("print :"+str(msg.payload))
    print("print msg : "+messageCome)
    

if __name__=='__main__':
    # gogoTest = test.testGogo()
    gogoMqtt = gogotalk.gogoTalk()
    gogoMqtt.beep()
    time.sleep(1)
    gogoMqtt.beep()
    gogoMqtt.talkToMotor(1)
    gogoMqtt.mOff()
    # gogoTest.processCommand()
    print("mqtt starting")
    # mttConnect()
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    if (debugMode == True):
        client.connect("soldier.cloudmqtt.com",14222,60)
        client.username_pw_set("obpkkwdc","1lUnSF15XpWM")
    else:
        client.connect("35.198.231.150",1883,60)
    client.loop_forever()




