### Final Report
On the final week my responsibilities were:
-   MQTT controls
-   HTTP controls
-   QMI, ECM and PPP comparison
-   Additional feature implementation
-   Final report

and all these are studied well. Report related to these titles can be found below.

### Modem Configuration
For a week connection was unstable. Responses from
```
AT+CREG?
AT+QIACT?
AT+COPS?
```
did not match by expected outputs. To adjust following commands had been used:
```
AT+CDGCONT=1,"IPV4V6","super"
AT+CFUN=1,1
AT+QCFG="usbnet"
AT+COPS=0
AT+CGACT=1,1
```
with following configuration above, modem was able to re-connect to the network.

### HTTP Results without Protocols
After re-connect to the network library re-designed for the HTTP part in order to get more clean response.
Also sleep times were re-arranged to get optimum responses.
```
class HTTP():
    def config(self):
        self.con.at_command('AT+QHTTPCFG="contextid",1', 'Context ID Configuration')
        self.con.at_command('AT+QHTTPCFG="responseheader",1', 'Response Header Configuration')        
        answer = input("Would you like to configure more settings? (Y/N): ")
        if answer.upper() == 'Y':
            self.QHTTPCFG_settings()
        else:
            self.con.at_command('AT+QHTTPCFG?', 'HTTP Settings')
        
    def set_PDP(self):
        apn = input("Enter APN: ")
        self.con.at_command(f'AT+QICSGP=1,1,"{apn}","","",1', 'Set APN')
        self.con.at_command(HTTP_AT['querry_PDP'], 'Querry PDP Context')
        self.con.at_command(HTTP_AT["activate"], 'Activate PDP Context')

    def connect(self):
        self.con.at_command(f'AT+QHTTPURL={len(HTTP_AT["url"])},80', 'Set URL')
        time.sleep(10)
        self.con.at_command(HTTP_AT['url'], 'URL')
        time.sleep(5)
        self.con.at_command(HTTP_AT['check_url'], 'Check URL status')
        
    def http_get(self):
        time.sleep(20)
        self.con.at_command(HTTP_AT['get_request'], 'HTTP GET Request')
        
    def http_read(self):
        time.sleep(20)
        self.con.at_command(HTTP_AT['read'], 'Read HTTP Response')
        
    def http_post(self):
        self.con.at_command(HTTP_AT['post_request'], 'HTTP POST Request')
        self.con.at_command(HTTP_AT['message'], 'Message')       
```
After configurations on HTTP part of the library, results were as given in below:

![Screenshot from 2024-01-15 23-12-38](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/ca415de2-0fe2-4535-b16d-9eaba0681d36)

HTTP part has ended for the main part.

### MQTT Results without Protocols
Last week connection had been made for a client, yet after connection errors subscribing and publishing was not
available. While configuring connections MQTT part of the library has been updates as follows:
```
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
```
In here there are no sleep times as can be seen. At first sleep time was 5 seconds yet realized MQTT does not
require that much sleep time and connection can interrupteed or get unconnected. So removed all the sleep time from
MQTT class.

![Screenshot from 2024-01-15 23-45-00](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/c132307b-744c-40b8-9afd-3ea9d36fbaa9)
![Screenshot from 2024-01-15 23-48-35](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/024f1301-6aff-4790-a819-18a8f473e1f0)

MQTT part has ended for the main part.

### ECM (Ethernet Control Modem) Installation and Tests
Ethernet Control Model (ECM) is a protocol designed for establishing and managing network connections via USB. 
This protocol typically allows a device (such as a Raspberry Pi) to connect to a network through a computer using USB.

Following commands had been applied to get ECM connection.
  1. List USB
     ```
     lsusb
     ```

  2. Set APN
     ```
     AT+CGDCONT=1,"IPV4V6","super"
     ```
  3. Configure module as 1, usually 0 is for PPP and QMI
     ```
     AT+QCFG="usbnet",1
     ```
  4. Reboot
     ```
     AT+CFUN=1,1
     ```
  5. Check connection
     ```
     ifconfig usb0
     ping -I usb0 google.com -c 5
     AT+QCFG="usbnet" # Returns 1 
     ```
![ecm_connected_usb0_only](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/01bb8fdb-3de0-45cb-a387-4620029e9751)

In here instead of wwan0 usb0 can be seen. That indicates USB connection.  
After connection is set over the ECM protocol re-run the HTTP and MQTT class functions as given in below:

  1. Base
     ```
     connect = Connection()
     connect.check_base()
     connect.set_APN()
     ```

  2. HTTP
     ```
     http = HTTP()
     http.config()
     http.connect()
     http.http_get()
     http.http_read()
     http.http_post()
     http.close_connection()
     ```
  3. MQTT
     ```
     mqtt = MQTT()
     mqtt.connect()
     mqtt.subscribe()
     mqtt.publish_message()
     mqtt.disconnect()
     ```

Result were OK! 
> I've realized that responses were slightly faster than usual connection that modems own connection by own with wi-fi. Cellular connection over ECM printed out responses in a minute with included time delay both HTTP and MQTT.


