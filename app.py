from flask import Flask, request

app = Flask(__name__)

led_state = {"status": "off"}  # default

@app.route("/sms", methods=["POST"])
def sms_webhook():
    incoming_msg = request.values.get('Body', '').strip().lower()
    if "on" in incoming_msg:
        led_state["status"] = "on"
        return "Turning ON", 200
    elif "off" in incoming_msg:
        led_state["status"] = "off"
        return "Turning OFF", 200
    else:
        return "Invalid command", 200

@app.route("/led-status", methods=["GET"])
def get_led_status():
    return led_state["status"], 200
