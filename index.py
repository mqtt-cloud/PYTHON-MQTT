import paho.mqtt.client as paho
def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))

client = paho.Client(client_id="Python_TEST", clean_session=True, userdata=None, protocol=paho.MQTTv31)
client.on_connect = on_connect
client.username_pw_set("test","123")
client.connect("127.0.0.1", 15542)
client.loop_forever()

