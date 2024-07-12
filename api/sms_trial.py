import africastalking
import os

# Initialize SDK
username = os.environ.get('AT_USERNAME')    # use 'sandbox' for development in the test environment
api_key = os.environ.get('AT_API_KEY')      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

#Initialize sms service
sms = africastalking.SMS

#Function for sending sms alert
def send_sms_alert(phone_number, message):
    try:
        sender = os.environ.get('AT_SENDER')
        response = sms.send(message, [phone_number], sender)
    except Exception as e:
        print("Error sending message")

message = f"Order received: Pens amounting to: 350 at 2024-06-21 15:00."
phone_number = "+2547xxxxxxxx"
send_sms_alert(phone_number, message)