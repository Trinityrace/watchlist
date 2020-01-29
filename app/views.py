from flask import render_template
from flask import app

#views
@app.route('/')
def index():
  '''
  view root page function that returns the index page and its data.
  '''
  # return render_template('index.html')

  message = 'Hello Trinity'
  return render_template ('index.html',message = message)