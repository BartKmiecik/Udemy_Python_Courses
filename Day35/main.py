#e5be7c520ea23c4aed6b77014739f2ca
#AC05f0ea84be4dd923f1a3cdc81d27a531
#+18145262067

import os
from twilio.rest import Client

account_sid = 'AC05f0ea84be4dd923f1a3cdc81d27a531'
auth_token = 'e5be7c520ea23c4aed6b77014739f2ca'
client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='+18145262067',
#   body='Test',
#   to='+48737365338'
# )
#
# print(message.sid)


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

# sid = 'AC05f0ea84be4dd923f1a3cdc81d27a531'
# token = 'e5be7c520ea23c4aed6b77014739f2ca'
#
# account_sid = os.environ[sid]
# auth_token = os.environ[token]
# client = Client(account_sid, auth_token)
#
message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18145262067',
                     to='+48737365338'
                 )

print(message.sid)