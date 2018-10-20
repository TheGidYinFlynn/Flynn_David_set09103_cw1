from flask import Flask , render_template
app = Flask(__name__)

@app.route('/home/')
def Home():
	return render_template('home.html')

@app.route('/character/')
@app.route('/character/<name>')
def Character(name=None):

    return render_template('character.html' , name=name)

@app.route('/item/')
@app.route('/item/<name>')
def item (name=None) :
   return render_template('item.html' , name=name)

@app.route('/location/')
@app.route('/location/<name>')
def location (name=None) :
   return render_template('location.html' , name=name)

@app.route('/about')
def about () :
   return render_template('about.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=true)
