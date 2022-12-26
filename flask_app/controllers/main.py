from flask_app import app
from flask import Flask, request, session, render_template, flash, redirect

@app.route('/')
def dashboard():
    return render_template('home.html')

