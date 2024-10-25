#!/usr/bin/env python3
"""A module to sort students according to average score"""


def get_avg(score_list):
    """To get the average of a score list"""

    avg = 0
    for score in score_list:
        if score.get('score'):
            avg += score.get('score')

    return avg / len(score_list)


if __name__ != '__main__':
    from pymongo import DESCENDING

    def top_students(mongo_collection):
        """A function to sort student by average score"""

        all_doc = mongo_collection.find()
        # iterate over all_docs and get the average score then update
        for doc in all_doc:
            avg_score = 0
            if doc.get('topics'):
                avg_score = get_avg(doc.get('topics'))
            mongo_collection.update_many(
                {'name': doc.get('name')},
                {'$set': {'averageScore': avg_score}})
        return mongo_collection.find(sort={'averageScore': DESCENDING})
