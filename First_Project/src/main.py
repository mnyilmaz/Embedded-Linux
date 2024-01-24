import serial

if __name__ == "__main__":
    modem = serial.Serial('/dev/ttyUSB3', 115200, timeout=5)
    byte = 1024

    BASE = {
        'sim': 'AT+CPIN?',
        'network': 'AT+CREG?',
        'gprs': 'AT+CGREG?',
        'base': 'AT+COPS?',
        'ue_reboot': 'AT+CFUN=1,1'
    }

    HTTP_AT = {
        'querry_PDP': 'AT+QIACT?',
        'activate': 'AT+QIACT=1',
        'deactivate': 'AT+QIDEACT=1',
        'url': 'https://webhook.site/',
        'check_url': 'AT+QHTTPURL?',
        'get_request': 'AT+QHTTPGET=80',
        'read':'AT+QHTTPREAD=80',
        'post_request': 'AT+QHTTPPOST=10,50',
        'message': 'hello http',
        'cancel': 'AT+QHTTPSTOP',
        'end': 'AT+QICLOSE=1'  
    }
    
    MQTT_AT = {
        'set': 'AT+QMTCFG="recv/mode",0,0,1',
        'open_net': 'AT+QMTOPEN=0,"broker.hivemq.com",1883', # Open a network for MQTT client id, hostname, port
        'is_open': 'AT+QMTOPEN?', # Check status 
        'connect': 'AT+QMTCONN=0,"embedded"', # clientID
        'sub1': 'AT+QMTSUB=0,1,"topic/example",2', # clientID, messageID, topic
        'sub2': 'AT+QMTSUB=0,1,"topic/pub",0', # clientID, messageID, topic
        'publish': 'AT+QMTPUBEX=0,0,0,0,"topic/pub",30', # clientID, messageID, qos
        'message': 'hello mqtt',
        'read': 'AT+QMTRECV=0', # clientID
        'close_net': 'AT+QMTCLOSE=0', # clientID
        'disconnect': 'AT+QMTDISC=0', # Disconnect a client
        'unsubscribe': 'AT+QMTUNS=0,1,"topic/example"' # cleintID, messageID, topic      
    }   

    # Base connection
    connect = Connection()
    #connect.check_base()
    #connect.set_APN()

    # HTTP connection
    #http = HTTP()
    #http.config()
    #http.set_PDP()
    #http.connect()
    #http.http_get()
    #http.http_read()
    #http.http_post()

    # MQTT connection
    mqtt = MQTT()
    mqtt.connect()
    #mqtt.subscribe()
    mqtt.publish_message()
    
    modem.close()
