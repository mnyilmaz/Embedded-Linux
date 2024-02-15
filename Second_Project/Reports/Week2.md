# Week 2

On the first week my responsibilities were understanding the basics of:
- Sixfab Pico LTE Module
- Basic protocols such as HTTP
- AT Commands

and all these are studied well. Report related to these titles can be found below.


# AT Commands
From earlier project library, AT command library written in python, I've imported the code below to check values on connection

```
import serial
import time


def at_command(at_command, explanation):
    try:
        modem.write((at_command + '\r').encode())
    finally:
        response = modem.read(byte)
        print(f"Received {explanation} response:\n{response.decode()}\n")
        return response
    
def check_base():
    at_command('AT+CPIN?', 'SIM status')
    at_command('AT+CREG?', 'Network registration')
    at_command('AT+CGREG?', 'GPRS registration')
    at_command('AT+COPS?', 'Base status')
    

if __name__ == "__main__":
    baudrate = 115200
    port = 'dev/ttyACM0'
    byte = 1024
    apn = 'super'
    modem = serial.Serial(port, baudrate, timeout=5)
    check_base()
```
Yet serial module raised an error that, for a while I've looked for the solution.
I've checked serial and pyserial plugins, still there was an error while importing only serial library. To not to waste too much time in this part I've skipped into HTTP part of the documentation. 

> Documentation contains lots of integrations related to communications. Via config.json file it is available to achieve tasks over applications. 

# Bug Fix
Usually I was using MicroPico with SSH connection over Raspberry Pi. But in last days connection over SSH was quite unstable over the VSCode so I've turned into Thonny IDE to run my codes.

![serial-module-error](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/30944e2e-ecd3-4121-a285-49d482df8224)


# HTTP Implementation
For HTTP implementation webhook.site still in use related to its practical usage over HTTP protocol tasks. From [following documentation](https://docs.sixfab.com/docs/pico-lte-http-request-to-web-server) steps has been followed one by one. Yet at first modules continue to raise an error. After controlling some of these configurations this problem has been solved. 
To check connection, I applied CREG command but result was 0,2 means connection is not valid also requests were unable to send. From [troubleshooting documentation](https://docs.sixfab.com/docs/sixfab-pico-lte-troubleshooting#connection-time-too-long) I enabled debug with:
```
from  pico_lte.common  import  debug  
debug.set_level(0)
```

Then tried following commands:
```
$ AT+CREG?
$ AT+CSQ -> for signal quality
$ AT+QNWINFO
$ AT+CGACT=1,1 -> remember from PDP connection?
$ AT+CGATT=1
$ AT+COPS=0
$ AT+CGPADDR=1
```
with using following code:
```
from pico_lte.utils.atcom import ATCom 

atcom = ATCom() 
at_command = "AT+CREG?" # requested command
response = atcom.send_at_comm(at_command) 
print(response)
```
In some regions some of the connection are not available yet module's are produced to scan every possible connection around. This module is one of these modules so it may try to scan undetected or unused connection in the region. To disable this action documentation recommends following application:
```
from  pico_lte.utils.atcom  import  ATCom  
from  pico_lte.modules.base  import  Base 
 
atcom  =  ATCom() 
base  =  Base(atcom) 

""" Set scan sequence (default=00) 
* 00 --> Automatic (eMTC → NB-IoT → GSM) 
* 01 --> GSM priority 
* 02 --> eMTC priority 
"""  

response  =  base.config_network_scan_sequence("01") 
print(response)
```
After these application CREG output was 0,5 as expected. 

From locally stored **pico_lte_sdk** folder example I've run HTTP GET file. At first connection has ended up with **timeout** yet I tried again. This time connection was successful and response was OK. Here are the following outputs:
![get-request](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/9957dfb5-123d-4951-bdd0-f498721c63fb)
![post-request](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/a6fba246-316e-4fc8-a31d-e3844098f04a)
![put-request](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/68639da4-db7c-49e4-bb5a-f50dcd4fe345)
![Screenshot from 2024-02-16 00-47-50](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/a2585766-c857-468f-a987-703fff99bd49)
