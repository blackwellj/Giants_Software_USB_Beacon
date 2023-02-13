import paho.mqtt.client as mqtt
import giants_beacon

def on_message(client, userdata, msg):
    giants_beacon.GiantsBeacon().device_state(msg.payload.decode())

mqtt.Client().connect("10.1.1.2", 1883, 60).subscribe("beacon", on_message).loop_forever()
