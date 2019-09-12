from flask import Flask, render_template, redirect, request, flash
from forms import SignupForm
import config
import sys
import json


app = Flask(__name__,
            instance_relative_config=False,
            template_folder="templates",
            static_folder="static"
            )


@app.route('/')
def index():
    return render_template('/index.html', title="Lipaswift | Buy Now, Pay Later")


@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

    
@app.route('/how')
def how():
    return render_template('how.html', title='How It Works')

@app.route('/partners')
def partners():
    return render_template('partners.html', title="Our Partners")

@app.route('/deals')
def deals():
    return render_template('deals.html', title="Hot deals")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Signup Form."""
    signup_form = SignupForm()
    if request.method == 'POST':
        if signup_form.validate():
            flash('Logged in successfully.')
            return render_template('/dashboard.html', template="dashbord-template")
    return render_template('/signup.html', form=signup_form, template="form-page")