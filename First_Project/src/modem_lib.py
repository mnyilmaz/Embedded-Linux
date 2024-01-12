import serial
import time

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
        self.at_command(AT_COMMANDS['base1'], AT_COMMANDS['base1'])
        self.at_command(AT_COMMANDS['base2'], AT_COMMANDS['base2'])
        self.at_command(AT_COMMANDS['base3'], AT_COMMANDS['base3'])
        
    
    # Check IP
    def check_IP(self):
        self.at_command(AT_COMMANDS['IP_check'], AT_COMMANDS['IP_check'])
        
    # Check PDP connection, expect output +CGACT: (0,1)
    def check_PDP(self):
        response = (self.at_command(AT_COMMANDS['PDP_check'], AT_COMMANDS['PDP_check'])).decode()
        if 'ERROR' in response:
            print('An error occured')
            self.con.at_command(AT_COMMANDS['PDP_set'], AT_COMMANDS['PDP_set'])
        
    # Set APN 
    def set_APN(self):
        '''
            to dynamically assign IP use AT+CGACT
        '''
        apn = input("Enter your APN: ") 
        ip = input("Enter your IP: ") 
        try:
            modem.write(b'AT+CGDCONT=1,"' + apn.encode() + b'","' + ip.encode() + b'"\r\n')
        finally:
            response = modem.read(byte)
            print("Received AT+CGDCONT=1 response:\n",response.decode())
    
    
    def check_APN(self):
        self.at_command(AT_COMMANDS['check_APN'], AT_COMMANDS['check_APN'])
    
    
    # Displays current settings
    def display_current(self):
        self.at_command(AT_COMMANDS['display'], AT_COMMANDS['display'])


    # Check the current settings
    def check_settings(self):
        command = 'AT+QCFG="usbnet"'
        try:
            modem.write(b'f' + command.encode() + b'\r')
        finally:
            response = modem.read(byte).decode()
            if '0' in response:
                modem.write(b'f' + 'AT+QCFG="usbnet",0'.encode() + b'\r')
            print("Received rAT+QCFG='usbnet', 0 response:\n", response.decode())


    # Set UE functionality and reset 
    def ue_reboot(self, com, byte):
        command = 'AT+CFUN'
        try:
            modem.write(b'f' + command.encode() + b'\r')
        finally:
            response = modem.read(byte)
            if 'ERROR' in response:
                print('An error occured\n')
                modem.close()
            print("Received AT_CFUN response:\n", response.decode())

# HTTP
class HTTP:
    con = Connection()
    
    # HTTP settings
    def config(self):
        answer = input("Would you like to configure settings ? (Y/N): ")
        
        if answer == 'Y':
            contexID = input("contextID: ")
            self.con.at_command("AT+QHTTPCFG=\"contextid\",\"{}\"".format(contexID), 'AT+QHTTPCFG=contextID')
            
            question = input("Would you like to continue ? (Y/N): ")
            if question == 'Y':
                request_header = input("request_header: ")
                self.con.at_command("AT+QHTTPCFG=\"requestheader\",\"{}\"".format(request_header), 'AT+QHTTPCFG=requestheader')
                response_header = input("response_header: ")
                self.con.at_command("AT+QHTTPCFG=\"responseheader\",\"{}\"".format(response_header), 'AT+QHTTPCFG=responseheader')
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
            else:
                print("Default")
            
        if answer == 'N':
            self.con.at_command(HTTP_AT_COMMANDS['settings'], HTTP_AT_COMMANDS['settings'])
        else:
            self.con.at_command(HTTP_AT_COMMANDS['settings'], HTTP_AT_COMMANDS['settings'])
    
    time.sleep(5)
    def set_PDP(self):
        response = (self.con.at_command(HTTP_AT_COMMANDS['querry_PDP'], HTTP_AT_COMMANDS['querry_PDP'])).decode()
        if 'OK' in response:
            try:
                apn = input("Enter your APN: ")
                modem.write(b'AT+QICSGP=1, 1, "' + apn.encode() + b'","", "", 1\r\n')
            finally:
                response = modem.read(byte)
                print("Received AT+QICSGP=1 response:\n", response.decode())
                self.con.at_command(HTTP_AT_COMMANDS['activate_PDP'], HTTP_AT_COMMANDS['activate_PDP'])
                self.con.at_command(HTTP_AT_COMMANDS['check_status'], HTTP_AT_COMMANDS['check_status'])
    
    
    def connect(self):
        self.con.at_command(HTTP_AT_COMMANDS['check_url'], HTTP_AT_COMMANDS['check_url'])
        self.con.at_command(HTTP_AT_COMMANDS['connect'], HTTP_AT_COMMANDS['connect'])  
        self.con.at_command(HTTP_AT_COMMANDS['webhook'], HTTP_AT_COMMANDS['webhook'])
        
    def http_get(self):
        self.con.at_command(HTTP_AT_COMMANDS['check_get'], HTTP_AT_COMMANDS['check_get'])
        self.con.at_command(HTTP_AT_COMMANDS['get_request'], HTTP_AT_COMMANDS['get_request'])
        
    def http_post(self):
        self.con.at_command(HTTP_AT_COMMANDS['check_post'], HTTP_AT_COMMANDS['check_post'])
        self.con.at_command(HTTP_AT_COMMANDS['post_request'], HTTP_AT_COMMANDS['post_request'])

    def http_stop(self):
        self.con.at_command(HTTP_AT_COMMANDS['cancel'], HTTP_AT_COMMANDS['cancel'])
        
    def close_connection(self):
        self.con.at_command(HTTP_AT_COMMANDS['end'], HTTP_AT_COMMANDS['end'])
        

