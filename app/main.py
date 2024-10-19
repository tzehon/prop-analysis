import os
import ura_api_utils as ura
import mongo_utils as mongo
from flask import Flask

app = Flask(__name__)

@app.route("/")
def pull_data():
    ura.print_external_ip()
    access_key = ura.get_access_key()
    token = ura.get_token(access_key)

    transactions_inserted = 0
    mongo.delete_transactions()
    for batch in ura.batches:
        print(f"BATCH: {batch}")
        transactions = ura.get_transactions(access_key, token, batch)
        transactions_inserted += mongo.insert_transactions(transactions)

    print(f"PRIVATE PROPERTY TRANSACTIONS INSERTED: {transactions_inserted}")
    return f"PRIVATE PROPERTY TRANSACTIONS INSERTED: {transactions_inserted}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))