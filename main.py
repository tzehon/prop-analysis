import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def pull_data():
    access_key = os.getenv('ACCESS_KEY')
    print(f"This is your key: {access_key}")
    return f"access key: {access_key}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))