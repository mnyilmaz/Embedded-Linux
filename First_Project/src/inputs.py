    # Main configurations
    baudrate = 115200
    port = 'dev/ttyUSB3'
    byte = 1024
    apn = 'super'
    modem = serial.Serial(port, baudrate, timeout=5)

    # HTTP
    url = 'https://webhook.site/'
    get_size = 80
    read_size = 80
    post_size = 20
    latency = 50
    
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
