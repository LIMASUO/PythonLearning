import json
import pandas as pd

def analysis(file, user_id):
    times = 0
    minutes = 0
    record = pd.read_json(file)
    extra = record[record['user_id']==user_id]['minutes']
    #print(extra.size)
    times = extra.count()
    minutes = extra.sum()

    return times, minutes

if __name__ == '__main__':
    
    fil = 'user_study.json'
    user_id = 199071
    #print(analysis(fil, user_id))
