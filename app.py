from twilio.rest import Client
from flask import Flask, request, redirect
import twilio.twiml
from twilio.twiml.messaging_response import Message, MessagingResponse
import os


app = Flask(__name__)


client = Client(***REMOVED***, ***REMOVED***)



@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']

    message = client.messages.create(to=number,
                                                  from_=***REMOVED***,
                                                  body="It works now!!")
    return 'this'


if __name__ == '__main__':
    app.run()
