"""Cloud Foundry test"""
from flask import Flask
import os, sys

try:
    from mypkg import mypkg
except ImportError:
    msg = "mypkg not available"
else:
    msg = "Message from mypkg: " + mypkg.hello_world()    


app = Flask(__name__)

port = int(os.getenv("VCAP_APP_PORT", default="8099"))

@app.route('/')
def hello_world():
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
