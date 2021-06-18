from flask import Flask
from flask_app.apis import test as bp_test
from flask_app.apis import demo as bp_demo
from flask_app.apis import auth as bp_auth
from flask_login import LoginManager, login_required
from flask_app.apis import User
from flask_app.dash import plot


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object("config.Config")

    app.secret_key = 's3cr3t'
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Add dash plot into the min app
    dash_plot = plot.create_dash()
    dash_plot.init_app(app)

    for view_func in app.view_functions:
        if view_func.startswith("/dash/"):
            app.view_functions[view_func] = login_required(app.view_functions[view_func])

    @login_manager.user_loader
    def load_user(user_id):
        user = User.User()
        return user

    app.register_blueprint(bp_test.test)
    app.register_blueprint(bp_demo.demo)
    app.register_blueprint(bp_auth.auth)

    #with app.app_context():
        # Failed in this way
        #from flask_app import routes
        #from flask_app.dash import plot

        #app = plot.create_dash()
    return app
