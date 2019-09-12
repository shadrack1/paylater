from flask import Blueprint, render_template
from flask import current_app as current_app

landing_bp = Blueprint('landing_bp', __name__, template_folder='templates', static_folder='static')


@landing_bp.route('/')
def index():
    return render_template('/index.html', title="Lipaswift | Buy Now, Pay Later")


@landing_bp.route('/about')
def about():
    return render_template('about.html', title="About Us")

    
@landing_bp.route('/how')
def how():
    return render_template('how.html', title='How It Works')

@landing_bp.route('/partners')
def partners():
    return render_template('partners.html', title="Our Partners")

@landing_bp.route('/deals')
def deals():
    return render_template('deals.html', title="Hot deals")

#@app.route('/signup', methods=['GET', 'POST'])
#def signup():
    #"""Signup Form."""
    #signup_form = SignupForm()
    #if request.method == 'POST':
        #if signup_form.validate():
            #flash('Logged in successfully.')
            #return render_template('/dashboard.html', template="dashbord-template")
    #return render_template('/signup.html', form=signup_form, template="form-page")