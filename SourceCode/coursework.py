from flask import Flask , render_template
app = Flask(__name__)

#home page
@app.route('/home/')
def Home():
	return render_template('home.html')

#character page
@app.route('/character/')
@app.route('/character/<name>')
def Character(name=None):

    return render_template('character.html' , name=name)

#item page
@app.route('/item/')
@app.route('/item/<name>')
def item (name=None) :
   return render_template('item.html' , name=name)

#location page
@app.route('/location/')
@app.route('/location/<name>')
def location (name=None) :
   return render_template('location.html' , name=name)

#about page
@app.route('/about')
def about () :
   return render_template('about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=true)
