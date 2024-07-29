import smtplib
# from twilio.rest import Client

def send_notification(user, flight):
    message = f"Flight {flight.flight_id} status changed to {flight.status}"
    send_email(user.email, message)
    # send_sms(user.phone, message)

def send_email(to_email, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    server.sendmail("your_email@gmail.com", to_email, message)
    server.quit()

def send_sms(to_phone, message):
    client = Client("TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN")
    client.messages.create(
        to=to_phone,
        from_="your_twilio_number",
        body=message
    )
