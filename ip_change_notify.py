#!/usr/bin/python3

import requests, datetime, smtplib, ssl

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "change.me@offline.com"
receiver_email = "someron_bakuli@world.com"
password = "change_me"

result = requests.get('http://api.ipify.org/')
message  = result.text
old_ip = ""

try:
        with open("my_ip.txt","r") as file:
                old_ip = file.read()
except:

        with open("my_ip.txt","w+") as file:
                old_ip = file.read()

if message!=old_ip:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

        with open("my_ip.txt","w") as file:
                file.write(message)
        print(datetime.datetime.now(),"Ip is Changed",message)
