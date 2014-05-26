import bottle
import cgi
import re
import mandrill
import os

mandrill_client = mandrill.Mandrill('a0ofkf1HNIwYt2P0CZ-CYQ')

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

	return bottle.redirect('http://jgwil2.github.io/contact/thanks.html')

bottle.debug(True)
bottle.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)))
