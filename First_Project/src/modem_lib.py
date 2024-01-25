import serial
import time


# Base class
class Connection:
    def at_command(self, at_command, explanation):
        try:
            modem.write((at_command + '\r').encode())
        finally:
            response = modem.read(byte)
            print(f"Received {explanation} response:\n{response.decode()}\n")
            return response

    
    # Check if base connection exists
    def check_base(self):
        self.at_command('AT+CPIN?', 'SIM status')
        self.at_command('AT+CREG?', 'Network registration')
        self.at_command('AT+CGREG?', 'GPRS registration')
        self.at_command('AT+COPS?', 'Base status')
        
    
    def define_PDP_context(self):
        apn = input("Enter your APN: ") 
        ip = input("Enter your IP: ") 
        self.at_command(f'AT+CGDCONT=1,"{ip}","{apn}"', 'Define PDP context')
        self.at_command('AT+CGDCONT?', 'Check APN')


    def reboot_options(self):
        response = self.at_command('AT+QCFG="usbnet"', 'Check USBNET settings')
        if '0' not in response:
            self.at_command('AT+QCFG="usbnet",0', 'Set USBNET')
            self.at_command('AT+CFUN=1,1', 'UE Reboot')

# HTTP
class HTTP:
    con = Connection()

    def __init__(self, apn, url, get_size, read_size, post_size, latency):
        self.apn = apn
        self.url = url
        self.get_size = get_size
        self.read_size = read_size
        self.post_size = post_size
        self.latency = latency
        

    # HTTP settings
    def config(self):
        self.con.at_command('AT+QHTTPCFG="contextid",1', 'Context ID Configuration')
        self.con.at_command('AT+QHTTPCFG="responseheader",1', 'Response Header Configuration')        
        answer = input("Would you like to configure more settings? (Y/N): ")
        if answer.upper() == 'Y':
            self.QHTTPCFG_settings()
        else:
            self.con.at_command('AT+QHTTPCFG?', 'HTTP Settings')

    def QHTTPCFG_settings(self):
        request_header = input("request_header: ")
        self.con.at_command(f'AT+QHTTPCFG="requestheader","{request_header}"', 'AT+QHTTPCFG=requestheader')
        sslctxID = input("sslctxID: ")
        self.con.at_command(f'AT+QHTTPCFG="sslctxID","{sslctxID}"', 'AT+QHTTPCFG=sslctxID')
        content_type = input("content_type: ")
        self.con.at_command(f'AT+QHTTPCFG="contenttype","{content_type}"', 'AT+QHTTPCFG=contenttype')
        auto_outrsp = input("auto_outrsp: ")
        self.con.at_command(f'AT+QHTTPCFG="rspout/auto","{auto_outrsp}"', 'AT+QHTTPCFG=rspout/auto')
        closedind = input("closedind: ")
        self.con.at_command(f'AT+QHTTPCFG="closed/ind","{closedind}"', 'AT+QHTTPCFG=closed/ind')
        window_size = input("window_size: ")
        self.con.at_command(f'AT+QHTTPCFG="windowsize","{window_size}"', 'AT+QHTTPCFG=windowsize')
        close_wait_time = input("close_wait_time: ")
        self.con.at_command(f'AT+QHTTPCFG="closewaittime","{close_wait_time}"', 'AT+QHTTPCFG=closewaittime')
        username = input("username: ")
        password = input("password: ")
        self.con.at_command(f'AT+QHTTPCFG="auth","{username}":"{password}"', 'AT+QHTTPCFG=auth')
        custom_header = input("custom_header: ")
        self.con.at_command(f'AT+QHTTPCFG="custom_header","{custom_header}"', 'AT+QHTTPCFG=custom_header')
        
    def set_PDP(self):
        self.con.at_command(f'AT+QICSGP=1,1,"{self.apn}","","",1', 'Set APN')
        self.con.at_command('AT+QIACT?', 'Querry PDP Context')
        self.con.at_command('AT+QIACT=1', 'Activate PDP Context')
        self.con.at_command('AT+QIDEACT=1', 'Deactivate PDP Context')

    def connect(self):
        self.con.at_command(f'AT+QHTTPURL={len(self.url)},80', 'Set URL pre-settings')
        time.sleep(10)
        self.con.at_command(self.url, 'Set URL')
        time.sleep(5)
        self.con.at_command('AT+QHTTPURL?', 'Check URL status')
        
    def http_get(self):
        time.sleep(20)
        self.con.at_command(f'AT+QHTTPGET="{self.get_size}"', 'HTTP GET Request')
        
    def http_read(self):
        time.sleep(20)
        self.con.at_command(f'AT+QHTTPREAD="{self.read_size}"', 'Read HTTP Response')
        
    def http_post(self):
        self.con.at_command(f'AT+QHTTPPOST="{self.post_size}","{self.latency}"', 'HTTP POST Request')
        message = input("Enter your message to the HTTP: ")
        self.con.at_command(message, 'Message')

    def destroyer_of_http(self):
        self.con.at_command('AT+QHTTPSTOP', 'Cancel')
        self.con.at_command('AT+QICLOSE=1', 'End the connection')
        

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
        self.con.at_command('AT+QMTCLOSE=0', 'Unsubscribe a topic')
        
    def publish_message(self):
        self.con.at_command(f'AT+QMTPUBEX=0,0,0,0,"{self.publish}","{self.message_length}"', 'Publish message to a topic')
        message = input("Enter your message to the MQTT: ")
        self.con.at_command(message, 'Message')
        self.con.at_command('AT+QMTRECV=0', 'Received')

    def destroyer_of_mqtt(self):
        self.con.at_command('AT+QMTCLOSE=0', 'Close Net')
        self.con.at_command('AT+QMTDISC=0', 'Close Net')
        
    
if __name__ == "__main__":
    # Main configurations
    baudrate = 115200
    port = 'dev/ttyUSB3'
    byte = 1024
    apn = 'super'
    modem = serial.Serial(port, baudrate, timeout=5)

    # HTTP
    url = 'https://webhook.site/'
    get_size = 80
    read_size = 80
    post_size = 20
    latency = 50
    
    # MQTT
    mode = "recv/mode"
    broker = "broker.hivemq.com"
    client_port = 1883
    client = "embedded"
    qos = 1
    topic = 1
    subscribe = "topic/sub"
    publish = "topic/pub"
    message_length = 80

    # Base connection
    connect = Connection()

    # HTTP connection
    http = HTTP()

    # MQTT connection
    mqtt = MQTT()
    
    modem.close()
