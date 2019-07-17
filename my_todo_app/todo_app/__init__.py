import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that list my todos
    @app.route('/saurabh')
    def saurabh():
        return ('Wake Up' + '<br/>' +
            'Eat' + '<br/>' +
            'Code' + '<br/>'+
	    'Repeat' + '<br/>'
        )

    return app
