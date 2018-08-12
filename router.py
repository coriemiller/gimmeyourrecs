from flask import Flask, request, Response, render_template, redirect
import requests

app = Flask(__name__)
# app.config['SERVER_NAME'] = 'localhost.dev:5000'



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users', methods=['POST'])
def create_user():
	username = request.form['username']
	redirect_url = 'http://' + username + '.' + app.config['SERVER_NAME']
	return redirect(redirect_url, code=302)

@app.route("/", subdomain="<username>")
def username_index(username):
    """Dynamic subdomains are also supported
    Try going to user1.your-domain.tld/dynamic"""
    return username + " the subdomain worked"