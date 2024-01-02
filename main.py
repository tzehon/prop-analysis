import os
import ura_api_utils as ura

from flask import Flask

app = Flask(__name__)

@app.route("/")
def pull_data():
    ura.print_external_ip()
    access_key = ura.get_access_key()
    token = ura.get_token(access_key)

    num_transactions = 0
    for batch in ura.batches:
        transactions = ura.get_transactions(access_key, token, batch)
        num_transactions += ura.save_transactions(transactions)
    print(f"NUM TRANSACTIONS: {num_transactions}")
    return f"NUM TRANSACTIONS: {num_transactions}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))