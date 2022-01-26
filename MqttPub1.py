import ssl
import sys

import paho.mqtt.client

client = paho.mqtt.client.Client('nevera-pub')
client.connect ("127.0.0.1", 1883, 60)
topic = "casa/cocina/nevera"
client.publish(topic, "temp: 15")
