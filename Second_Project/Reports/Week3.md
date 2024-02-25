# Week 3

On the first week my responsibilities were understanding the basics of:
- Send message to Telegram channel 
- State Manager
- create_your_own_method.py
- ThingsBoard App
- MQTT and HTTP features

and all these are studied well. Report related to these titles can be found below.


# Telegram Message
For Telegram message implementation from [following documentation](https://docs.sixfab.com/docs/pico-lte-http-request-to-web-server) steps has been followed one by one.

1. BotFather integrated via Telegram to generate a new bot for individual processes.
	a. /newbot
	b. Bot name
	c. Bot username 
	Then BotFather allows you to have a token for GET and POST HTTP methods.
2. From related url of the new bot access is available to your personal bot. Messages can be send and received from Pico LTE. 

This application can allow IoT devices to respond relative situations according to commands. 

![telegram1](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/c0b06b36-9d30-48d8-9462-88db514252cd)

![Screenshot from 2024-02-22 22-45-13](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/5054d2c1-0356-4b73-939b-6af9c4a5d96c)


# State Manager
State manager refers as a "class" that manages states for the program. These stages may vary related to the project that you're working on but currently it has features as:
1. Adding step
2. Updating step
3. Getting step
4. Clear related counter to this step process
5. Increasing step number
6. Organizing these steps
7. Executing
8. Handling success and failure
9. Run

These steps may seem easy to write and understand yet they are the core values for application processing. 

# create_your_own_method.py
Inside PicoLTE SDK repository "create_your_own_method.py" can be found. This method is a guideline for users to understand how to imply their own method related to apps or processes. Aim is to figure out how to use manager utility. Manager is an important utility to manage processes with:
1. Multiple steps
2. Specific execution order
3. Response binded decision

and so on. This file let user to understand how to work with manager. To work with this python file there are various steps to build base and understand fundamentals of working system. 
First of all, all the utilities importing from PicoLTE modem class. So at this point user do not need to interact with AT commands to accomplish to send POST request or publish MQTT message. Here things are related how to state the manager structure and how to deploy steps related to your application. Every step is related with four main variable:
1. **name**: Define name for the step
2. **function**: Such as network registration of pdp preparation
3.  **success**: Define next step in case of success
4. **fail**: failure
5. **retry**: Number of retries
6. **function_params**: Parmeters for related functions such as messages
7. **interval**: Time interval between each steps

These step paramters are essential for the process that you want to apply. With help of manager object all steps have to be added to it. Then manager can be run. Here an example process can be found below:

```
from pico_lte.utils.status import Status
from pico_lte.utils.manager import StateManager, Step
from pico_lte.core import PicoLTE

def example_MQTT_subscribe(topic):

	picoLTE = PicoLTE()

	step_1_network_check = Step(
		name="net_check",
		function=picoLTE.network.register_network,
		success="connect",
		fail="failure",
	)

	step_2_connect = Step() #set broker and etc.
	.
	.
	.

	manager = StateManager()
	manager.add_step(step_1_network_check)
	manager.add_step(step_2_connect)
	.
	.
	.
	
	while True:
		result = manager.run()
		# handle success and error status
```

# ThingsBoard App
[ThingsBoard App](https://thingsboard.io/) is an open-source IoT platform for data collection, processing, visualization, and device management. It enables device connectivity via industry standard IoT protocols - MQTT, CoAP and HTTP and supports both cloud and on-premises deployments. ThingsBoard combines scalability, fault-tolerance and performance so it offers data will never to lose.

# MQTT and HTTP features
 MQTT (Message Queue Telemetry Transport) and HTTP (Hypertext Transfer Protocol) are two popular communication protocols used in IoT (Internet of Things) applications. Here are some differences, common points, advantages, and disadvantages between MQTT and HTTP:

**Differences:**
-   MQTT is a lightweight, publish-subscribe protocol, while HTTP is a request-response protocol.
-   MQTT uses a broker to handle messages, while HTTP uses a server to handle requests.
-   MQTT has a small overhead, while HTTP has a larger overhead.
-   MQTT is designed for low-bandwidth, high-latency networks, while HTTP is designed for high-bandwidth, low-latency networks.

**Common Points:**
-   Both MQTT and HTTP are used to transfer data between devices and servers.
-   Both MQTT and HTTP are supported by most IoT platforms.
-   Both MQTT and HTTP can be secured using SSL/TLS.

**Advantages of MQTT:**
-   Low overhead, which makes it ideal for low-power, battery-operated devices.
-   Publish-subscribe model, which allows for many-to-many communication.
-   Quality of Service (QoS) levels, which ensure message delivery.
-   Support for offline messages, which allows devices to receive messages when they are offline.

**Disadvantages of MQTT:**
-   Not as widely supported as HTTP.
-   Not as well understood as HTTP.
-   Not as secure as HTTP.

**Advantages of HTTP:**
-   Widely supported by most devices and servers.
-   Well understood by most developers.
-   Secure, with support for SSL/TLS.

**Disadvantages of HTTP:**
-   Higher overhead, which makes it less suitable for low-power, battery-operated devices.
-   Request-response model, which limits communication to one-to-one.
-   No support for offline messages.

For the project that interacts with ThingsBoard App selection between HTTP and MQTT depends on process requirements. HTTP requires high-bandwith and low-latency so at this state using HTTP is more beneficial for this project.
