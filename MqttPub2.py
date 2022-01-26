import ssl
import sys

import paho.mqtt.client

client = paho.mqtt.client.Client('tostadora-pub')
client.connect ("127.0.0.1", 1883, 60)
topic = "casa/cocina/tostadora"
client.publish(topic, "temp:35")
