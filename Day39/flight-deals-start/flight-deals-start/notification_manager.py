from twilio.rest import Client
import os

os.environ['twilio_sid'] = 'AC05f0ea84be4dd923f1a3cdc81d27a531'
os.environ['twilio_aut_token'] = '40924077eb00c507f54a6047be844f1c'


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_notification(self, msg: str = ''):
        account_sid = os.environ['twilio_sid']
        auth_token = os.environ['twilio_aut_token']
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+18145262067',
            body=msg,
            to='+48737365338'
        )

        print(message.sid)
