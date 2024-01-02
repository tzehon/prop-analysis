import os

from pymongo import MongoClient

client = MongoClient(os.environ.get("ATLAS_CONNECTION_STRING"))
db = client["ura"]
collection = db["transactions"]

def delete_transactions():
    result = collection.delete_many({})
    print(f"Number of documents deleted: {result.deleted_count}")

def insert_transactions(transactions):
    insertion_result = collection.insert_many(transactions["Result"])
    num_documents_inserted = len(insertion_result.inserted_ids)
    print(f"Number of documents inserted: {num_documents_inserted}")
    return num_documents_inserted

def close():
    client.close()