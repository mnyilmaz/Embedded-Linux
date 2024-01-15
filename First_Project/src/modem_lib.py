import serial
import time


# Base class
class Connection:
    def at_command(self, at_command, explanation):
        try:
            modem.write((at_command + '\r').encode())
            #time.sleep(5)
        finally:
            #time.sleep(5)
            response = modem.read(byte)
            print(f"Received {explanation} response:\n{response.decode()}\n")
            return response
    
    # Check if base connection exists
    def check_base(self):
        self.at_command(BASE['sim'], 'SIM status')
        self.at_command(BASE['network'], 'Network registration')
        self.at_command(BASE['gprs'], 'GPRS registration')
        self.at_command(BASE['base'], 'Base status')
        
    
    def set_APN(self):
        apn = input("Enter your APN: ") 
        ip = input("Enter your IP: ") 
        self.at_command(f'AT+CGDCONT=1,"IP","{apn}","{ip}"', 'Set APN')
        self.at_command('AT+CGDCONT?', 'Check APN')


    def check_ppp_settings(self):
        response = self.at_command('AT+QCFG="usbnet"', 'Check USBNET settings')
        if '0' not in response:
            self.at_command('AT+QCFG="usbnet",0', 'Set USBNET')
            self.at_command(BASE['ue_reboot'], 'UE Reboot')

# HTTP
class HTTP:
    con = Connection()
    
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
        self.con.at_command("AT+QHTTPCFG=\"requestheader\",\"{}\"".format(request_header), 'AT+QHTTPCFG=requestheader')
        sslctxID = input("sslctxID: ")
        self.con.at_command("AT+QHTTPCFG=\"sslctxid\",\"{}\"".format(sslctxID), 'AT+QHTTPCFG=sslctxid')
        content_type = input("content_type: ")
        self.con.at_command("AT+QHTTPCFG=\"contenttype\",\"{}\"".format(content_type), 'AT+QHTTPCFG=contenttype')
        auto_outrsp = input("auto_outrsp: ")
        self.con.at_command("AT+QHTTPCFG=\"rspout/auto\",\"{}\"".format(auto_outrsp), 'AT+QHTTPCFG=rspout/auto')
        closedind = input("closedind: ")
        self.con.at_command("AT+QHTTPCFG=\"closed/ind\",\"{}\"".format(closedind), 'AT+QHTTPCFG=closed/ind')
        window_size = input("window_size: ")
        self.con.at_command("AT+QHTTPCFG=\"windowsize\",\"{}\"".format(window_size), 'AT+QHTTPCFG=windowsize')
        close_wait_time = input("close_wait_time: ")
        self.con.at_command("AT+QHTTPCFG=\"closewaittime\",\"{}\"".format(close_wait_time), 'AT+QHTTPCFG=closewaittime')
        username = input("username: ")
        password = input("password: ")
        self.con.at_command("AT+QHTTPCFG=\"auth\",\"%s\":\"%s\"".format(username, password), 'AT+QHTTPCFG=auth')
        custom_value = input("custom_value: ")
        self.con.at_command("AT+QHTTPCFG=\"custom_header\",\"{}\"".format(custom_value), 'AT+QHTTPCFG=custom_header')
        
    def set_PDP(self):
        apn = input("Enter APN: ")
        self.con.at_command(f'AT+QICSGP=1,1,"{apn}","","",1', 'Set APN')
        self.con.at_command(HTTP_AT['querry_PDP'], 'Querry PDP Context')
        self.con.at_command(HTTP_AT["activate"], 'Activate PDP Context')

    def connect(self):
        self.con.at_command(f'AT+QHTTPURL={len(HTTP_AT["url"])},80', 'Set URL')
        time.sleep(10)
        self.con.at_command(HTTP_AT['url'], 'URL')
        time.sleep(5)
        self.con.at_command(HTTP_AT['check_url'], 'Check URL status')
        
    def http_get(self):
        time.sleep(20)
        self.con.at_command(HTTP_AT['get_request'], 'HTTP GET Request')
        
    def http_read(self):
        time.sleep(20)
        self.con.at_command(HTTP_AT['read'], 'Read HTTP Response')
        
    def http_post(self):
        self.con.at_command(HTTP_AT['post_request'], 'HTTP POST Request')
        self.con.at_command(HTTP_AT['message'], 'Message')

    def http_stop(self):
        self.con.at_command(HTTP_AT['cancel'], 'Cancel')
        
    def close_connection(self):
        self.con.at_command(HTTP_AT['end'], 'End the connection')
        

