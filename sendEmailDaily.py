'''
Send Single Email
Randal McKee
'''
from pathlib import Path
import os
import yagmail
import time
from datetime import datetime as dt


sender = os.getenv('email')
sender_psw = os.getenv('password')
receiver = 'randal.j.mckee@gmail.com'

#print(sender, sender_psw)

subject = 'This is the subject'

contents = """
Here is the content of the email!
Hi!
"""

while True:
    #variable now  will store the current datetime
    now = dt.now()
    #if statement to check current datetime and if the hour and minute are equal to 13:15 send email
    if now.hour == 15 and now.minute == 10:
        yag = yagmail.SMTP(user=sender, password=sender_psw)
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email Sent!")
        time.sleep(60)