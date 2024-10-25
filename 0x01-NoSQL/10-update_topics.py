#!/usr/bin/env python3
"""A module to update a document"""

if __name__ != '__main__':
    def update_topics(mongo_collection, name, topics):
        """A function to update a database"""

        mongo_collection.update_one({'name': name},
                                    {'$set': {'topics': topics}})
