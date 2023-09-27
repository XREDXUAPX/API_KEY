import flask , json
import requests
import re
import flask
from flask import Flask , request

app = Flask(__name__)
#@app.route("/")
@app.route("/key")
def dd():
	key = request.args.get('Api_key')
	up = ('yes')
	km = ('no')
	ww = ('hook')
	if key == up or km or ww :
	   return 'nice '
	else :
	   return 'bad'
    
app.run()