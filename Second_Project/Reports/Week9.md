# Week 9

On the ninth week my responsibilities were:
- MQTT Subscribe tests
- Documentation
and all these are studied well. Report related to these titles can be found below.


# MQTT Subscribe Tests
Earlier my attempts over subscribing was within private device that I specify credentials. Later on I made device Public yet credentials were the same, subscribing function over command line was up to work. Yet still over the code I couldn't observe the telemetry values that I've sent as temperature value. To check them one by one I've used AT commands directly over the device. The code for publishing can be found below:

```
from pico_lte.common import debug
from pico_lte.utils.atcom import ATCom
from pico_lte.utils.status import Status

THINGSBOARD_HOST = "demo.thingsboard.io"
DEVICE_TOKEN = "my_token"
TOPIC = "v1/devices/me/attributes"

atcom = ATCom()

atcom.send_at_comm('AT+QMTCFG="version",0,4')  
atcom.send_at_comm('AT+QMTCFG="keepalive",0,60') 
atcom.send_at_comm(f'AT+QMTOPEN=0,"{THINGSBOARD_HOST}",1883')  
atcom.send_at_comm(f'AT+QMTCONN=0,"{DEVICE_TOKEN}"')

response = atcom.send_at_comm(f'AT+QMTSUB=0,1,"{TOPIC}",1')
print(response)
```

Result of this can be found at below:

![Screenshot from 2024-04-08 16-49-09](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/2f2259d5-a1f4-4a02-9609-1074c14de57a)


Later on I tried MQTT subscribe.py example over [MQTTHQ](https://mqtthq.com) yet result was as given below:

![Screenshot from 2024-04-08 16-47-53](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/2af1b471-66fd-41a6-9c9a-1d68aeffe28e)


Over my code I've tried subscription through MQTTHQ yet still response cannot be delivered. 

# Documentation
Between these errors due to subscription I've started and nearly completed documentation. In three sections such as:
1. ThingsBoard Configuration
2. Publishing
3. Subscribing

Assets are being prepared for these documentation.
