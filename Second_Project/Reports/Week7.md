# Week 7

On the first week my responsibilities were:
- MQTT connection tests over ThingsBoard App
and all these are studied well. Report related to these titles can be found below.


# ThingsBoard MQTT Host
After completing successfull test over MQTT Explorer I've changes host as:
```
demo.thingsboard.io
```
Re-organised config file as:
```
{
    "thingsboard": {
        "host":"demo.thingsboard.io",
        "port": 1883,
        "pub_topic": "v1/devices/me/telemetry",
        "username": "some_username",
        "password": "",
        "qos": 1,
    },
}
```
and turned payload into:
```
payload = {"temperature":30}
```
to follow as the same instruction at ThingsBoard App. Yet after first run, following result has raised:
```
INFO: Result: {'status': 1, 'response': ['+QMTCONN: 0,0,2', '+QMTSTAT: 0,4'], 'interval': 0}
```
When I followed to Quectel Documentation for [BG96 MQTT Applicaiton](https://www.quectel.com/wp-content/uploads/2021/03/Quectel_BG96_MQTT_Application_Note_V1.2.pdf)
outputs were as below:

 - +QMTCONN: 0,0,2: Connection Refused: Identifier Rejected
 - +QMTSTAT: 0,4: Receiving CONNACK packet timed out or failed.

To resolve that I've made device public on ThingsBoard and got clientId from the device. Then results were as this:
```
INFO: Result: {'status': 1, 'response': ['+QMTCONN: 0,0,5', '+QMTSTAT: 0,4'], 'interval': 0}
```
 - +QMTCONN: 0,0,5: Connection Refused: Not Authorized

This result was due to authorization that means access token must be implemented via different processes. 
So I implemented access token into username and send MQTT message to the device. Response was as this:
```
INFO: Result: {'status': 0, 'response': ['OK'], 'interval': 0}
```
![Screenshot from 2024-03-25 01-26-12](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/6768aa28-c5b4-43d5-afa2-5c4440707256)

Yet device set itself into inactive due to that I could not observe the output.
I re-set device to active, response was still OK but on telemetry page values were not observable. 
![Screenshot from 2024-03-25 01-25-04](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/60c9924c-fd86-4da7-ad50-feb87c65000b)

