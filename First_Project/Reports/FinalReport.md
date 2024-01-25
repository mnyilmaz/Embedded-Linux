## Final Report
On the final week my responsibilities were:
-   MQTT controls
-   HTTP controls
-   QMI, ECM and PPP comparison
-   Additional feature implementation
-   Final report

and all these are studied well. Report related to these titles can be found below.
- [ECM Installation](https://docs.sixfab.com/page/cellular-internet-connection-in-ecm-mode)
- [QMI Installation](https://docs.sixfab.com/page/setting-up-a-data-connection-over-qmi-interface-using-libqmi)
- [QMI Mode](https://forum.openwrt.org/t/quectel-ec25-4g-modem-qmi-mode/70092)
- [Timeout](https://community.sixfab.com/t/err-timeout-couldnt-get-response-on-telit-le910c4-eu/2121/2)
- [AT+CSQ](https://m2msupport.net/m2msupport/atcsq-signal-quality/)

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

## HTTP Results without Protocols
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

## MQTT Results without Protocols
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

## ECM (Ethernet Control Modem) Installation and Tests
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

To continue with QMI
     ```
     AT+QCFG="usbnet",0
     AT+QCFG="usbnet"   # Should return +QCFG: "usbnet",0
     AT+CFUN=1,1
     ```


## QMI (Qualcomm MSM Interface) Installation and Tests
QMI, or Qualcomm MSM Interface, is a protocol developed by Qualcomm for communication with modems embedded in mobile devices. QMI is commonly used in cellular modems and modules to facilitate communication between the host processor (like an application processor in a smartphone or an embedded system) and the cellular modem.

Following commands had been applied to get ECM connection.
  1. List USB
     ```
     lsusb -t
     ```
  > Return: Port 3: Dev 7, If 4, Class=Vendor Specific Class, Driver=qmi_wwan, 480M

  2. Check usbnet
     ```
     AT+QCFG="usbnet"  # Should return 0 if not set to zero and rebbot the module
     ```
  3. Install packages
     ```
     sudo apt update && sudo apt install libqmi-utils udhcpc
     ```
  4. Check if the module is ready
     ```
     sudo qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode  # or -dms-get-operating-mode='online'
     ```
  > [/dev/cdc-wdm0] Operating mode retrieved:
  >     Mode: 'online'
  >     HW restricted: 'no'

  5. Set wwan0 down to enable QMI and configure network interface
     ```
     sudo ip link set wwan0 down
     ```
     ```
     echo 'Y' | sudo tee /sys/class/net/wwan0/qmi/raw_ip
     ```
     ```
     sudo ip link set wwan0 up
     ```
  6. Confirm data format
     ```
     sudo qmicli -d /dev/cdc-wdm0 --wda-get-data-format
     ```
  7. Connect mobile network
     ```
     sudo qmicli -p -d /dev/cdc-wdm0 --device-open-net='net-raw-ip|net-no-qos-header' --wds-start-network="apn='super',ip-type=4" --client-no-release-cid
     ```
  8. Configure IP address
     ```
     sudo udhcpc -q -f -i wwan0
     ```
  9. Check connection
     ```
     ifconfig wwan0
     ping -I wwan0 google.com -c 5
     AT+QCFG="usbnet" # Returns 0
     ```
After connection is set over the QMI protocol re-run the HTTP and MQTT class functions. If you close the Pi follow the steps above again.
Result were OK! 
> HTTP 20 GET and POST request were requested with reduced sleep times. Result: 20/20
> MQTT 20 Publish and Subscribe were requested. In normally there were no reduce time. Result: 20/20
> Responses were fair faster than ECM and network. Even sending more than one request did not effect the performance of the data transmission over cellular network.

## PPP (Point to Point Protocol) Installation and Tests
PPP, is a data link layer protocol commonly used to establish a direct connection between two networking nodes. It is widely used in connecting a computer (or a network of computers) to the Internet via a dial-up connection or as part of a Virtual Private Network (VPN). PPP is commonly used for establishing connections over serial links, such as traditional phone lines. It has been widely utilized for Internet connections, especially in the era of dial-up access. However, with the prevalence of broadband technologies like DSL and cable modems, PPP is less commonly used for Internet connectivity today.

Earlier weeks PPP installation steps were given and has been made successfully. At this week after QMI I've re-installed PPP protocol and re-run the HTTP and MQTT class functions.
Result were OK! 
> According to ECM and QMI, PPP were slower than these two. Yet it is an old protocol, may effect its compability with modem.

## Final Results of ECM-QMI-PPP Comparison
PPP provided obviously slower connection according to the ECM and QMI. Less efficient in terms of speed compared to other modern protocols, especially when used over traditional dial-up connections. 

ECM and QMI were nip and tuck at this point. Because their speed and cabaility depends on features they have. For example 4G affects QMI in a positive manner while USB2 drags down the ECM. For this applicaiton both in HTTP and MQTT within a minute (included sleep times) all the processes hav been written were accomplished.

## Final Week Configurations
As all the tasks accomplished, on my final week input variables, HTTP, MQTT and Base classes have been seperated from modem_lib.py file as:
    1. base.py
    2. http-lib.py
    3. mqtt-lib.py
    4. main.py
    5. inputs.py

#### base.py
```
def check_base(self)
def define_PDP_context(self)
def reboot_options(self)
```
BASE dictionary had been removed in order to optimize the code. 

#### http-lib.py
```
class HTTP:
    def config(self)
    def set_PDP(self)
    def connect(self)
    def http_get(self)
    def http_post(self)
    def destroyer_of_http(self)
```
HTTP dictionary had been removed in order to optimize the code. After get and post processes PDP context deactivated related to documentation.

#### mqtt-lib.py
```
class MQTT:
    def connect(self)
    def subscribe(self)
    def publish(self)
```
MQTT dictionary had been removed in order to optimize the code. After subscribe process unsubscribed from the topic and closed the net. Same steps had been followed at publish process.

#### main.py
```
def control_base(self)
def http_get(self)
def http_post(self)
def.mqtt_sub(self)
def.mqtt_pub(self)
```
All processes had been organized as in documentations. Only require the call from the main.
I've also added User Guidline to run the project properly.

## Final Review of the Project
Througout 6 weeks of project timeline scope, I have learned basics about cellular connection and communication. Step by step; HTTP and MQTT protocols reviewed and tested, AT commands were tested and documentations have been read, related to that knowledge a library based on Python programming language has been formed, tests over PPP, QMI and ECM has been accomplished. All these theoretical and practical applications bringed in a different view on communication approach. My earlier applications were related on basic requests via Python requests library, yet with AT commands and over modem communicaiton imporved better my problem solving techniques and approaches. While establishing protocols and connections lots of errors have been encountered. Getting help from each other, shuffling forum pages. Eventually, with up's and down's project completed within the scope of desired outcomes.
