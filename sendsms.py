
from twilio.rest import Client
import keys
client=Client(keys.acc_sid,keys.auth_token)
message=client.messages.create(
    body="Hey,It's time to take your medicine",
    from_=keys.twilio_no,
    to=keys.phone_no

)
print(message.body)
