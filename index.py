import sys, os, time, base64, traceback
from pathlib import Path
import requests
import brotli
from flask import Flask, redirect, render_template, request, abort

app = Flask(__name__)

# You need to set your app's name in Heroku's environment variables as:
# host="your-app.herokuapp.com"
HOST = f'{os.environ.get("host", "localhost")}:{os.environ.get("PORT", 9001)}'


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
	defaults = [[f'/{i}', i.stem[8:]] for i in Path('./static/defaults').iterdir()]

	with open('static/defaults/default_bulma.html') as file:
		return render_template('edit.j2', html=file.read(), defaults=defaults)


@app.route('/bit-length', methods=['POST'])
def bit_length():
	data = request.get_json()
	if not data:
		return '0'
	return f'{len(compress(data["value"]))}'


@app.route('/compress', methods=['POST'])
def compress_url():
	# Trim hash from URL
	params = request.get_json()
	data = params['value']
	compressed = compress(data)

	if params['GENERATE_FRAGMENT_URL'] and len(compressed) > 2000:
		return (f'Error - Compressed content too large: '
				f'{len(compressed)}/2000. Limit to 2000 bytes.')
	
	stub = '#/' if params['GENERATE_FRAGMENT_URL'] else ''
	url = f'http://{HOST}/{stub}{compressed}'
	return url



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
