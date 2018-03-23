from flask import Flask, request
import get_sharable_links
import json

app = Flask(__name__)

@app.route("/create_links", methods=['POST'])
def create_links():
    payload = request.get_json()
    resp = get_sharable_links.start(payload['api_key'], payload['folders'])
    return json.dumps(resp)

if (__name__ == "__main__"):
    app.run(port = 5000)