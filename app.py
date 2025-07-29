from flask import Flask, request
import requests

app = Flask(__name__)

ESP_IP = "http://12:39:50.452"  # Your ESP8266 IP address

@app.route("/sms", methods=["POST"])
def sms_webhook():
    incoming_msg = request.values.get('Body', '')
    msg = incoming_msg.strip().lower()
    print("📲 WhatsApp Message Received:", msg)

    try:
        if 'oled on' in msg:
            requests.get(f"{ESP_IP}/on")
            print("✅ LED ON triggered")
            return "LED turned ON", 200
        elif 'oled off' in msg:
            requests.get(f"{ESP_IP}/off")
            print("✅ LED OFF triggered")
            return "LED turned OFF", 200
        else:
            print("⚠️ Invalid command")
            return "Invalid command", 200
    except Exception as e:
        print("❌ Error:", e)
        return "ESP8266 not reachable", 500

if __name__ == "__main__":
    app.run(port=5000)
