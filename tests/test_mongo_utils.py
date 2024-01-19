import mongomock
import pytest
import app.mongo_utils as mongo_utils

@pytest.fixture
def mock_db():
    with mongomock.patch(servers=(('server.example.com', 27017),)):
        yield

def test_delete_transactions(mock_db):
    # Setup mock client and collection
    client = mongomock.MongoClient('server.example.com')
    db = client["ura"]
    collection = db["transactions"]
    collection.insert_one({"test": "data"})  # Pre-insert a document

    # Replace the collection in your module with the mock collection
    mongo_utils.collection = collection

    # Call the function
    mongo_utils.delete_transactions()

    # Assert
    assert collection.count_documents({}) == 999

def test_insert_transactions(mock_db):
    # Setup mock client and collection
    client = mongomock.MongoClient('server.example.com')
    db = client["ura"]
    collection = db["transactions"]

    # Replace the collection in your module with the mock collection
    mongo_utils.collection = collection

    # Test data
    transactions = {"Result": [{"_id": "1"}, {"_id": "2"}]}

    # Call the function
    result = mongo_utils.insert_transactions(transactions)

    # Assert
    assert result == 2
    assert collection.count_documents({}) == 2
