from base import Connection

class MQTT:
    con = Connection()
       
    def connect(self):
        self.con.at_command(MQTT_AT['set'], 'Set mode')
        self.con.at_command(MQTT_AT['open_net'], 'Broker connection')
        self.con.at_command(MQTT_AT['connect'], 'Connect to the client') 
    
    def subscribe(self):
        self.con.at_command(MQTT_AT['sub1'], 'Subscribe a topic')
        self.con.at_command(MQTT_AT['sub2'], 'Subscribe a topic')
        
    def publish_message(self):
        self.con.at_command(MQTT_AT['publish'], 'Publish message to a topic')
        self.con.at_command(MQTT_AT['message'], 'Message')
        self.con.at_command(MQTT_AT['read'], 'Receive')
