# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient
from collections import OrderedDict

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    contests_ordered = contests.aggregate([
                                           {'$group':{'_id': '$user_id', 'Tscore':{'$sum':'$score'}, 'Telapse':{'$sum':'$submit_time'}}},
                                           {'$sort': OrderedDict([('Tscore', -1), ('Telapse', 1)])}
                                          ])
    rank0 = 1
    for it in contests_ordered:
        if it['_id'] == user_id:
            rank = rank0
            score = it['Tscore']
            submit_time = it['Telapse']
        rank0 += 1
    return rank, score, submit_time

if __name__ == '__main__':
    try:
        user_id = int(sys.argv[1])
    except:
        print('Parameter Error')
    userdata = get_rank(user_id)
    print(userdata)
