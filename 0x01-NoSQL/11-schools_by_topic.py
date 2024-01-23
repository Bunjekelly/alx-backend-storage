#!/usr/bin/env python3

"""a Python function that returns the list of school having a specific topic"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """function definition"""
    result = mongo_collection.find({"topic": topic})
    return [doc for doc in result]
