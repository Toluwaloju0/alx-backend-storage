#!/usr/bin/env python3
"""A script to find a document based on topic"""
if __name__ != '__main__':
    def schools_by_topic(mongo_collection, topic):
        """A function to find a document using the topic"""

        return mongo_collection.find({'topics': topic})
