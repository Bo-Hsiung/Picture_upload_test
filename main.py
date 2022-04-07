from flask import Flask
from datetime import timedelta
import re,os,route

from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
SESSION_TYPE = "redis"
# PERMANENT_SESSION_LIFETIME = 30
app.config.update(SECRET_KEY=os.urandom(24))
app.permanent_session_lifetime = timedelta(seconds=2)
# app.config['UPLOAD_FOLDER']='./TPMI/ICF/static/upload'
app.config['MAX_CONTENT_PATH']= 1024*1024*1024
app.register_blueprint(route.app)
CORS(app)

app.run(host="0.0.0.0")

