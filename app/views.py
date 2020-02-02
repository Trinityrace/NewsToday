from flask import render_template
from app import app

# Views
@app.route("/movuie/<movie_id>")
def index():

  '''
  View root page function returns index page and its data
  '''

  message = 'NEWS TODAY!'
  return render_template('index.html', message = message)
  