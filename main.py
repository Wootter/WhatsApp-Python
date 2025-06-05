"""
Name: WhatsApp Python
Author: Wootter
Date: 6th of June 2025
Github repo: https://github.com/Wootter/WhatsApp-Python
Funtion: A python communications method for WhatsApp
How to use:
"""

from twilio.rest import Client

client = Client()

from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio sandbox number
to_whatsapp_number = 'whatsapp:' + os.environ['TO_WHATSAPP_NUMBER']  # Your WhatsApp number

client.messages.create(body='Hello World!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)