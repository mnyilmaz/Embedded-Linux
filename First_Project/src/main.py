from inputs import *
import serial, time, base, http_lib, mqtt_lib 

# Base
base = base.Connection()

# HTTP
http = http_lib.HTTP()
    
# MQTT
mqtt = mqtt_lib.MQTT()

class Execute:
    def control_base(self):
        base.check_base()
    
    # HTTP Implementations
    def http_get(self):
        http.config()
        http.set_PDP()
        http.connect()
        http.http_get()
        
    def http_post(self):
        http.set_PDP()
        http.connect()
        http.http_post()
    
    # MQTT Implementations
    def mqtt_sub(self):
        mqtt.connect()
        mqtt.subscribe()
    
    def mqtt_pub(self):
        mqtt.connect()
        mqtt.publish()
        
if __name__ == "__main__":

    exc = Execute()
    # Check
    exc.control_base()

    # HTTP
    exc.http_get()

    # MQTT
    exc.mqtt_pub()

    modem.close()
