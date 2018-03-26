from flask import Flask, request, jsonify, render_template
import get_sharable_links

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('/index.html')


@app.route("/create_links", methods=['POST'])
def create_links():
    payload = request.get_json()
    resp = get_sharable_links.start(payload['api_key'], payload['folders'])
    return jsonify(resp)

@app.route("/get_status/<token>")
def get_status(token):
	tokenResponse = get_sharable_links.get_token_status(token)
	return jsonify(tokenResponse)

if (__name__ == "__main__"):
    app.run(port = 5000)