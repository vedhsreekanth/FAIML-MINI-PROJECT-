from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create database
db = client["Covid_project"]

# Create collection
collection = db["covid_data"]

# Load JSON file
with open("covid19.json") as file:
    data = json.load(file)

# Insert data
collection.insert_many(data)

print("Data successfully inserted into MongoDB!")
