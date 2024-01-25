# 1st Project 

Very first project includes various aims and purposes. These are quite essential to obtain basic skills of using Embedded Linux, Raspberry Pi, Python, Git and Github, Project planning and so on. This Documentation includes:

 - Understandable project documentation
 - Weekly project plan
 - Gantt Chart

> “A man who does not plan long ahead will find trouble at his door.”      	Confucius

# Purposes

 - Understanding embedded linux systems
 - Compability with Raspberry Pi
 - Ascertain linux commands
 - Writing maintable codes in Python with using OOP
 - Learning basic information about cellular network modems. Ability to send and receive data in basic protocols using a modem.
 - Project planning and documentation

These valuable purposes is **highly  important** to achieve tasks.

# Project Requirements

* A Python library will be written to talk to the modem, change its settings, send and receive data. The library must be able to send AT commands to talk to the modem and process the responses from the modem.
  * Extra: Automatic recognition of modem serial port.
  * Extra: Serial port, baudrate, parity etc. Customize serial port settings.
* A sample code will be written that sends HTTP GET and POST requests to [webhook.site](http://webhook.site) over the modem. This code will use the library we wrote before.
* A sample code will be written that sends an MQTT message to a topic on [hivemq](https://www.hivemq.com/mqtt/public-mqtt-broker/), which is a free and open MQTT broker, via modem. By subscribing to the same topic, the message sent here will be read by the modem again. This code will use the library we wrote before.
* Raspberry Pi will be able to access the internet via modem.
  * With PPP protocol
  * With QMI/RMNET protocol
  * With ECM protocol
* The speeds of the connections established with these 3 protocols will be measured and a general comparison of the protocols will be made.

# Project Tools and Hardware

### Tools

 - Python programming language
 - Linux operating system
 - Bash
 - Git and Github
 - Markdown for reports
 - Gantt Chart
 
### Hardware

 - Raspberry Pi 3B+
 - SD Card and reader
 - Raspberry Pi Base Hat
 - Quectel  EG25-G  Modem
 - Antennas
 - SIM card
  

# Operation Plan

This project has to be done within 6 weeks. That requires a dynamic agile project plan to obtain the best outcome from the project. Change planning is a must.

## Week 1

 - [x] Understanding basic git commands to form a repository
 - [x] Initialize a git repository
 - [x] Learn how to use markdowns
 - [x] Installation of Raspberry Pi 3B+ and ascertaion related bash commands
 - [x] Prepare a project plan
 - [x] Prepare a Gantt Chart
 - [x] Report into `Reports` folder

## Week 2

 - [x] Work on AT commands
 - [x] Initialize a src folder for source files
 - [x] Process the responses from the modem
 - [x] Basic test

## Week 3

 - [x] Initialize AT commands on the src file
 - [x] SSH connection
 - [x] PPP connection

## Week 4

 - [x] Complete request code
 - [x] Send HTTP GET and POST request
 - [x] MQTT message sending


## Week 5

 - [x] HTTP implementation with additional functions
 - [x] MQTT implementation
 - [x] Improvements on library

## Week 6

 - [x] MQTT Implementation
 - [x] HTTP control
 - [] Additional feature implementation
 - [x] QMI, ECM and PPP comparison
 - [x] Final Report

# Gantt Chart

Gantt charts are quite essential in project planning to observe:

 - Timeline
 - Dependencies
 - Milestones
 in a visualized manner. That allows to follow the project better.

![gantt_chart](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/347e2466-138d-41f9-ad15-35fcaf3b2ab2)


---

|      Tasks      |    Begin Date    |   End Date   |
|-----------------|------------------|--------------|
|Research stage|4.12.23|14.12.23|
|Completing installations (hardware included)|8.12.23|11.12.23|
|Implementing requirements on Python library|12.12.23|16.12.23|
|HTTP GET and POST requests over modem|16.12.23|20.12.23|
|Sending MQTT message|20.12.23|24.12.23|
|Raspberry Pi protocol implementations|24.12.23|30.02.24|
|Connection establishment control and comparison|2.12.23|7.02.24|
|Extra part comparison and implementation|7.12.23|12.02.24|
|Final report|12.12.23|14.02.24|
