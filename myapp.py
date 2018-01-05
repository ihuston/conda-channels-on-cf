"""Cloud Foundry test"""
from flask import Flask
import os, sys

try:
    from mypkg import mypkg
except ImportError:
    msg = "mypkg not available"
else:
    msg = "Message from mypkg: " + mypkg.hello_world()    

try:
    from prettytable import PrettyTable
except ImportError:
    pretty_msg = "prettyTable not available"
else:
    x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
    x.add_row(["Adelaide", 1295, 1158259, 600.5])
    x.add_row(["Brisbane", 5905, 1857594, 1146.4])
    x.add_row(["Darwin", 112, 120900, 1714.7])
    pretty_msg = "Message from prettytable: <br />" + x.get_html_string() 



app = Flask(__name__)

port = int(os.getenv("VCAP_APP_PORT", default="8099"))

@app.route('/')
def hello_world():
    return msg + "<br />" + pretty_msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
