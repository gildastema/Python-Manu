import os
import requests
from flask import request

from flask import Flask

app = Flask(__name__)




@app.route("/status")
def status():
    response = {
        'result' : "success"
    }
    return response



@app.route("/ip")
def get_location():
    ip_address = request.remote_addr
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    if response['error'] :
        return response
    else :
        location_data = {
            "ip": ip_address,
            "city": response['city'],
            "state": response["region"],
        }
        return location_data



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)