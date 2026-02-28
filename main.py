"""
Name: WhatsApp Python
Author: Wootter
Date: 6th of June 2025
Github repo: https://github.com/Wootter/WhatsApp-Python
Funtion: A python communications method for WhatsApp
How to use:
"""

import requests
def sendWSP(message, apikey,gid=0):
    url = "https://whin2.p.rapidapi.com/send"
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": apikey,
	"X-RapidAPI-Host": "whin2.p.rapidapi.com"}
    try:
        if gid==0:
            return requests.request("POST", url, json=message, headers=headers)
        else: 
            url = "https://whin2.p.rapidapi.com/send2group"
            querystring = {"gid":gid}
            return requests.request("POST", url, json=message, headers=headers, params=querystring) 
    except requests.ConnectionError:
        return("Error: Connection Error")

# Testing Section
msg1 = {"text":"hello there"}
# msg2 = {"text":"this is a group message"}

myapikey = "9f7be6e2bcmsh907c7a526a8a525p18049ejsn7e87b9796299"
# mygroup = "your_wsp_group_id"

sendWSP(msg1,myapikey)
# sendWSP(msg2, myapikey,mygroup)