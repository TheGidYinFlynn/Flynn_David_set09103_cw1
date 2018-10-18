from flask import Flask , render_template
app = Flask(__name__)

@app.route('/home/')
def Home():
	return render_template('home.html')

@app.route('/character/')
def Character():
    return render_template('character.html')

@app.route('/item')
def item () :
   return render_template('item.html')

@app.route('/location')
def location () :
   return render_template('location.html')

@app.route('/about')
def about () : 
   return render_template('about.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=true)
