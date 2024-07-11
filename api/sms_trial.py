import africastalking

# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "atsk_ed34c399ef839b5af0ead66cb52cba3e6e5e89dda614ceec9933969d3ff99c8db10aa46c"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

#Initialize sms service
sms = africastalking.SMS

#Function for sending sms alert
def send_sms_alert(phone_number, message):
    try:
        sender = "1739"
        response = sms.send(message, [phone_number], sender)
    except Exception as e:
        print("Error sending message")

message = f"Order received: Pens amounting to: 350 at 2024-06-21 15:00."
phone_number = "+254798889503"
send_sms_alert(phone_number, message)