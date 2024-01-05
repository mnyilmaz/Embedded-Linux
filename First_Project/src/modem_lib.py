import serial

class HTTP:

    def at_command(self, at_command):
        try:
            modem.write((at_command + '\r\n').encode())
        finally:
            response = modem.read(byte)
            print("Received response:", response.strip().decode())

    def set_APN(self):
        '''
            to dynamically assign IP use AT+CGACT
        '''
        ip = input("Enter your IP: ") 
        apn = input("Enter your APN: ") 
        command = 'AT+CGIP="%s"; AT+CGDCONT=1,"%s","%s"' % (ip, apn)
        try:
            modem.write(b'f' + command.encode() + b'\r')
        finally:
            response = modem.read(byte)
            print("Received response:", response.strip().decode())

    # Displays current settings
    def display_current(self):
        self.at_command(AT_COMMANDS['display'])

    def zero_check(self, response):
        parts = response.split(":")
        value = parts[1].strip()
        if value == "0":
            return True
        return False

    # Check the current settings
    def check_settings(self):
        command = 'AT+QCFG="usbnet"'
        try:
            modem.write(b'f' + command.encode() + b'\r')
        finally:
            response = modem.read(byte)
            if zero_check(response) == True:
                modem.write(b'f' + 'AT+QCFG="usbnet",0'.encode() + b'\r')
            print("Received response:", response.strip().decode())

    # Set UE functionality and reset 
    def ue_reboot(self, com, byte):
        command = 'AT+CFUN'
        try:
            modem.write(b'f' + command.encode() + b'\r')
        finally:
            response = modem.read(byte)
            if response.contains('ERROR'):
                print('An error occured')
                modem.close()
            print("Received response:", response.strip().decode())

    # HTTP settings
    def config(self):
        answer = input("Would you like to configure settings ? (Y/N): ")
        
        if answer == 'Y':
            contexID = input("contextID: ")
            self.at_command("AT+QHTTPCFG: 'contextid',<%s>", contexID)
            request_header = input("request_header: ")
            self.at_command("AT+QHTTPCFG: 'requestheader',<%s>", request_header)
            response_header = input("response_header: ")
            self.at_command("AT+QHTTPCFG: 'responseheader',<%s>", response_header)
            sslctxID = input("sslctxID: ")
            self.at_command("AT+QHTTPCFG: 'sslctxid',<%s>", sslctxID)
            content_type = input("content_type: ")
            self.at_command("AT+QHTTPCFG: 'contenttype',<%s>", content_type)
            auto_outrsp = input("auto_outrsp: ")
            self.at_command("AT+QHTTPCFG: 'rspout/auto',<%s>", auto_outrsp)
            closedind = input("closedind: ")
            self.at_command("AT+QHTTPCFG: 'closed/ind',<%s>", closedind)
            window_size = input("window_size: ")
            self.at_command("AT+QHTTPCFG: 'windowsize',<%s>", window_size)
            close_wait_time = input("close_wait_time: ")
            self.at_command("AT+QHTTPCFG: 'closewaittime',<%s>", close_wait_time)
            username = input("username: ")
            password = input("password: ")
            self.at_command("AT+QHTTPCFG: 'auth',<%s>:<%s>", username, password)
            custom_value = input("custom_value: ")
            self.at_command("AT+QHTTPCFG: 'custom_header',<%s>", custom_value)
            
        if answer == 'N':
            self.at_command(AT_COMMANDS['settings'])
        else:
            self.at_command(AT_COMMANDS['settings'])
            
        
    def http_url(self, url):
        command = AT_COMMANDS['webhook'] % url
        self.at_command(command)

    def http_post(self):
        self.at_command(AT_COMMANDS['post_request'])

    def http_get(self):
        self.at_command(AT_COMMANDS['get_request'])
    
    def http_stop(self):
        self.at_command(AT_COMMANDS['cancel'])

class MQTT:
    pass

    
if __name__ == "__main__":
    
    modem = serial.Serial('/dev/ttyUSB2', 115200, timeout=5)
    byte = 256
    url = "https://webhook.site/aa36a3cd-93d8-4d37-9ecc-6ab8292fe2ec"

    AT_COMMANDS = {
        'classic': 'AT+QCFG',
        'display': 'AT+V',
        'ue_reboot': 'AT+CFUN',
        'settings': 'AT+QHTTPCFG=?', # Configures parameters for HTTP(S) server
        'webhook': 'AT+QHTTPURL',
        'post_request': 'AT+QHTTPPOST',
        'get_request': 'AT+QHTTPGET',
        'cancel': 'AT+QHTTPSTOP',
    }
    
    http = HTTP()
    http.at_command("AT")
    #http.display_current()
    http.config()
    http.http_url(url)
    
    modem.close()
    

    mqtt = MQTT()
