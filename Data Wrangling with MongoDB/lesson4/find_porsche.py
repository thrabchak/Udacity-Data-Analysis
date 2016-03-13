#!/usr/bin/env python
"""
Your task is to complete the 'porsche_query' function and in particular the query
to find all autos where the manufacturer field matches "Porsche".
Please modify only 'porsche_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB and download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials at
the following link:
https://www.udacity.com/wiki/ud032
"""

import json

def porsche_query():
    # Please fill in the query to find all autos manuafactured by Porsche.
    query = {"manufacturer" : "Porsche"}
    return query

def add_car(db):
    with open('example_car.json') as data_file:    
        data = json.load(data_file)
    db.autos.insert(data)

# Do not edit code below this line in the online code editor.
# Code here is for local use on your own computer.
def get_db(db_name):
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def find_porsche(db, query):
    return db.autos.find(query)

if __name__ == "__main__":
    # For local use
    db = get_db('examples')
    #add_car(db)
    query = porsche_query()
    results = find_porsche(db, query)

    print("Printing first 3 results\n")
    import pprint
    for car in results[:3]:
        pprint.pprint(car)