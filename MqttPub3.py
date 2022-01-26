import ssl
import sys

import paho.mqtt.publish as publish

broker_address = "localhost"
topic = "casa/cocina/horno"
mensaje1 = "Time: 15 minutos desde que encendio el horno"
mensaje2 = "Deberia revisar su alimento"
mensaje3 = "Ya casi va a estar"

msgs = [{'topic': topic, 'payload': mensaje1},
(topic, mensaje2, 0, False),
(topic, mensaje3, 0, False)]

publish.multiple(msgs, hostname=broker_address)
