from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)

TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_NUMBER = "whatsapp:+14155238886"  # Twilio sandbox or approved number
TO_NUMBER = "whatsapp:+919025447741"     # Your WhatsApp number

client = Client(TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_SID)

@app.route("/notify", methods=["POST"])
def send_whatsapp():
    message = request.form.get("message", "Alert from ESP8266")
    client.messages.create(
        body=message,
        from_=TWILIO_NUMBER,
        to=TO_NUMBER
    )
    return "Message sent!", 200
