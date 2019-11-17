from twilio.rest import Client
from flask import Flask, request, redirect
import twilio.twiml
from twilio.twiml.messaging_response import Message, MessagingResponse
import os
import requests


app = Flask(__name__)


client = Client(os.environ['SID'], os.environ['AUTH'])

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    resolving = request.form['Body']

    response = maps(resolving)

    message = client.messages.create(to=number,
                                     from_=os.environ['TWILIO_NUM'],
                                     body=response)

    return 'this'


def maps(resolving):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?input={}&inputtype=textquery&fields=formatted_address,name,opening_hours&key={}"

    response = " "
    if "found" in resolving:
        response = 'Animal Shelters in NYC'

    if "injured" in resolving:
        response = 'Animal Hospitals in NYC'

    if "shelter" in resolving:
        response = 'Animal Shelters in NYC'

    if "Shelter" in resolving:
        response = 'Animal Shelters in NYC'

    if "stray" in resolving:
        response = 'Animal Shelters in NYC'

    if "Stray" in resolving:
        response = 'Animal Shelters in NYC'




    #response = resolve

    url_request = url.format(response,os.environ['MAPS_KEY'])
    r = requests.get(url_request)

    results_object = r.json()['results']

    result_list = []
    result_list.append("\n")
    result_list.append("Here are some nearby shelters and animal hospitals")
    result_list.append("\n")


    for i in range(0, 5):
        result_list.append((results_object[i]['name']))
        result_list.append('\n')
        result_list.append(results_object[i]['formatted_address'])
        result_list.append('\n')
    result_list.append("To help these stray animals if you can't find immediate care go here : https://www.humanesociety.org/resources/how-help-stray-pet")
    result_list = ' '.join(map(str, result_list))

    print(result_list)
    return result_list


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
