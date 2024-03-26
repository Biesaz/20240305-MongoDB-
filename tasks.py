# Create a CLI application that takes name surname gender and age (in a single sentence).
# Check if gender or age is provided correctly. Result save to database with timestamp of the event.

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict
import datetime
import argparse

# def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
#     client = MongoClient(host, port)
#     database = client[db_name]
#     return database

# def insert_document(collection: Collection, document: Dict) -> str:
#     result = collection.insert_one(document)
#     return str(result.inserted_id)

# # Example usage
# if __name__ == "__main__":
#     # Connection details
#     mongodb_host = 'localhost'
#     mongodb_port = 27017
#     database_name = 'mydatabase'
#     collection_name = 'mycollection'

#     # Connect to MongoDB
#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

#     # Retrieve a specific collection
#     collection = db[collection_name]

#     # Create (Insert) Operation
#     timestamp = datetime.datetime.now()
#     document = {
#         "name": "Jonas",
#         "surname": "Jonaitis",
#         "age": 18,
#         "gender": "Ono",
#         "timestamp": timestamp
#     }
#     inserted_id = insert_document(collection, document)
#     print(f"Inserted document with ID: {inserted_id}")



# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['user_data']
collection = db['users']

# Parse the input arguments
parser = argparse.ArgumentParser(description='CLI Application to save user data to MongoDB')
parser.add_argument('input_data', type=str, help='Enter name, surname, gender, and age in a single sentence')
args = parser.parse_args()

# Split the input sentence into individual components
input_data = args.input_data.split()
if len(input_data) != 4:
    print('Please provide name, surname, gender, and age in a single sentence.')
    exit()

name, surname, gender, age = input_data

# Validate gender and age
if gender.lower() not in ['male', 'female']:
    print('Invalid gender provided. Gender should be either "male" or "female".')
    exit()

try:
    age = int(age)
    if age < 0:
        raise ValueError
except ValueError:
    print('Invalid age provided. Age should be a positive integer.')
    exit()

# Save the user data to MongoDB with timestamp
timestamp = datetime.datetime.now()
user_data = {
    'name': name,
    'surname': surname,
    'gender': gender,
    'age': age,
    'timestamp': timestamp
}

result = collection.insert_one(user_data)
print('User data saved successfully with timestamp:', timestamp)

# Close the MongoDB connection
client.close()