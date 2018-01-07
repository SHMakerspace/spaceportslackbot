Spaceport Slackbot
============
This python script is an application to companion [Spaceport](https://github.com/SHMakerspace/spaceport) . Once configured the script will listen on the Spaceport MQTT and create slack notifications in a channel of your choice when Spaceport posts notifications to MQTT.

Configuration
-----------
Install the required package dependancies contained within **requirements.txt**, the suggested method being with pip:
```
# pip install -r requirements.txt
```
Register an application with slack [here](https://api.slack.com/apps?new_app=1) and record the client secret.
Update the user configuration values in spaceportslackbot.py :
- SLACKBOT_TOKEN = The client secret from slack application registration
- SLACK_CHANNEL = The channel you would like slackbot to run in
- BROKER_ADDRESS = The IP address (or FQDN) of the MQTT server Spaceport is pushing messages to (often localhost)
- TOPIC = The MQTT topic Spaceport messages are pushed to.

Once the above items are configured spaceportslackbot.py is ready to be run, it can be run by simply calling `python spaceportslackbot.py`, but it is more robust to be run as a monitored service. 

Below is a systemd unit file for running the slack bot. It relies on the script being in the directory **/usr/bin/spaceportslackbot/**  and a user named *spaceport* existing on the system with execute permissions on the file **/usr/bin/spaceportslackbot/spaceportslackbot.py**
```
[Unit]
Description=Spaceport Slackbot
After=network.target

[Service]
User=spaceport
Group=spaceport
WorkingDirectory=/usr/bin/spaceportslackbot/
ExecStart=/bin/python /usr/bin/spaceportslackbot/spaceportslackbot.py

Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
```

More information on Spaceport can be found in the [Spaceport repo](https://github.com/SHMakerspace/spaceport).
