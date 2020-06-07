from email.message import EmailMessage
import json
import re
import smtplib


def load_json(file_name):
    """Load a json file from the root in to an object"""
    try:
        with open(file_name) as content:
            return json.load(content)
    except Exception:
        print(Exception)
        return {}


def send_text(message):
    """Email the event as a text message"""
    config = load_json('config.json')
    sms_codes = config['sms_codes']

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = 'To Do'
    msg['From'] = config['gmail_login']

    for notify in config['send_alerts_to']:
        phone_number = re.sub("[^0-9]", "", notify['phone_number'])
        
        msg['To'] = phone_number + "@" \
            + sms_codes[notify['wireless_carrier']]

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(config['gmail_login'], config['gmail_pwd'])
            server.send_message(msg)
            server.quit()
        except Exception:
            print(Exception)
        else:
            print('Message sent to ' + msg['To'])
            print(message)
