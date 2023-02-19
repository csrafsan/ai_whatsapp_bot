from django.conf import settings
import requests

def sendWhatsAppMessage(phoneNumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {"messaging_product": "whatsapp",
               "recipient_type": "individual",
               "to": phoneNumber,
               "type": "text",
               "text": {"body": message}

                }
    
    response = requests.post(settings.WHATSAPP_URL, headers = headers, json = payload)
    ans = response.json()
    return ans

    # phoneNumber = "8801739158770"
    # message = "Hello there, \n This is our first Django Whatsapp Message, glad to have you here!"

    # ans = sendWhatsAppMessage(phoneNumber, message)
