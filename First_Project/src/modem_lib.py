import serial

class Connection:

    def at_command(self, at_command):
        try:
            modem.write((at_command + '\r\n').encode())
        finally:
            response = modem.read(byte)
            print("Received response:", response.strip().decode())
            return response
    
    # Check if base connection exists
    def check_base(self):
        self.at_command(AT_COMMANDS['base'])
    
    # Check PDP connection, expect output +CGACT: (0,1)
    def check_PDP(self):
        response = (self.at_command(AT_COMMANDS['PDP_check'])).decode()
        if 'ERROR' in response:
            print('An error occured')
            self.at_command(AT_COMMANDS['PDP_set'])
    
    
    def set_PDP(self):
        response = (self.at_command(AT_COMMANDS['querry_PDP'])).decode()
        if 'OK' in response:
            try:
                apn = input("Enter your APN: ")
                modem.write(b'AT+QICSGP=1, 1, "' + apn.encode() + b'","", "", 1\r\n')
            finally:
                response = modem.read(byte)
                print("Received response:", response.strip().decode())
                self.at_command(AT_COMMANDS['activate_PDP'])
    
    # Check IP
    def check_IP(self):
        self.at_command(AT_COMMANDS['IP_check'])
    
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
            print("Received response:", response.strip().decode())

    # Displays current settings
    def display_current(self):
        self.at_command(AT_COMMANDS['display'])

    # Check the current settings
    def check_settings(self):
        command = 'AT+QCFG="usbnet"'
        try:
            modem.write(b'f' + command.encode() + b'\r')
        finally:
            response = modem.read(byte).decode()
            if '0' in response:
                modem.write(b'f' + 'AT+QCFG="usbnet",0'.encode() + b'\r')
            print("Received response:", response.strip().decode())

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
            print("Received response:", response.strip().decode())
            

# HTTP
class HTTP:
    con = Connection()
    # HTTP settings
    def config(self):
        answer = input("Would you like to configure settings ? (Y/N): ")
        
        if answer == 'Y':
            contexID = input("contextID: ")
            self.con.at_command("AT+QHTTPCFG=\"contextid\",\"{}\"".format(contexID))
            
            question = input("Would you like to continue ? (Y/N): ")
            if question == 'Y':
                request_header = input("request_header: ")
                self.con.at_command("AT+QHTTPCFG=\"requestheader\",\"{}\"".format(request_header))
                response_header = input("response_header: ")
                self.con.at_command("AT+QHTTPCFG=\"responseheader\",\"{}\"".format(response_header))
                sslctxID = input("sslctxID: ")
                self.con.at_command("AT+QHTTPCFG=\"sslctxid\",\"{}\"".format(sslctxID))
                content_type = input("content_type: ")
                self.con.at_command("AT+QHTTPCFG=\"contenttype\",\"{}\"".format(content_type))
                auto_outrsp = input("auto_outrsp: ")
                self.con.at_command("AT+QHTTPCFG=\"rspout/auto\",\"{}\"".format(auto_outrsp))
                closedind = input("closedind: ")
                self.con.at_command("AT+QHTTPCFG=\"closed/ind\",\"{}\"".format(closedind))
                window_size = input("window_size: ")
                self.con.at_command("AT+QHTTPCFG=\"windowsize\",\"{}\"".format(window_size))
                close_wait_time = input("close_wait_time: ")
                self.con.at_command("AT+QHTTPCFG=\"closewaittime\",\"{}\"".format(close_wait_time))
                username = input("username: ")
                password = input("password: ")
                self.con.at_command("AT+QHTTPCFG=\"auth\",\"%s\":\"%s\"".format(username, password))
                custom_value = input("custom_value: ")
                self.con.at_command("AT+QHTTPCFG=\"custom_header\",\"{}\"".format(custom_value))
            else:
                print("Default")
            
        if answer == 'N':
            self.con.at_command(AT_COMMANDS['settings'])
        else:
            self.con.at_command(AT_COMMANDS['settings'])
            
        
    def http_url(self, url):
        command = AT_COMMANDS['webhook'] % url
        self.con.at_command(command)

    def http_post(self):
        self.con.at_command(AT_COMMANDS['post_request'])

    def http_get(self):
        self.con.at_command(AT_COMMANDS['get_request'])
    
    def http_stop(self):
        self.con.at_command(AT_COMMANDS['cancel'])

# MQTT
class MQTT:
    pass

    
if __name__ == "__main__":
    
    modem = serial.Serial('/dev/ttyUSB2', 115200, timeout=5)
    byte = 256
    url = "https://webhook.site/"

    AT_COMMANDS = {
        'base': 'AT+CGREG?',
        'PDP_check': 'AT+CGACT=?',
        'PDP_set': 'AT+CGACT=1',
        'IP_check': 'AT+CGPADDR=?',
        'classic': 'AT+QCFG',
        'display': 'AT+V',
        'ue_reboot': 'AT+CFUN',
        'querry_PDP': 'AT+QIACT=?', # Query the state of PDP context
        'activate_PDP': 'AT+QIACT=1', # Activate PDP
        'settings': 'AT+QHTTPCFG=?', # Configures parameters for HTTP(S) server
        'webhook': 'AT+QHTTPURL',
        'post_request': 'AT+QHTTPPOST',
        'get_request': 'AT+QHTTPGET',
        'cancel': 'AT+QHTTPSTOP',
    }
    
    connected = Connection()
    connected.check_base()
    connected.set_PDP()
    #connected.check_PDP()
    #connected.check_IP()
    #connected.set_APN()
    
    http = HTTP()
    http.config()
    #http.http_url(url)
    
    modem.close()
    
    #mqtt = MQTT()
