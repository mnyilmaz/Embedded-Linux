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
