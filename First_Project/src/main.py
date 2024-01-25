import serial, time, base, http-lib, mqtt-lib 

# Main configurations
baudrate = 115200
port = 'dev/ttyUSB3'
byte = 1024
apn = 'super'
modem = serial.Serial(port, baudrate, timeout=5)
base = base.Connection()

# HTTP
url = 'https://webhook.site/'
get_size = 80
read_size = 80
post_size = 20
latency = 50
http = http-lib.HTTP(apn, url, get_size, read_size, post_size, latency)
    
# MQTT
mode = "recv/mode"
broker = "broker.hivemq.com"
client_port = 1883
client = "embedded"
qos = 1
topic = 1
subscribe = "topic/sub"
publish = "topic/pub"
message_length = 80
mqtt = mqtt-lib.MQTT(mode, broker, port, subscribe, client, qos, topic, publish, message_length)

def control_base(self):
    base.check_base()

def http_get(self):
    http.set_PDP()
    http.connect()
    http.http_get()
    
 def http_post(self): 
    http.set_PDP()
    http.connect()
    http.http_get()

def mqtt_sub(self):
    mqtt.connect()
    mqtt.subscribe()

def mqtt_pub(self):
    mqtt.connect()
    mqtt.publish()
    
if __name__ == "__main__":
    # Check
    control_base()

    # HTTP
    http_get()

    # MQTT
    mqtt_pub()

    modem.close()
