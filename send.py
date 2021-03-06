import bottle
from bottle import hook, response
import cgi
import re
import mandrill
import os

mandrill_client = mandrill.Mandrill('a0ofkf1HNIwYt2P0CZ-CYQ')

@hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'

@bottle.post('/')
def send_mail():
	destination = 'jgwil2@gmail.com'
	name = bottle.request.forms.get('name')
	email = bottle.request.forms.get('email')
	message = bottle.request.forms.get('message')

	form = {
				'to': [{'email': destination}],
				'from_email': email,
				'subject': 'Message from ' + name,
				'text': message
			}

	result = mandrill_client.messages.send(message=form)
	if result[0]['status'] != 'sent':
		abort(500)

	return {'message': 'Thank you! Your message has been sent succesfully.'}

bottle.debug(True)
bottle.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)))
