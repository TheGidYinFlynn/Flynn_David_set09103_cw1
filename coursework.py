from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello Napier finally this is working'

@app.route('/hello/')
def hello():
     return 'Hello Everyone !!!'

@app.route('/goodbye/')
def goodbye():
    return 'goodbye everyone'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=true)
