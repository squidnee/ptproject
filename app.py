from flask import Flask, render_template, url_for
import json

app = Flask(__name__)
ctx = app.test_request_context()
ctx.push()
app.preprocess_request()

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)