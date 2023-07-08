from twilio.rest import Client
import os

os.environ['twilio_sid'] = 'AC05f0ea84be4dd923f1a3cdc81d27a531'
os.environ['twilio_aut_token'] = '198642796b54075617d5a75a91492ffe'

account_sid = os.environ['twilio_sid']
auth_token = os.environ['twilio_aut_token']
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass

    def send_notification(self, msg: str = ''):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+18145262067',
            body=msg,
            to='+48737365338'
        )
