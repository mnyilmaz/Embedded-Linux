from base import Connection 

class HTTP:
    con = Connection()

    def __init__(self, apn, url, get_size, read_size, post_size, latency):
        self.apn = apn
        self.url = url
        self.get_size = get_size
        self.read_size = read_size
        self.post_size = post_size
        self.latency = latency

    # HTTP settings
    def config(self):
        self.con.at_command('AT+QHTTPCFG="contextid",1', 'Context ID Configuration')
        self.con.at_command('AT+QHTTPCFG="responseheader",1', 'Response Header Configuration')        
        answer = input("Would you like to configure more settings? (Y/N): ")
        if answer.upper() == 'Y':
            self.QHTTPCFG_settings()
        else:
            self.con.at_command('AT+QHTTPCFG?', 'HTTP Settings')

    def QHTTPCFG_settings(self):
        request_header = input("request_header: ")
        self.con.at_command(f'AT+QHTTPCFG="requestheader","{request_header}"', 'AT+QHTTPCFG=requestheader')
        sslctxID = input("sslctxID: ")
        self.con.at_command(f'AT+QHTTPCFG="sslctxID","{sslctxID}"', 'AT+QHTTPCFG=sslctxID')
        content_type = input("content_type: ")
        self.con.at_command(f'AT+QHTTPCFG="contenttype","{content_type}"', 'AT+QHTTPCFG=contenttype')
        auto_outrsp = input("auto_outrsp: ")
        self.con.at_command(f'AT+QHTTPCFG="rspout/auto","{auto_outrsp}"', 'AT+QHTTPCFG=rspout/auto')
        closedind = input("closedind: ")
        self.con.at_command(f'AT+QHTTPCFG="closed/ind","{closedind}"', 'AT+QHTTPCFG=closed/ind')
        window_size = input("window_size: ")
        self.con.at_command(f'AT+QHTTPCFG="windowsize","{window_size}"', 'AT+QHTTPCFG=windowsize')
        close_wait_time = input("close_wait_time: ")
        self.con.at_command(f'AT+QHTTPCFG="closewaittime","{close_wait_time}"', 'AT+QHTTPCFG=closewaittime')
        username = input("username: ")
        password = input("password: ")
        self.con.at_command(f'AT+QHTTPCFG="auth","{username}":"{password}"', 'AT+QHTTPCFG=auth')
        custom_header = input("custom_header: ")
        self.con.at_command(f'AT+QHTTPCFG="custom_header","{custom_header}"', 'AT+QHTTPCFG=custom_header')
        
    def set_PDP(self):
        self.con.at_command(f'AT+QICSGP=1,1,"{self.apn}","","",1', 'Set APN')
        self.con.at_command('AT+QIACT?', 'Querry PDP Context')
        self.con.at_command('AT+QIACT=1', 'Activate PDP Context')
        self.con.at_command('AT+QIDEACT=1', 'Deactivate PDP Context')

    def connect(self):
        self.con.at_command(f'AT+QHTTPURL={len(self.url)},80', 'Set URL pre-settings')
        time.sleep(10)
        self.con.at_command(self.url, 'Set URL')
        time.sleep(5)
        self.con.at_command('AT+QHTTPURL?', 'Check URL status')
        
    def http_get(self):
        time.sleep(20)
        self.con.at_command(f'AT+QHTTPGET="{self.get_size}"', 'HTTP GET Request')
        time.sleep(20)
        self.con.at_command(f'AT+QHTTPREAD="{self.read_size}"', 'Read HTTP Response')
        
    def http_post(self):
        self.con.at_command(f'AT+QHTTPPOST="{self.post_size}","{self.latency}"', 'HTTP POST Request')
        message = input("Enter your message to the HTTP: ")
        self.con.at_command(message, 'Message')
        
    def destroyer_of_http(self):
        self.con.at_command('AT+QHTTPSTOP', 'Cancel')
        self.con.at_command('AT+QICLOSE=1', 'End the connection')
