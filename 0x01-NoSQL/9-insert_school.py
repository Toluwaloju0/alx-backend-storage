#!/usr/bin/env python3
"""A module to insert a document in a collection"""

if __name__ != '__main__':
    def insert_school(mongo_collection, **kwargs):
        """A function to insert into a collection"""

        result = mongo_collection.insert_one(kwargs)

        return result.inserted_id