# MQTT
class MQTT:
    con = Connection()
       
    def connect(self):
        self.con.at_command(MQTT_AT['set'], 'Set mode')
        self.con.at_command(MQTT_AT['open_net'], 'Broker connection')
        self.con.at_command(MQTT_AT['connect'], 'Connect to the client') 
    
    def subscribe(self):
        self.con.at_command(MQTT_AT['sub1'], 'Subscribe a topic')
        self.con.at_command(MQTT_AT['sub2'], 'Subscribe a topic')
        
    def publish_message(self):
        self.con.at_command(MQTT_AT['publish'], 'Publish message to a topic')
        self.con.at_command(MQTT_AT['message'], 'Message')
        self.con.at_command(MQTT_AT['read'], 'Receive')
        
    
if __name__ == "__main__":
    modem = serial.Serial('/dev/ttyUSB3', 115200, timeout=5)
    byte = 1024

    BASE = {
        'sim': 'AT+CPIN?',
        'network': 'AT+CREG?',
        'gprs': 'AT+CGREG?',
        'base': 'AT+COPS?',
        'ue_reboot': 'AT+CFUN=1,1'
    }

    HTTP_AT = {
        'querry_PDP': 'AT+QIACT?',
        'activate': 'AT+QIACT=1',
        'deactivate': 'AT+QIDEACT=1',
        'url': 'https://webhook.site/',
        'check_url': 'AT+QHTTPURL?',
        'get_request': 'AT+QHTTPGET=80',
        'read':'AT+QHTTPREAD=80',
        'post_request': 'AT+QHTTPPOST=10,50',
        'message': 'hello http',
        'cancel': 'AT+QHTTPSTOP',
        'end': 'AT+QICLOSE=1'  
    }
    
    MQTT_AT = {
        'set': 'AT+QMTCFG="recv/mode",0,0,1',
        'open_net': 'AT+QMTOPEN=0,"broker.hivemq.com",1883', # Open a network for MQTT client id, hostname, port
        'is_open': 'AT+QMTOPEN?', # Check status 
        'connect': 'AT+QMTCONN=0,"embedded"', # clientID
        'sub1': 'AT+QMTSUB=0,1,"topic/example",2', # clientID, messageID, topic
        'sub2': 'AT+QMTSUB=0,1,"topic/pub",0', # clientID, messageID, topic
        'publish': 'AT+QMTPUBEX=0,0,0,0,"topic/pub",30', # clientID, messageID, qos
        'message': 'hello mqtt',
        'read': 'AT+QMTRECV=0', # clientID
        'close_net': 'AT+QMTCLOSE=0', # clientID
        'disconnect': 'AT+QMTDISC=0', # Disconnect a client
        'unsubscribe': 'AT+QMTUNS=0,1,"topic/example"' # cleintID, messageID, topic      
    }   

    # Base connection
    connect = Connection()
    #connect.check_base()
    #connect.set_APN()

    # HTTP connection
    #http = HTTP()
    #http.config()
    #http.set_PDP()
    #http.connect()
    #http.http_get()
    #http.http_read()
    #http.http_post()

    # MQTT connection
    mqtt = MQTT()
    mqtt.connect()
    #mqtt.subscribe()
    mqtt.publish_message()
    
    modem.close()
