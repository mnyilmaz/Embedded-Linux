# Week 6

On the first week my responsibilities were:
- MQTT connection setup
- Publish and subscribe tests
- Value test

and all these are studied well. Report related to these titles can be found below.


# Uploading new version and run
After updating ThingsBoard app I've uploaded it into Raspberry Pico and run the example that I wrote. Yet there was not any errors also there wasn't any responses at the topic that I selected for this specific application. Response can be found at below. After re-arranging the code I was able to get response from the server.

Example Code:
```
"""
Example code for publish topics for ThingsBoard and
recerving data from ThingsBoard channel by using MQTT.

Example Configuration
---------------------
Create a config.json file in the root directory of the PicoLTE device.
config.json file must include the following parameters for this example:

{
    "thingsboard": {
        "host":"[HOST_ADDRESS]",
        "port": [PORT_NUMBER],
        "pub_topic": "[YOUR_MQTT_TOPIC]",
        "username": "[DEVICE_MQTT_USERNAME]",
        "password": "[DEVICE_MQTT_PASSWORD]",
        "qos": "[QoS]",
    }
}
"""

from pico_lte.core import PicoLTE
from pico_lte.common import debug

picoLTE = PicoLTE()

debug.info("Publishing a message.")


payload = {"device": "temp_sensor", "value_type": "celcius", "area": "indoor", "status": "Temperature value"}

debug.info("Publishing data to ThingsBoard...")
result = picoLTE.thingsboard.publish_message(payload)
debug.info("Result:", result)
```

![Screenshot from 2024-03-17 22-17-59](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/5a06dfb2-fcd4-4a50-a853-d36afdcbe198)
![Screenshot from 2024-03-18 01-38-51](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/07326bf2-d492-4f71-a853-723718261d1c)


# Publish and subscribe tests
From ThinsgBoard app for this time I followed a different approach including gateway configuration. The ThingsBoard IoT Gateway is an open-source solution, designed to serve as a bridge between IoT devices connected to legacy and third-party systems with ThingsBoard. Steps can be found at below:

**1. Dashboard addition (or selection if it exists)**

![Screenshot from 2024-03-18 00-19-22](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/4259a069-9737-48b3-b7aa-fcdbd54ec117)

**2. Add and set a new connector**

![Screenshot from 2024-03-18 00-19-31](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/9f7789d5-c6d0-4030-ad84-7a43a4d1b6c7)
![Screenshot from 2024-03-18 00-21-35](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/3fad2dd8-9f41-4985-8e84-2c0c06d4e6f6)

 MQTT connector configuration establishes a connection to a broker named **“Demo Broker”** at **“host.docker.internal”** on port **1884**, using an 	 
 anonymous security type. It includes a mapping for the **“data/”** topic, specifying a JSON converter and defining attribute and timeseries 		 
 mappings for device data. Additionally, it handles connect and disconnect requests for sensors with expressions to extract device names from topic 	 
 filters.

**3.  Adjust values for testing:** At this point as I thought and designed at first given the device name as in config file yet as I learnt payload is a better option for this. Key values can be used for this. Also I've searched forums and documentation yet I could not find subscribe option for ThingsBoard app.
    


	


