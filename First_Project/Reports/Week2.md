# Week 2

On the second week my responsibilites were:
-   Work on AT commands
-   Initialize a src folder for source files
-   Process the responses from the modem
-   Basic test
-   Week 2 report
  
and all these are studied well. Report related to these titles can be found below.

# AT Commands
AT commands are primarily used to configure a modem and establish its network connection. They can be used to interrogate the modem's Super SIM.
In this project AT commands are highly required to achieve connection with SIM over the modem. Throughout this task first installation of modem is essential. To install:

1. Check if USB is inserted and can be seen:
```
lsusb
```
2. Using the documentation complete installation (PPP)
- [PPP Protocol](https://docs.sixfab.com/page/setting-up-the-ppp-connection-for-sixfab-shield-hat)
- [Setup of PPP](https://www.twilio.com/docs/iot/supersim/getting-started-super-sim-raspberry-pi-sixfab-base-hat)
After installaiton check the connection by steps:
	1. `sudo pon`
	2. `ifconfig`
	From the ifconfig command ppp0 connection can be seen.

### PPP
Point-to-Point Protocol (PPP) is a data link layer protocol designed for establishing and maintaining direct connections between two network nodes, commonly used in dial-up connections. PPP encapsulates multiprotocol data frames for transmission over various physical media, supporting protocols such as IP, IPv6, and IPX. It includes authentication mechanisms like PAP and CHAP, ensuring secure communication, and features error detection to maintain data integrity. PPP handles connection establishment, maintenance, and termination, and its flexibility allows for negotiation of network layer protocols during the connection setup. While traditionally associated with dial-up, PPP remains a foundational protocol and is often used in conjunction with technologies like PPPoE in broadband connections.

    
   
Later on AT commands have to become meaningful over the modem. Here is a guide from Quectel itself:
- [Quectel AT Commands Manuel](https://www.quectel.com/wp-content/uploads/2021/05/Quectel_RG50xQRM5xxQ_Series_AT_Commands_Manual_V1.1.pdf)
- [Modems and AT Commands](https://en.m.wikibooks.org/wiki/Serial_Programming/Modems_and_AT_Commands)
- [AT Commands with Raspberry](https://forums.raspberrypi.com/viewtopic.php?t=183796)
  
On example test baud rate set to 9600 ms. The baud rate is a unit of measurement in data transmission that refers to the rate at which symbols are transmitted over a communication channel. It is measured in symbols per second (Bd). Simply put, it's like the speed of a data highway: the higher the baud rate, the more symbols can be sent per second, and the faster data can be transferred. 
```
Baud rate = Bit rate / Number of bits per symbol

```

Througout this week codes has been written on VIM due to Raspberry's performance with other IDE's (Geany, VSCode).
Basic commands were sent such as 'hello world' and configurations checked.
