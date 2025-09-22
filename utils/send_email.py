import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from pydantic import EmailStr
import os

load_dotenv()

def send_notification_email(receiver_email:EmailStr,name:str,password:str):
    sender_email=os.getenv("EMAIL_ID")
    sender_password=os.getenv("APP_PASSWORD")

    subject = "Welcome to our APP"
    body=f"""
        Hello,{name}
        Your Account has been created Succesfully,
        Email ID : {receiver_email}
        Temporary Password : {password}
        Please Change the Password After Login.

"""
    msg=MIMEText(body)
    msg['Subject']=subject
    msg['From']=sender_email
    msg['To']=receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        print("hello")
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,receiver_email,msg.as_string())

    print(f"notification send on {receiver_email}.")


def send_otp_email(receiver_email:EmailStr,otp:int):
   
    sender_email=os.getenv("EMAIL_ID")
    sender_password=os.getenv("APP_PASSWORD")

    subject="Your Reset Password OTP"
    body=f"""
    {otp} is the OTP for reset the Password 
"""
    msg=MIMEText(body)
    msg["Subject"]=subject
    msg["From"]=sender_email
    msg["To"]=receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,receiver_email,msg.as_string())


def send_notify_email(receiver_email:EmailStr):
   
    sender_email=os.getenv("EMAIL_ID")
    sender_password=os.getenv("APP_PASSWORD")

    subject="You Have A new Message"
    body=f"""
   you have a new message
"""
    msg=MIMEText(body)
    msg["Subject"]=subject
    msg["From"]=sender_email
    msg["To"]=receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
    


