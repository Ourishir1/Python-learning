from twilio.rest import Client

TWILIO_SID = "AC6cfd6dd68cf837a8718c837471652a68"
TWILIO_AUTH_TOKEN = "3959e6a724d5ee96650244c207a19d46"
TWILIO_VIRTUAL_NUMBER = '+15076195218'
TWILIO_VERIFIED_NUMBER = '+972509988726'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
