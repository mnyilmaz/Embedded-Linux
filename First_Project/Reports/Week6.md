# Week 6

On the fourth week my responsibilities were:
-   MQTT Implementation
-   HTTP controls
-   QMI, ECM and PPP comparison
-   Additional feature implementation
-   Week 6 report
-	Final Report

and all these are studied well. Report related to these titles can be found below.


# MQTT Implementation
For  MQTT I've formed a class named **MQTT**. Later on one by one added AT commands related to the document. For MQTT implementation [hivemq](https://www.mqtt-dashboard.com/) has been used. 

![Screenshot from 2024-01-09 10-55-26](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/acd7c4bf-ea6a-4fdc-b71b-d99f8f697b79)

#### Functions Implementation Related to AT Commands
1. **AT+QMTCFG:** Configure Optional Parameters of MQTT
	There are various parameters under this command. Related to application these commands return specific values for the user. If your applicaiton does not require these spesifications, usage is not needed. Can be used as AT+QMTCFG="desired_parameter" but in my case this usage always raised an error. But AT+QMTCFG=? works just fine. 

![Screenshot from 2024-01-09 11-22-39](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/ee9bc9d2-d78f-4117-854b-0c6f92ef071a)

2.  **AT+QMTOPEN:** Set connection with the server. Can be used as: 			  **AT+QMTOPEN=0,\"broker.hivemq.com\",8884**

3.  **AT+QMTCONN:** Connect to the client. Can be used as: 			  **AT+QMTCONN=0,"clientId"**

4. **AT+QMTSUB:** Subscription to the topic. Can be used as: 			  **AT+QMTSUB=0,1,"testtopic/3",1**
On every subscription process raised an ERROR. Connection is set, topic is set but subscription and publish process fail each time that i ran the code. Even trying with atcom process has failed.

![Screenshot from 2024-01-11 20-31-44](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/fec09dac-1b57-4c2e-94fa-f58ccd10ef85)