# MQTT
class MQTT:
    con = Connection()
    
    def config(self):
        self.con.at_command(MQTT_AT_COMMANDS['settings'], MQTT_AT_COMMANDS['settings'])  
    
    def connect(self):
        self.con.at_command(MQTT_AT_COMMANDS['set'], MQTT_AT_COMMANDS['set'])
        time.sleep(5)
        self.con.at_command(MQTT_AT_COMMANDS['open_net'], MQTT_AT_COMMANDS['open_net'])
        time.sleep(5)
        self.con.at_command(MQTT_AT_COMMANDS['is_open'], MQTT_AT_COMMANDS['is_open'])
        time.sleep(5)
        self.con.at_command(MQTT_AT_COMMANDS['connect'], MQTT_AT_COMMANDS['connect']) 
    
    def subscribe(self):
        time.sleep(5)
        self.con.at_command(MQTT_AT_COMMANDS['sub1'], MQTT_AT_COMMANDS['sub1'])
        time.sleep(5)
        self.con.at_command(MQTT_AT_COMMANDS['sub2'], MQTT_AT_COMMANDS['sub2'])
        
    
    def publish_message(self):
        self.con.at_command(MQTT_AT_COMMANDS['publish'], MQTT_AT_COMMANDS['publish']) 
        
    
if __name__ == "__main__":
    
    modem = serial.Serial('/dev/ttyUSB2', 115200, timeout=5)
    byte = 256
    http_url = "https://webhook.site/83abfba6-e208-43d9-8cd0-fe5bd2c4a792"

    AT_COMMANDS = {
        'base1': 'AT+CPIN?',
        'base2': 'AT+CREG?',
        'base3': 'AT+CGREG?',
        'check_APN': 'AT+CGDCONT?',
        'PDP_check': 'AT+CGACT=?',
        'PDP_set': 'AT+CGACT=1,1',
        'IP_check': 'AT+CGPADDR?',
        'classic': 'AT+QCFG',
        'display': 'AT+V',
        'ue_reboot': 'AT+CFUN=1',
    }
    
    HTTP_AT_COMMANDS = {
        'querry_PDP': 'AT+QIACT?', # Query the state of PDP context
        'activate_PDP': 'AT+QIACT=1', # Activate PDP
        'check_status': 'AT+QICSGP=1',        
        'http_settings': 'AT+QHTTPCFG=?', # Configures parameters for HTTP(S) server
        'connect': 'AT+QIOPEN=1,0,"TCP","https://webhook.site/83abfba6-e208-43d9-8cd0-fe5bd2c4a792",80',
        'check_url': 'AT+QHTTPURL?',
        'webhook': 'AT+QHTTPURL=\"https://webhook.site/83abfba6-e208-43d9-8cd0-fe5bd2c4a792\",80',
        'check_get': 'AT+QHTTPGET=?',
        'get_request': 'AT+QHTTPGET=80',
        'check_post': 'AT+QHTTPPOST=?',
        'post_request': 'AT+QHTTPPOST=48,80,80',
        'cancel': 'AT+QHTTPSTOP',
        'end': 'AT+QICLOSE=1',
    }
    
    MQTT_AT_COMMANDS = {
        'settings':'AT+QMTCFG=?', # Configure optional parameters of MQTT
        'set': 'AT+QMTCFG="recv/mode",1,0,1',
        'all': 'AT+QMTCFG=\"aliauth\",0,\"oyjtmPl5a5j\",\"MQTT_TEST\",\"wN9Y6pZSIIy7Exa5qVzcmigEGO4kAazZ\"',
        'open_net': 'AT+QMTOPEN=1,"broker.hivemq.com",1883', # Open a network for MQTT client id, hostname, port
        'is_open': 'AT+QMTOPEN?', # Check status 
        'connect': 'AT+QMTCONN=1,"embedded"',
        'sub1': 'AT+QMTSUB=1,1,"topic/example",2', # clientID, messageID, topic
        'sub2': 'AT+QMTSUB=1,1,"topic/pub",0', # clientID, messageID, topic
        'publish': 'AT+QMTPUBEX=1,0,0,0,"topic/pub",30', # clientID, messageID, qos
        'read': 'AT+QMTRECV=1', # clientID
        'close_net': 'AT+QMTCLOSE=1',
        'disconnect': 'AT+QMTDISC=1', # Disconnect a client
        'unsubscribe': 'AT+QMTUNS=1,1,"message_list"', # cleintID, messageID, topic      
    }
    
    connected = Connection()
    #connected.check_base()
    #connected.check_PDP()
    #connected.check_IP()
    #connected.set_APN()
    
    #http = HTTP()
    #http.config()
    #http.set_PDP()
    #http.connect()
    #http.http_get()
    #http.http_post()
        
    mqtt = MQTT()
    #mqtt.config()
    mqtt.connect()
    #mqtt.subscribe()
    #mqtt.publish_message()
    
    modem.close()
