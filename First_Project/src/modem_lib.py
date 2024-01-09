import serial
import time

class Connection:

    def at_command(self, at_command, explanation):
        try:
            modem.write((at_command + '\r\n').encode())
        finally:
            response = modem.read(byte)
            print(f"Received {explanation} response:\n{response.decode()}\n")
            return response
    
    # Check if base connection exists
    def check_base(self):
        self.at_command(AT_COMMANDS['base'], AT_COMMANDS['base'])
    
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
                print('An error occured')
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
    
    
    def check_url(self):
        self.con.at_command(HTTP_AT_COMMANDS['check_url'], HTTP_AT_COMMANDS['check_url'])
        
    def http_url(self):
        self.con.at_command(HTTP_AT_COMMANDS['webhook'], HTTP_AT_COMMANDS['webhook'])
        
    def check_get(self):
        self.con.at_command(HTTP_AT_COMMANDS['check_get'], HTTP_AT_COMMANDS['check_get'])
        
    def http_get(self):
        self.con.at_command(HTTP_AT_COMMANDS['get_request'], HTTP_AT_COMMANDS['get_request'])
        
    def check_post(self):
        self.con.at_command(HTTP_AT_COMMANDS['check_post'], HTTP_AT_COMMANDS['check_post'])

    def http_post(self):
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

    def check_network(self):
        self.con.at_command(MQTT_AT_COMMANDS['is_open'], MQTT_AT_COMMANDS['is_open'])
        
    def open_network(self):
        self.con.at_command(MQTT_AT_COMMANDS['open_net'], MQTT_AT_COMMANDS['open_net'])
    
if __name__ == "__main__":
    
    modem = serial.Serial('/dev/ttyUSB2', 115200, timeout=5)
    byte = 256
    http_url = "https://webhook.site/83abfba6-e208-43d9-8cd0-fe5bd2c4a792"

    AT_COMMANDS = {
        'base': 'AT+CGREG?',
        'PDP_check': 'AT+CGACT=?',
        'PDP_set': 'AT+CGACT=1,1',
        'IP_check': 'AT+CGPADDR=?',
        'classic': 'AT+QCFG',
        'display': 'AT+V',
        'ue_reboot': 'AT+CFUN',
    }
    
    HTTP_AT_COMMANDS = {
        'querry_PDP': 'AT+QIACT?', # Query the state of PDP context
        'activate_PDP': 'AT+QIACT=1', # Activate PDP        
        'http_settings': 'AT+QHTTPCFG=?', # Configures parameters for HTTP(S) server
        'connect': 'AT+QIOPEN=1,0,"TCP","https://webhook.site/83abfba6-e208-43d9-8cd0-fe5bd2c4a792",80',
        'check_url': 'AT+QHTTPURL=?',
        'webhook': 'AT+QHTTPURL=57,80',
        'check_get': 'AT+QHTTPGET=?',
        'get_request': 'AT+QHTTPGET=80',
        'check_post': 'AT+QHTTPPOST=?',
        'post_request': 'AT+QHTTPPOST=48,80,80',
        'cancel': 'AT+QHTTPSTOP',
        'end': 'AT+QICLOSE=1',
    }
    
    MQTT_AT_COMMANDS = {
        'settings':'AT+QMTCFG=?', # Configure optional parameters of MQTT
        'is_open': 'AT+QMTOPEN?', # Check status 
        'open_net': 'AT+QMTOPEN="1","broker.hivemq.com","8883"', # Open a network for MQTT client id, hostname, port
        'close_net': 'AT+QMTCLOSE=1',
        'connect': 'AT+QMTCONN=1,"deneme","deneme"',
        'disconnect': 'AT+QMTDISC=1', # Disconnect a client
        'subscribe': 'AT+QMTSUB=1,1,"message_list"', # cleintID, messageID, topic
        'unsubscribe': 'AT+QMTUNS=1,1,"message_list"', # cleintID, messageID, topic
        'publish': 'AT+QMTPUBEX=1,1,1', # clientID, messageID, qos
        'read': 'AT+QMTRECV=1', # clientID
        
    }
    
    connected = Connection()
    #connected.check_base()
    #connected.check_PDP()
    #connected.check_IP()
    #connected.set_APN()
    
    http = HTTP()
    #http.config()
    #http.set_PDP()
    #http.check_url()
    #http.http_url()
    #http.check_get()
    #http.http_get()
    #http.check_post()
    #http.http_post()
        
    mqtt = MQTT()
    #mqtt.config()
    #mqtt.check_network()
    mqtt.open_network()
    
    
    modem.close()
    
