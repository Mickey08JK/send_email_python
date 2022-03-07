'''
Send Single Email
Randal McKee
'''
from pathlib import Path
import os
import yagmail
import time


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
    yag = yagmail.SMTP(user=sender, password=sender_psw)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)