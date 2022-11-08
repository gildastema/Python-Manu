import os
import requests
from flask import request

from flask import Flask

app = Flask(__name__)




@app.route("/status")
def status():
    """_summary_
    Define the end point to get status of service
    Returns:
        dict:response 
    """
    response = {
        'result' : "success"
    }
    return response



@app.route("/ip")
def get_location():
    """_summary_
        Get information about city base uppon of the ip
    Returns:
        _type_: _description_
    """
    ip_address = request.remote_addr # Get Call Ip
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json() # Call Service to convert IP to state and city
    if response['error'] : ## if error return a response 
        return response
    else :
        location_data = {
            "ip": ip_address,
            "city": response['city'], # Extract city
            "state": response["region"], # Extract state
        }
        return location_data



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) # Get port
    app.run(debug=False, host='0.0.0.0', port=port) # Launch the application