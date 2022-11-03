import json
import os

from flask import Flask

app = Flask(__name__)


@app.route("/status")
def root():
    response = {
        'result' : "success"
    }
    return json.dumps(response)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)