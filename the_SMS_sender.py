# Importing libraries and twilio-python important stuff
import os
from dotenv import load_dotenv
from twilio.rest import Client


# Loading .env file 
load_dotenv()

# Setting up twilio account stuff located in very secret, obviously .gitIgnored .env config file
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# Finally creating client connection
client = Client(account_sid, auth_token)

# Write your bullshit message bellow

message = client.messages.create(
    body="Hi! My name is Eric, i'm a CNU nerd! Come join my nerdy troop at mojo dojo casa house, CNU, Virginia!",
    from_=os.getenv("SENDER_PHONE_NUMBER"),
    to=os.getenv("RECEIVER_PHONE_NUMBER_US")
)

# Regular python debug stuff
print(message.sid)