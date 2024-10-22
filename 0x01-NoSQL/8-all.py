#!/usr/bin/env python3
"""A script to list all documentsin a database"""\

if __name__ != '__main__':
    def list_all(mongo_collection):
        """A function to return all documents in a collection """

        return mongo_collection.find()
