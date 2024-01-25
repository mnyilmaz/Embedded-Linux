from base import Connection
import inputs as var

# MQTT
class MQTT:
    con = Connection()
        
    def connect(self):
        self.con.at_command(f'AT+QMTCFG="{var.mode}",0,0,1', 'Set mode')
        self.con.at_command(f'AT+QMTOPEN=0,"{var.broker}","{var.port}"', 'Broker connection')
        self.con.at_command(f'AT+QMTCONN=0,"{var.client}"', 'Connect to the client') 
    
    def subscribe(self):
        self.con.at_command(f'AT+QMTSUB=0,"{var.qos}","{var.subscribe}","{var.topic}"', 'Subscribe a topic')
        self.con.at_command(f'AT+QMTUNS=0,"{var.topic}","{var.subscribe}"', 'Unsubscribe a topic')
        self.con.at_command('AT+QMTCLOSE=0', 'Close Net')
        
    def publish(self):
        self.con.at_command(f'AT+QMTPUBEX=0,0,0,0,"{var.publish}","{var.message_length}"', 'Publish message to a topic')
        message = input("Enter your message to the MQTT: ")
        self.con.at_command(message, 'Message')
        self.con.at_command('AT+QMTRECV=0', 'Received')
        self.con.at_command('AT+QMTDISC=0', 'Disconnect a client from MQTT server')
        self.con.at_command('AT+QMTCLOSE=0', 'Close Net')
