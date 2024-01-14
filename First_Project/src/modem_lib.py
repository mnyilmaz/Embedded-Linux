import serial
import time


# Base class
class Connection:
    def at_command(self, at_command, explanation):
        try:
            modem.write((at_command + '\r').encode())
            time.sleep(10)
        finally:
            time.sleep(10)
            response = modem.read(byte)
            print(f"Received {explanation} response:\n{response.decode()}\n")
            return response
    
    # Check if base connection exists
    def check_base(self):
        self.at_command(BASE['sim'], 'SIM status')
        self.at_command(BASE['network'], 'Network registration')
        self.at_command(BASE['gprs'], 'GPRS registration')
    
    def set_APN(self):
        apn = input("Enter your APN: ") 
        ip = input("Enter your IP: ") 
        self.at_command(f'AT+CGDCONT=1,"IP","{apn}","{ip}"', 'Set APN')
        self.at_command('AT+CGDCONT?', 'Check APN')

    def display_current(self):
        self.at_command(BASE['display'], 'Display current settings')

    def check_settings(self):
        response = self.at_command('AT+QCFG="usbnet"', 'Check USBNET settings')
        if '0' in response:
            self.at_command('AT+QCFG="usbnet",0', 'Set USBNET')

    def ue_reboot(self):
        response = self.at_command(BASE['ue_reboot'], 'UE Reboot')
        if 'ERROR' in response:
            print('An error occurred during UE Reboot')
            self.modem.close()

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
        self.con.at_command(BASE['querry_PDP'], 'Querry PDP Context')
        id = input("Enter PDP context ID: ")
        self.con.at_command(f'"{BASE['querry_PDP']}""{id}"', 'Activate PDP Context')

    def connect(self):
        time.sleep(10)
        self.con.at_command(f'AT+QHTTPURL={len(HTTP['url'])},80', 'Set URL')
        time.sleep(10)
        self.con.at_command(HTTP['url'], 'URL')
        time.sleep(30)
        self.con.at_command(HTTP['check_url'], 'Check URL status')
        time.sleep(10)
        
    def http_get(self):
        self.con.at_command(HTTP['get_request'], 'HTTP GET Request')
        time.sleep(30)
        
    def http_read(self):
        self.con.at_command(HTTP['read'], 'Read HTTP Response')
        time.sleep(10)
        
    def http_post(self):
        self.con.at_command(HTTP['post_request'], 'HTTP POST Request')
        self.con.at_command(HTTP['message'], 'Message')

    def http_stop(self):
        self.con.at_command(HTTP['cancel'], 'Cancel')
        
    def close_connection(self):
        self.con.at_command(HTTP['end'], 'End the connection')
        

# MQTT
class MQTT:
    con = Connection()
       
    def connect(self):
        self.con.at_command(MQTT['set'], MQTT['set'])
        time.sleep(5)
        self.con.at_command(MQTT['open_net'], MQTT['open_net'])
        time.sleep(5)
        self.con.at_command(MQTT['is_open'], MQTT['is_open'])
        time.sleep(5)
        self.con.at_command(MQTT['connect'], MQTT['connect']) 
    
    def subscribe(self):
        time.sleep(5)
        self.con.at_command(MQTT['sub1'], MQTT['sub1'])
        time.sleep(5)
        self.con.at_command(MQTT['sub2'], MQTT['sub2'])
        
    def publish_message(self):
        self.con.at_command(MQTT['publish'], MQTT['publish']) 
        
    
if __name__ == "__main__":
    modem = serial.Serial('/dev/ttyUSB2', 115200, timeout=20)
    byte = 1024

        BASE = {
        'sim': 'AT+CPIN?',
        'network': 'AT+CREG?',
        'gprs': 'AT+CGREG?',
        'display': 'AT+V',
        'ue_reboot': 'AT+CFUN=1,1',
    }

    HTTP = {
        'querry_PDP': 'AT+QIACT?',
        'activate': 'AT+QIACT=',
        'deactivate': 'AT+QIDEACT=',
        'url': 'https://webhook.site/3d58bfc7-6c53-4092-8ff8-11941f1f6753',
        'check_url': 'AT+QHTTPURL?',
        'get_request': 'AT+QHTTPGET=80',
        'read':'AT+QHTTPREAD=80',
        'post_request': 'AT+QHTTPPOST=10,50',
        'message': 'hello http',
        'cancel': 'AT+QHTTPSTOP',
        'end': 'AT+QICLOSE=1',    
    }
    
    MQTT = {
        'set': 'AT+QMTCFG="recv/mode",1,0,1',
        'open_net': 'AT+QMTOPEN=0,"broker.hivemq.com",1883', # Open a network for MQTT client id, hostname, port
        'is_open': 'AT+QMTOPEN?', # Check status 
        'connect': 'AT+QMTCONN=0,"client/1"', # clientID
        'sub1': 'AT+QMTSUB=0,1,"topic/example",2', # clientID, messageID, topic
        'sub2': 'AT+QMTSUB=0,1,"topic/pub",0', # clientID, messageID, topic
        'publish': 'AT+QMTPUBEX=0,0,0,0,"topic/pub",30', # clientID, messageID, qos
        'read': 'AT+QMTRECV=0', # clientID
        'close_net': 'AT+QMTCLOSE=0', # clientID
        'disconnect': 'AT+QMTDISC=0', # Disconnect a client
        'unsubscribe': 'AT+QMTUNS=0,1,"topic/example"', # cleintID, messageID, topic      
    }

    # Base connection
    connect = Connection()
    connect.check_base()
    connect.set_APN()

    # HTTP connection
    http = HTTP()
    http.config()
    http.set()
    http.connect()
    http.http_get()

    # MQTT connection
    #mqtt = MQTT()
    
    modem.close()
