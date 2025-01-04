from logging import exception
from twilio.rest import Client
from datetime import datetime,timedelta
import time

account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"#enter your twilio account sid
auth_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxx" #enter account token

client = Client(account_sid,auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_="whatsapp: +12313071785",
            body=message_body,
            to = f'whatsapp:{recipient_number}'
        )
        print(f'message send successfully {message.sid}')
    except exception as e:
        print("an error occurred")
name = input("what is your name : ")
recipient_number = input("enter your friend number with country code : ")
message_body = input(f"what message do you want to send to {name}")

date_str = input("enter date which date to send (yyyy-mm-dd) : ")
time_str = input("which time you want to send(HH:MM) : ")

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds<=0:
    print("the time is gone please enter upcoming time ")
else:
    print(f"message scheduled to send to {name} at {schedule_datetime}. ")
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number,message_body)
