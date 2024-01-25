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
        select = input("Want to change usbnet mode (Y/N) ?: ")
        if select.upper() == 'Y':
            mode = input("Selected mode (1/0): ")
            self.at_command('AT+QCFG="usbnet","{mode}"', 'Set USBNET')
            self.at_command('AT+CFUN=1,1', 'UE Reboot')
        else:
            print("Default")
