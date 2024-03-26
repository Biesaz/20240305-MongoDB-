# Write a data population script. The script/function should create a document,
# with necessary fields. Values should be auto generated (random number/numbers, int, float, random words etcs.) 
# and itteration=0 value how many documents we want to populate the DB.
# For the beggining lets agree that we want to create a database people, with collection
# employees . Fields: name,surname,age,years employed.

# import pymongo
# import random
# import string

# # Connect to MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["people"]
# collection = db["employees"]

# # Function to generate random data
# def generate_random_data():
#     name = ''.join(random.choices(string.ascii_uppercase, k=5))
#     surname = ''.join(random.choices(string.ascii_uppercase, k=7))
#     age = random.randint(20, 60)
#     years_employed = random.randint(1, 10)
#     return {"name": name, "surname": surname, "age": age, "years_employed": years_employed}

# # Function to populate the database
# def populate_database(iterations):
#     for _ in range(iterations):
#         data = generate_random_data()
#         collection.insert_one(data)

# # Specify the number of documents to populate
# iterations = 10
# populate_database(iterations)
# print(f"{iterations} documents inserted into the 'employees' collection.")

#####################################################################################
############# Mykolo #################
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict
from faker import Faker
from random import randint


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def insert_document(collection: Collection, document: Dict) -> str:
    result = collection.insert_one(document)
    print(f"Printed result: {result}")
    return str(result.inserted_id)


def create_a_person():
    fake = Faker()
    name = fake.first_name()
    surname = fake.last_name()
    age = randint(18, 75)
    years_employed = (
        -1
    )  # Cannot use zero, as it is a valid value, can't use None, as it wont work
    while age - 18 < years_employed or years_employed == -1:
        years_employed = randint(0, 55)
    return name, surname, age, years_employed

if __name__ == "__main__":
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "People"
    collection_name = "employees"

    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    collection = db[collection_name]
    fake = Faker()
    for _ in range(10):
        name, surname, age, years_employed = create_a_person()
        document = {
            "name": name,
            "surname": surname,
            "age": age,
            "years_employed": years_employed,
        }
        inserted_id = insert_document(collection, document)
        print(f"Inserted document with ID: {inserted_id}")
        print(f"This person was inserted into the database: {document}")

#################################################################################
############### Saruno #################
#         from pymongo import MongoClient
# from pymongo.database import Database
# from pymongo.collection import Collection
# from typing import Dict
# from faker import Faker
# import random

# def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
#     client = MongoClient(host, port)
#     database = client[db_name]
#     return database

# def insert_document(collection: Collection, document: Dict) -> str:
#     result = collection.insert_one(document)
#     print(f"Result: {result}")
#     return str(result.inserted_id)

# def create_document() -> Dict:
#     fake = Faker()
#     name = fake.first_name()
#     surname = fake.last_name()
#     age = random.randint(18, 100)
#     years_emp = random.randint(0, 50)
    
#     return {
#         "name": name,
#         "surname": surname,
#         "age": age,
#         "years_emp": years_emp 
#     }

# if __name__ == "__main__":
#     mongodb_host = 'localhost'
#     mongodb_port = 27017
#     database_name = 'people'
#     collection_name = 'employees'

#     db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)
#     collection = db[collection_name]

#     itteration = 2
#     for _ in range(itteration):
#         document = create_document()
#         inserted_id = insert_document(collection, document)
#         print(f"Inserted document with ID: {inserted_id}")

#######################################################################
############## 

