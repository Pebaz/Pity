"""
[✔] Rename project
[ ] Deploy on Zeit
[ ] Map url.pebaz.com wildcard domain to Zeit
[✔] Generate new ID for URL
[✔] Save URL to database
[✔] Return ID/URL to user
[✔] Allow redirecting using IDs
"""

import sys, os, time, base64
import requests
from flask import Flask, redirect, render_template, request, abort
import brotli

ctm = lambda: int(round(time.time() * 1000))
app = Flask(__name__)


data = 'Hello World!'
url = 'http://asdf.com/#/' + compress(data)
print(url)

def compress(data: str):
	c = brotli.compress(bytes(data, encoding='utf-8'))
	return base64.b64encode(c).decode('utf-8')

def decompress(data: str):
	d = base64.b64decode(bytes(data, encoding='utf-8'))
	return 


@app.route('/')
def index():
	"""
	Index page.
	"""
	return render_template('index.j2')


@app.route('/render', methods=['POST'])
def get_url(data):
	"""
	GET a previously-shortened URL by ID.

	POST a new URL to shorten.
	"""
	print(data)
	return "bah!"

	# try:
	# 	start = ctm()

	# 	print(f'Delay: {ctm() - start} ms')

	# 	print(f'REDIRECTING TO: {url}')
	# 	return redirect(url, code=302)
	# except Exception as e:
	# 	print(e)
	# 	abort(404)
		


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 9001))

	if sys.platform == 'win32':
		app.run(host='0.0.0.0', port=port)
	else:
		import bjoern
		bjoern.run(app, host='0.0.0.0', port=port)
