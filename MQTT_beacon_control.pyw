import paho.mqtt.client as mqtt
import giants_beacon

beacon = giants_beacon.GiantsBeacon()

def on_message(client, userdata, msg):
    beacon.device_state(msg.payload.decode())

client = mqtt.Client()
client.connect("10.1.1.2", 1883, 60)
client.on_message = on_message
client.subscribe("beacon")
client.loop_forever()
