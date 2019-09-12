from flask import Flask
from .landing import landing_routes

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Config')
    
    with app.app_context():

        #importing the landing component
        from .landing import landing_routes

        app.register_blueprint(landing_routes.landing_bp)


        return app
