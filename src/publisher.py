
import os
import string
from secretfile import topic
from secretfile import server

print("publisher.py Copyright (C) 2023  Sam Warr")
print("This program comes with ABSOLUTELY NO WARRANTY")
print("This is free software, and you are welcome to redistribute it")
print("under certain conditions")
print()

# The topic of the MQTT server to publish on
print("Publishing on topic [" + topic + "]")
while True:
# Prompt the user for a message
    message = input("Message: ")
# Define the bash command
    command = "mosquitto_pub -h " + server + " -t \"" + topic + "\" -m \"" + message + "\""
# Execute the command
    os.system(command)
