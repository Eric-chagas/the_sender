# Importing libraries and twilio-python important stuff
import os
from twilio.rest import Client

# Setting up twilio account stuff located in very secret, obviously .gitIgnored .env config file
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Finally creating client connection
client = Client(account_sid, auth_token)

# Write your bullshit message bellow

message = client.messages.create(
    body="Hi! My name is Eric, i'm a CNU nerd! Come join my nerdy bullshit at CNU, virginia!",
    from_=os.environ['SENDER_PHONE_NUMBER'],
    to=os.environ['RECEIVER_PHONE_NUMBER_BR']
)

# Regular python debug stuff
print(message.sid)