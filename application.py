"""
A simple bagtracking flask app.
"""

import flask
from flask.views import MethodView
from index import Index
from createtag import createtag
from viewtag import View
from sendtext import sendtext
from about import About
from qr import Qr


print("Lost My Bag Website @lostmybag.com Started")


application = flask.Flask(__name__)       # our Flask app

application.add_url_rule('/qr/',
                 view_func=Qr.as_view('qr'),
                 methods=["GET"])

application.add_url_rule('/about/',
                 view_func=About.as_view('about'),
                 methods=["GET"])

application.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])


application.add_url_rule('/static/<path:filename>',endpoint='static',view_func=application.send_static_file) 

application.add_url_rule('/viewtag/',
                 view_func=View.as_view('viewtag'),
                 methods=['GET', 'POST'])

application.add_url_rule('/submit/',
                 view_func=createtag.as_view('createtag'),
                 methods=['GET', 'POST'])

application.add_url_rule('/sendtext/<string:id>',
                 view_func=sendtext.as_view('sendtext'),
                 methods=['POST'])


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000, debug=True)
    print (request.remote_addr)
