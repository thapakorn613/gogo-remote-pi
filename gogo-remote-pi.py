# from classes.testGogo.py import TestGogo
import classes.testGogo as test
# import classes.gogotalk as gogotalk

import paho.mqtt.client as mqtt

messageCome = ""

def cmdProcess(message):
    #  gogo all cmd
    print('command ' + message)
    msg = message.split(" ")
    if (msg[0] == "ledOn"):
        # gogoMqtt.ledControl(0,1)
        gogoTest.process1()
    elif (msg[0] == "ledOff"):
        gogoTest.processNone()
        # gogoMqtt.ledControl(0,0)
    elif (msg[0] == "beep"):
        # gogoMqtt.beep()
        gogoTest.process2()
    elif (msg[0] == "motorOn"):
        gogoMqtt.mOn()
        # gogoTest.processNone()
    elif (msg[0] == "motorOff"):
        # gogoMqtt.mOff()
        # gogoTest.processNone()
    elif (msg[0] == "motorRD"):
        # gogoTest.processNone()
        gogoMqtt.mRD()
    elif (msg[0] == "motorCW"):
        gogoTest.processNone()
        gogoMqtt.mCW()
    elif (msg[0] == "motorCCW"):
        # gogoTest.processNone()
        gogoMqtt.mCCW()
    elif (msg[0] == "talkToMotor"):
        # gogoTest.processNone()
        gogoMqtt.talkToMotor(msg[1])
    elif (msg[0] == "setPower"):
        # gogoTest.processNone()
        gogoMqtt.setPower(msg[1])
    elif (msg[0] == "runStop"):
        # gogoTest.processNone()
        gogoMqtt.LogoControl(2)
    else:
        # gogoTest.processNone()
        gogoMqtt.processNone()


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




