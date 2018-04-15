import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def analysis(fil):
    record = pd.read_json(fil)
    extra = record[['user_id', 'minutes']].groupby('user_id').sum()
    x = list(extra.index)
    #print('xlen: {}, xtype: {}'.format(len(x), type(x)))
    y = list(extra['minutes'])
    #print('ylen: {}, ytype: {}'.format(len(y), type(y)))
    return x, y, 



def data_plot(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    majorx_ticks = np.arange(0, max(x), 50000)
    majory_ticks = np.arange(0, max(y), 500)

    ax.set_title("StudyData")
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    ax.set_xticks(majorx_ticks)
    ax.set_yticks(majory_ticks)

    ax.plot(x, y, 'b-')
    #ax.set_xlim([min(x), max(x)])
    plt.show()
    return ax

if __name__ == '__main__':
    fil = 'user_study.json'
    x, y = analysis(fil)
    data_plot(x, y)
