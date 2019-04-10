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

def compress(data: str):
	c = brotli.compress(bytes(data, encoding='utf-8'))
	return base64.b64encode(c).decode('utf-8')

def decompress(data: str):
	d = base64.b64decode(bytes(data, encoding='utf-8'))
	return brotli.decompress(d).decode('utf-8')

data = 'Hello World!'
url = 'http://asdf.com/#/' + compress(data)
print(url)


@app.route('/')
def index():
	return render_template('index.j2')

@app.route('/edit')
def edit():
	return render_template('edit.j2')

@app.route('/bit-length', methods=['POST'])
def bit_length():
	data = request.get_json()
	if not data:
		return '0'
	return f'{len(compress(data["value"]))}'

@app.route('/compress', methods=['POST'])
def compress_url():
	# Trim hash from URL
	data = request.get_json()['value']
	compressed = compress(data)
	if len(compressed) > 2000:
		return f'Error - Compressed content too large: {len(compressed)}/2000. Limit to 2000 bytes.'
	else:
		if sys.platform == 'win32':
			return f'http://localhost:9001/#/{compressed}'
		else:
			return f'http://pbz-pity.heroku-app.com/#/{compressed}'

@app.route('/render', methods=['POST'])
def render():
	# Trim hash from URL
	data = request.get_json()['value'].replace('#/', '').replace('#', '')
	if data:
		return decompress(data)
	else:
		return ''


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 9001))

	if sys.platform == 'win32':
		app.run(host='0.0.0.0', port=port)
	else:
		import bjoern
		bjoern.run(app, host='0.0.0.0', port=port)
