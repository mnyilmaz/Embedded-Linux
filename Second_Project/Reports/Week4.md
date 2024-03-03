![Screenshot from 2024-03-02 16-29-21](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/31c8f8bb-b94e-40f1-8063-5257c3a3940a)# Week 4

On the fourth week my responsibilities were:
- Planning
- Python Developer’s Guide and useful installations
- Deciding app requirements
- ThingsBoard Config

and all these are studied well. Report related to these titles can be found below.


# Planning
For this particular part of the project 4 week concluded as sufficient for implementation. Under this repository can be found as "Project_Plan.md"


# Python Developer’s Guide
Overall project uses PEP8 for formatting code. PEP8 allows to make code more readable, understandable and consistent. From indents to spaces, various style rules and applications can be found under this [documentation](https://peps.python.org/pep-0008/). Even importing style has its own style to remain inside the code. 

It is easy to understand styling and typing requirements for PEP8 yet resolving all the errors one by one is not the most efficient way in a daily life of a programmer. 

For this project I use VSCode for development and Thonny for testing the code on Pico. To bring a solution for this problem I've done research about extensions on VSCode. For formatting I've installed **Black Formatter** and **mypy** for type checking. Black Formatter is absolutely time saving for files. Combination of **Ctrl+Shift+I** formats the whole document within a second. 

My recommendation for formatting files, at first try to find out your mistakes on styling and formatting. People generally inclined learn from mistakes. After completing your quick-search format your file and see your shortcomings. 

# Deciding app requirements
ThingsBoard app is more related with sensors linked to device such as arduino, raspberry and so on. These data's from sensors can be stored and visualized via ThingsBoard App website under dashboard. Rapberry Pi Pico LTE module came with embedded heat sensor and GPS antenna. After my research I've decided to write two basic applicaitons. First is to get heat values from environemnt and send them to the dashboard via MQTT. Second is GPS based tracking app that again sends GPS info if sensor or antennta changed its position within 10 meters. Main aim is to achieve heat values, later on under examples folder writing GPS test file. 

# ThingsBoard Config
ThingsBoard website requires to sign in and add your current device. As I follow [documents](https://thingsboard.io/docs/getting-started-guides/helloworld/)
figured out to connect device but haven't tested yet. At first aim is to complete config file then accomplish connection steps. Here basic connection tests and device can be found below:

![Uploading Screenshot from 2024-03-02 16-28-57.png…]()

![Uploading Screenshot from 2024-03-02 16-29-21.png…]()
