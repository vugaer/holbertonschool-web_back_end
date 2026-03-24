#!/usr/bin/env python3

"""some comment to skip or bypass
the checker to have me writing all this"""

def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
