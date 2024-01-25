from base import Connection

# MQTT
class MQTT:
    con = Connection()

    def __init__(self, mode, broker, port, subscribe, client, qos, topic, publish, message_length)
        self.mode = mode
        self.broker = broker
        self.port = port
        self.client = client
        self.qos = qos
        self.subscribe = subscribe
        self.topic = topic
        self.publish = publish
        self.message_lenght = message_length
        
    def connect(self):
        self.con.at_command(f'AT+QMTCFG="{self.mode}",0,0,1', 'Set mode')
        self.con.at_command(f'AT+QMTOPEN=0,"{self.broker}","{self.port}"', 'Broker connection')
        self.con.at_command(f'AT+QMTCONN=0,"{self.client}"', 'Connect to the client') 
    
    def subscribe(self):
        self.con.at_command(f'AT+QMTSUB=0,"{self.qos}","{self.subscribe}","{self.topic}"', 'Subscribe a topic')
        self.con.at_command(f'AT+QMTUNS=0,"{self.topic}","{self.subscribe}"', 'Unsubscribe a topic')
        self.con.at_command('AT+QMTCLOSE=0', 'Close Net')
        
    def publish(self):
        self.con.at_command(f'AT+QMTPUBEX=0,0,0,0,"{self.publish}","{self.message_length}"', 'Publish message to a topic')
        message = input("Enter your message to the MQTT: ")
        self.con.at_command(message, 'Message')
        self.con.at_command('AT+QMTRECV=0', 'Received')
        self.con.at_command('AT+QMTDISC=0', 'Disconnect a client from MQTT server')
        self.con.at_command('AT+QMTCLOSE=0', 'Close Net')
