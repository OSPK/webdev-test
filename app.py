from flask import Flask, render_template

app = Flask(__name__)

# Define Routes
@app.route('/')
def index():
	name = "waqas"
	return render_template('main.html', name=name)

@app.route('/test')
def test():
	return render_template('test.html')

# Define Routes
@app.route('/<name>')
def index_name(name=None):
	test = 5
	return render_template('main.html', name=name)