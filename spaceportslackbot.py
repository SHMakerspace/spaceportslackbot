#!/bin/python
import paho.mqtt.client as mqtt
import json
from slackclient import SlackClient

## ---- User configuration ---- ##
SLACKBOT_TOKEN = ""
SLACK_CHANNEL = ""
BROKER_ADDRESS = ""
TOPIC = ""
## ---- END User configuration ---- ##


def SlackMessage(message):
	        slack_client.api_call("chat.postMessage",channel=SLACK_CHANNEL,text=message)

def constructmessage(data):
	if data["Misc"] == "Naughty":
		message = ":rage: %s has been auto logged out, naughty naughty!!" % data["user"]
	elif data["SiteStatus"] == "Open":
		message = "SHM is open :grinning: %s has entered via %s" % (data["user"], data["Node"] )
	elif data["SiteStatus"] == "Closed":
		message = "SHM is closed :cry: %s has left via %s" % (data["user"], data["Node"] )
	else:
		message = "%s has %sed via %s" % (data["user"], data["Direction"], data["Node"] )
	return message

def on_message(client, userdata, message):
	data= json.loads(str(message.payload.decode("utf-8")))
	SlackMessage(constructmessage(data))

if __name__ == "__main__":

	slack_client = SlackClient(SLACKBOT_TOKEN)
	starterbot_id = None
	if slack_client.rtm_connect(with_team_state=False):
		starterbot_id = slack_client.api_call("auth.test")["user_id"]

	client = mqtt.Client("slackbot")
	client.connect(BROKER_ADDRESS)
	client.subscribe(TOPIC)
	client.on_message=on_message
	client.loop_forever()
