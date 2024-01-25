from base import Connection 

class HTTP:
    con = Connection()
    
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
        self.con.at_command("AT+QHTTPCFG=\"requestheader\",\"{}\"".format(request_header), 'AT+QHTTPCFG=requestheader')
        sslctxID = input("sslctxID: ")
        self.con.at_command("AT+QHTTPCFG=\"sslctxid\",\"{}\"".format(sslctxID), 'AT+QHTTPCFG=sslctxid')
        content_type = input("content_type: ")
        self.con.at_command("AT+QHTTPCFG=\"contenttype\",\"{}\"".format(content_type), 'AT+QHTTPCFG=contenttype')
        auto_outrsp = input("auto_outrsp: ")
        self.con.at_command("AT+QHTTPCFG=\"rspout/auto\",\"{}\"".format(auto_outrsp), 'AT+QHTTPCFG=rspout/auto')
        closedind = input("closedind: ")
        self.con.at_command("AT+QHTTPCFG=\"closed/ind\",\"{}\"".format(closedind), 'AT+QHTTPCFG=closed/ind')
        window_size = input("window_size: ")
        self.con.at_command("AT+QHTTPCFG=\"windowsize\",\"{}\"".format(window_size), 'AT+QHTTPCFG=windowsize')
        close_wait_time = input("close_wait_time: ")
        self.con.at_command("AT+QHTTPCFG=\"closewaittime\",\"{}\"".format(close_wait_time), 'AT+QHTTPCFG=closewaittime')
        username = input("username: ")
        password = input("password: ")
        self.con.at_command("AT+QHTTPCFG=\"auth\",\"%s\":\"%s\"".format(username, password), 'AT+QHTTPCFG=auth')
        custom_value = input("custom_value: ")
        self.con.at_command("AT+QHTTPCFG=\"custom_header\",\"{}\"".format(custom_value), 'AT+QHTTPCFG=custom_header')
        
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

    def http_stop(self):
        self.con.at_command(HTTP_AT['cancel'], 'Cancel')
        
    def close_connection(self):
        self.con.at_command(HTTP_AT['end'], 'End the connection')
