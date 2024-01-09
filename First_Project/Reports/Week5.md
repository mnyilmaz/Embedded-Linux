# Week 5

On the fourth week my responsibilities were:
-   Finish HTTP part
-   Improve library
-   Implement MQTT
-   Resolve problems
-   Week 5 report
  
and all these are studied well. Report related to these titles can be found below.


# Improve Library
set_apn function that I wrote previous week was not able to set IP and APN so new implementations has been made to improve.

1. HTTP and Connection classes have been seperated.
2. Added new function to check connection parameters such as:
```
# Check if base connection exists
def  check_base(self):
	self.at_command(AT_COMMANDS['base'])

# Check PDP connection, expect output +CGACT: (0,1)
def  check_PDP(self):
	response =  (self.at_command(AT_COMMANDS['PDP_check'])).decode()
	if  'ERROR'  in response:
		print('An error occured')
		self.at_command(AT_COMMANDS['PDP_set'])

# Check IP
def  check_IP(self):
	self.at_command(AT_COMMANDS['IP_check'])

# Set APN
def  set_APN(self):
	'''
	to dynamically assign IP use AT+CGACT
	'''
	apn =  input("Enter your APN: ")
	ip =  input("Enter your IP: ")
	try:
		modem.write(b'AT+CGDCONT=1,"'  + apn.encode() +  b'","'  + 			ip.encode() +  b'"\r\n')
	finally:
		response = modem.read(byte)
		print("Received response:", response.strip().decode())
```
Output:

![Screenshot from 2024-01-08 12-53-56](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/8ce9c318-0328-4484-b27b-0f2b9293c7a4)


3. Later on following steps were accomplished:
	1. Checked base conenction
	2. Set PDP wit using APN
	3. Set "contextID" as 1 from HTTP config function
	4. +CME ERROR: 730 obtained after setting up the contextID
	5. Put url with 57 byte length, raised +CME ERROR: 703
	6. Received HTTP GET and response was: OK
	7. +CME ERROR: 703 raised again with AT+QHTTPPOST=values
	
	**703: HTTP(S) busy
	730: Invalid parameter**

I've followed Quectel's documentation.

![Screenshot from 2024-01-09 01-14-15](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/62cff781-ee88-4c99-8635-182e88f6c124)


# MQTT Essentials
MQTT is an OASIS standard messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth. MQTT is a standards-based protocol that enables machine-to-machine communication and is commonly used in the IoT ecosystem to transmit data between low power, resource-constrained IoT devices and the cloud. Specifically, MQTT uses a small code footprint and is well-suited for devices that have limited processing capabilities and/or available memory.

In basis **MQTT** has two main components which are: **clients and brokers.**

#### Clients
Also known as **Publishers and Subscribers.** Client can publish a message to a topic if it's a **Publisher**; can subscribe a message topic if it's a **Subscriber.** A client can be a Publisher and Subscriber **at the same time.**

#### Brokers
Message router between clients. They manage the distribution of messages between clients by keeping the track.


![MQTT_Diagram_gOmDdU4 width-800](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/28f06328-6b0c-4c5d-9c90-0beb318c36eb)


### Features

 - Lightweight and Efficient
 - Large Scale for Connection
 -  Reliable Message Delivery
 - **Bi-directional Communication:** Cloud to device, device to cloud
 - **Unreliable Network Support:** IoT devices connect over unreliable cellular networks
 - **TLS Encryption (Transport Layer Security):** Widely adopted security protocol designed to facilitate privacy and data security for communications over the Internet. HTTPS  is an implementation of TLS encryption on top of the HTTP protocol, which is used by all websites as well as some other web services. Any website that uses HTTPS is therefore employing TLS encryption.
 
[What is MQTT ?](https://www.twilio.com/blog/what-is-mqtt)
[MQTT Applicaiton Note #1](https://www.quectel.com/wp-content/uploads/2021/05/Quectel_EC200xEG912Y_Series_MQTT_Application_Note_V1.1.pdf)
[MQTT Applicaiton Note #2](https://sixfab.com/wp-content/uploads/2020/08/Quectel_EC2xEG9xEM05_MQTT_Application_Note_V1.1.pdf)
