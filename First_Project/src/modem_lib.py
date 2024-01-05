import serial

modem = serial.Serial('/dev/ttyUSB2', 115200, timeout=5)
#command = 'AT+QCFG="usbnet"'
byte = 256

class HTTP:
    AT_COMMANDS = {
        'classic': 'AT+QCFG',
        'display': 'AT+V',
        'ue_reboot': 'AT+CFUN',
        'parameter': 'AT+QHTTPCFG', # Configures parameters for HTTP(S) server
        'webhook': 'AT+QHTTPURL',
        'post_request': 'AT+QHTTPPOST',
        'get_request': 'AT+QHTTPGET',
        'cancel': 'AT+QHTTPSTOP',
    }
    
    def __init__(self):
        pass


    def at_command(at_command):
        try:
            modem.write((at_command + '\r\n').encode())
        finally:
            response = modem.read(byte)
            print("Received response:", response.strip().decode())
            modem.close()

    def set_APN():
        '''
            to dynamically assign IP use AT+CGACT
        '''
        ip = input("Enter your IP: ") 
        apn = input("Enter your APN: ") 
        command = 'AT+CGIP="%s"; AT+CGDCONT=1,"IP","%s"' % (ip, apn)
        try:
            modem.write(b'f' + command.encode() + b'\r')
        finally:
            response = modem.read(byte)
            print("Received response:", response.strip().decode())
            modem.close


    # Displays current settings
    def display_current():
        at_command(AT_COMMANDS['display'])

    def zero_check(response):
    parts = response.split(":")
    value = parts[1].strip()
    if value == "0":
        return True
    return False

    # Check the current settings
    def check_settings():
        command = 'AT+QCFG="usbnet"'
        try:
            modem.write(b'f' + command.encode() + b'\r')
        finally:
            response = modem.read(byte)
            if zero_check(response) == True:
                modem.write(b'f' + 'AT+QCFG="usbnet",0'.encode() + b'\r')
            print("Received response:", response.strip().decode())
            modem.close()

    # Set UE functionality and reset 
    def ue_reboot(com, byte):
        command = 'AT+CFUN'
        try:
            modem.write(b'f' + command.encode() + b'\r')
        finally:
            response = modem.read(byte)
            if response.contains('ERROR'):
                print('An error occured')
                modem.close()
            print("Received response:", response.strip().decode())
            modem.close()

    # HTTP settings
    def config():
        send_command(AT_COMMANDS['parameter'])
        
    def http_url(url):
        command = AT_COMMANDS['webhook'] % url
        at_command(command)

    def http_post():
        send_command(AT_COMMANDS['post_request'])

    def http_get():
        send_command(AT_COMMANDS['get_request'])
    
    def http_stop():
        send_command(AT_COMMANDS['cancel'])

class MQTT:
    pass

if __name__ == "__main__":
    
    http = HTTP()
    mqtt = MQTT()
