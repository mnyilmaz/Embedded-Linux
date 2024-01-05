# Week 4

On the fourth week my responsibilities were:
-   Re-install Raspberry pi due to recovery error
-   Inspect related AT commands for modem
-   Implement related AT commands as functions
-   Learn unit tests
-   Week 4 report
  
and all these are studied well. Report related to these titles can be found below.

# Re-installaiton of Raspberry Pi
After updating the system, I had an error that given down below:

Only solution was re-installing the OS. So with Raspberry Imager I've re-installed it.

# Inspect Related AT Commands
For this part I have inspected Quectel's AT commands file.
[Quectel EG25 Manual](https://forums.quectel.com/uploads/short-url/cBnrTmjnCg7OGnqRsk8dIpbHuVX.pdf)

Related with this documentation I've added following functions to my library:
```
# Displays current settings

def  display_current():
	at_command(AT_COMMANDS['display'])

def  zero_check(response):
	parts = response.split(":")
	value = parts[1].strip()
	if value ==  "0":
		return  True
	return  False

# Check the current settings
def  check_settings():
	command =  'AT+QCFG="usbnet"'
	try:
		modem.write(b'f'  + command.encode() +  b'\r')
	finally:
		response = modem.read(byte)
		if  zero_check(response)  ==  True:
			modem.write(b'f'  +  'AT+QCFG="usbnet",0'.encode() +  b'\r')
		print("Received response:", response.strip().decode())
		modem.close()

# Set UE functionality and reset
def  ue_reboot(com,  byte):
	command =  'AT+CFUN'
	try:
		modem.write(b'f'  + command.encode() +  b'\r')
	finally:
		response = modem.read(byte)
		if response.contains('ERROR'):
			print('An error occured')
			modem.close()
		print("Received response:", response.strip().decode())
		modem.close()
```


# Errors that Encountered
At first these part of the code was working fine but after re-installation of Raspberry Pi it couldn't recognize the AT commands, atcom and etc. Also port errors have been raised.



