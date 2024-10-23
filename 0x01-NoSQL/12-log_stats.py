#!/usr/bin/env python3
"""A script to show log files"""

if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient()
    nginx_col = client.logs.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print(f"{nginx_col.count_documents({})} logs\nMethods:")
    for method in methods:
        print(f"\tmethod {method}:\
{nginx_col.count_documents({'method': method})}")
    print(f"{nginx_col.count_documents({'path': '/status', 'method': 'GET'})} status check")
