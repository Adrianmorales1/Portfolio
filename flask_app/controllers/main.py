from flask_app import app
from flask import Flask, request, session, render_template, flash, redirect
from flask_app.models.email_send import Email

@app.route('/')
def dashboard():
    return render_template('home.html')

@app.route('/send_email', methods = ['POST'])
def sending_email():
    data = {
        'subject' : request.form['name'],
        'body' : request.form['message'],
        'sender' : request.form['email']
    }
    email = Email()
    email.send_email(data)
    return redirect('/')