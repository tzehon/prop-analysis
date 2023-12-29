import os
import requests

from flask import Flask

app = Flask(__name__)


@app.route("/")
def pull_data():
    response = requests.get('https://curlmyip.org/')
    external_ip = response.text
    print(f"This is your external IP: {external_ip}")

    access_key = os.getenv('ACCESS_KEY')
    print(f"This is your key: {access_key}")
    return f"access key: {access_key}, external IP: {external_ip}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))