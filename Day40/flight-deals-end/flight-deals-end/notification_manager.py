from twilio.rest import Client
import smtplib

TWILIO_SID = 'AC05f0ea84be4dd923f1a3cdc81d27a531'
TWILIO_AUTH_TOKEN = 'e7483b05f217dfed2fd8255f64030b16'
TWILIO_VIRTUAL_NUMBER = '+18145262067'
TWILIO_VERIFIED_NUMBER = '+48737365338'

email = 'mlodybartus@gmail.com'
password = 'tkelpunbstudhbgo'

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, message):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(email, email, message)
            connection.quit()




