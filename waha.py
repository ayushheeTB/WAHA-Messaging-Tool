import requests
import json
from datetime import datetime
import time
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://localhost:3000/api/sendText"
SESSION = "true_b"


numbers = ["91234567890"]


MESSAGE = """Vigilance: Our Shared Responsibility\n
Join us in promoting integrity and transparency by observing Vigilance Awareness Week 2025. Let’s work together towards building a corruption-free India.\n
Take the e-pledge today: https://pledge.mygov.in/cvc\n"""

results = []

API_KEY=os.getenv("WAHA_API_KEY")
headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}


for num in numbers:
    payload = {
        "session": SESSION,
        "chatId": f"{num}@c.us",
        "text": MESSAGE
    }

    try:
        response = requests.post(BASE_URL, json=payload, headers=headers)
        data = response.json()

        print("⏳ Waiting 5 seconds for delivery...")
        time.sleep(5)

        status = "success" if 200 <= response.status_code < 300 else "failed"
        ack_map = {0: "sent", 1: "delivered", 2: "read", 3: "played"}
        ack_status = ack_map.get(data.get("ack", 0), "unknown")

        results.append({
            "number": num,
            "status": status,
            "ack_status": ack_status,
            "response": data,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        print(f"Message to {num}: {status}")

    except Exception as e:
        results.append({
            "number": num,
            "status": "error",
            "response": str(e),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Error sending to {num}: {e}")

with open("delivery_status.json", "w") as f:
    json.dump(results, f, indent=4)

print("\nDelivery status saved to 'delivery_status.json'")
