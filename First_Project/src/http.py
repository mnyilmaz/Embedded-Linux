import serial

def at_command(port, baudrate, command, byte):
    com = serial.Serial(port, baudrate, timeout=5)
    try:
        com.write(b'f' + command.encode() + b'\r')
    finally:
        response = com.read(byte)
        print("Received response:", response)
        com.close()

port = '/dev/ttyUSB3'
baudrate = 115200
command = 'AT+CGATT'
byte = 80

at_command(port, baudrate, command, byte)