#!/usr/bin/python3

import subprocess, smtplib

def is_host_reachable(host):
    try:
        output = subprocess.check_output(["ping", "-c", "1", host])
        return True
    except subprocess.CalledProcessError:
        return False

# CONFIG
host = "abc.xyz"
port = 587
smtp_server = "smtp.gmail.com"
sender_email = "abc.xyz@lost.com"
receiver_email = "someron_bakuli@lost.com"
password = "change_me"

if not is_host_reachable(host):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, f"The host {host} could not be reached via ping.")
else:
    print(f"{host} is reachable.")
