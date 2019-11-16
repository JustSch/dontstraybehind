from twilio.rest import Client
from flask import Flask, request, redirect
import twilio.twiml
from twilio.twiml.messaging_response import Message, MessagingResponse
import os
import requests
import json

app = Flask(__name__)


client = Client(os.environ['SID'], os.environ['AUTH'])





@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    resolving = request.form['Body']

    response = maps(resolving)

    message = client.messages.create(to=number,
                                     from_=***REMOVED***,
                                     body=response)
    return 'this'


def maps(resolving):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?input={}&inputtype=textquery&fields=formatted_address,name,opening_hours&key=***REMOVED***"

    response = " "
    if "found" in resolving:
        response = 'Animal Shelters in NYC'
    if "Found" in resolving:
        response = 'Animal Shelters in NYC'
    if "injured" in resolving:
        response = 'Animal Hospitals in NYC'
    if "Injured" in resolving:
        response = 'Animal Hospitals in NYC'

    #response = resolve

    url_request = url.format(response)
    r = requests.get(url_request)

    results_object = r.json()['results']

    result_list = []

    for i in range(0, 5):
        result_list.append((results_object[i]['name']))
        result_list.append(' ')
        result_list.append(results_object[i]['formatted_address'])
        result_list.append(' ')
    result_list = ' '.join(map(str, result_list))

    print(result_list)
    return result_list


if __name__ == '__main__':
    app.run()
