"""
[✔] Rename project
[ ] Deploy on Zeit
[ ] Map url.pebaz.com wildcard domain to Zeit
[✔] Generate new ID for URL
[✔] Save URL to database
[✔] Return ID/URL to user
[✔] Allow redirecting using IDs
"""

import sys, os, time, base64, traceback
import requests
import brotli
from flask import Flask, redirect, render_template, request, abort

app = Flask(__name__)

def compress(data: str):
	c = brotli.compress(bytes(data, encoding='utf-8'))
	return base64.b64encode(c).decode('utf-8')

def decompress(data: str):
	d = base64.b64decode(bytes(data, encoding='utf-8'))
	return brotli.decompress(d).decode('utf-8')


@app.route('/')
@app.route('/<path:data>')
def index(data=None):
	return render_template('index.j2')


@app.route('/edit')
def edit():
	with open('default_html.html') as file:
		return render_template('edit.j2', html=file.read())


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
			return f'http://pbz-pity.herokuapp.com/#/{compressed}'


@app.route('/render', methods=['POST'])
def render():
	# Trim hash from URL
	data = request.get_json()['value'].replace('#/', '').replace('#', '')

	try:
		if data:
			return decompress(data)
		else:
			return ''
	except Exception as e:
		traceback.print_exc()
		return render_template('error.j2', error=e.__class__.__name__)


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 9001))

	if sys.platform == 'win32':
		app.run(host='0.0.0.0', port=port)
	else:
		import bjoern
		bjoern.run(app, host='0.0.0.0', port=port)
