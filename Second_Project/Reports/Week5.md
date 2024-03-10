# Week 5

On the fourth week my responsibilities were:
- Configure config file
- Network connections
- MQTT Server
- Heat or GPS values

and all these are studied well. Report related to these titles can be found below.


# Configure config file
From latest meeting we've decided to get more parameters from config file such as device name. I also included host and port to the config file for a better user interface. My previous version was 
not including these parameters. For publish and subscribe config.json can be found below:

```
config.json
{
    "thingsboard": {
        "host":"[HOST_ADDRESS]",
        "port": [PORT_NUMBER],
        "client_id": "[DEVICE_MQTT_CLIENT_ID]",
        "username": "[DEVICE_MQTT_USERNAME]",
        "password": "[DEVICE_MQTT_PASSWORD]",
        "device_name": "[DEVICE_NAME]",
        "pub_qos": [QoS],
        "sub_topics": [
            ["[YOUR_MQTT_TOPIC]"]
        ]
    }
}
```
```
config.json
{
    "thingsboard": {
        "host":"[HOST_ADDRESS]",
        "port": [PORT_NUMBER],
        "client_id": "[DEVICE_MQTT_CLIENT_ID]",
        "username": "[DEVICE_MQTT_USERNAME]",
        "password": "[DEVICE_MQTT_PASSWORD]",
        "device_name": "[DEVICE_NAME]",
        "pub_topic": "[YOUR_MQTT_TOPIC]"
    }
}
```

# Network Connections
Project base is ThingBoard app but earlier, I've installed MQTT-Explorer to make sure connection has established. At first basic configuration failed due to core.py configuration. Related to this error
core.py file edited as:
```
from pico_lte.apps.thingsboard import ThingsBoard

self.thingsboard = ThingsBoard(self.base, self.network, self.mqtt)
```
from modules only network and mqtt are required. Few attempts has been made on publishing messages yet it is only for publishing and adding new connection does not work for me. Even after permissions still
forming a new connection is not available. Due to that for testing I still use test.mosquitto.org.

![Screenshot from 2024-03-10 23-09-23](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/cb212fb2-eb96-4d7d-8ab7-fff6f8784e51)

# MQTT Server
Under thingsboard.py publish message and subscirbe topics has been initialized. Few examples related to these functions can be found as:
```
        if host is None:
            host = get_parameter(["thingsboard", "host"])
            #host = get_parameter(["thingsboard", "host"], "test.mosquitto.org")
            

        if port is None:
            port = get_parameter(["thingsboard", "port"])
            #port = get_parameter(["thingsboard", "port"], 1883)
            

        if client_id is None:
            client_id = get_parameter(["thingsboard", "client_id"])

        if username is None:
            username = get_parameter(["thingsboard", "username"], )

        if password is None:
            password = get_parameter(["thingsboard", "password"])

        if topic is None:
            topic = get_parameter(
                ["thingsboard", "pub_topic"],
                "channels/" + str(self.channel_id) + "/publish",
            )
```

Yet after completing basics of this code I tried to run but error down below occured:

![Screenshot from 2024-03-10 23-37-20](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/467a1256-1184-4d83-82c1-76dd39132297)

I've re-implemented all the imports yet could not solve the problem. Next week I'll be re-writing the code to see the source of this error. It might occur from Thonny IDE.

# Heat or GPS values
Earlier weeks, I was able to get heat values from embedded sensor of the Pico. MQTT side is not working due to that publishing heat values were not avaliable at the moment.




