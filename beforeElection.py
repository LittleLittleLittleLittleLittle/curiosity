from helperFunctions import findSubSequence
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.dates as mdates
import re

data = pd.read_csv('/Users/xiao_yang/Documents/Life/Stock/projects/curiosity/data/spy.csv', sep="\t")
electionDate = pd.read_csv('/Users/xiao_yang/Documents/Life/Stock/projects/curiosity/data/electionDate.csv')


electionDate = electionDate['election day'].map(lambda x: re.sub("[^0-9]+", "-Nov-", x)).tolist()
electionDate = [item[:(-4)]+item[-2:] for item in electionDate]

data = data.reindex(index=data.index[::-1])
data = data.reset_index(drop=True)
print data.head()

myFmt = mdates.DateFormatter('%d')

# print data.head()
print data.tail()
data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
# data.date = pd.to_datetime(data.date)

numDays = 9
seq = data['close'].tolist()

ind = data[data['date'].isin(electionDate)].index.tolist()
print ind

left = 30
right = 30


with PdfPages('/Users/xiao_yang/Documents/Life/Stock/projects/curiosity/plot/election.pdf') as pdf:
    for i in range(len(ind)):
        thisInd = ind[i]
        plotInd = i%9
        print data.ix[thisInd, 'date']
        if plotInd == 0:
            plt.figure()
        # print data.ix[(i-8):(i+2), ['date','close']]
        # plt.figure()
        # print range(10)
        # print data.ix[(thisInd-8):(thisInd+2), :]
        thisDate = data.ix[(thisInd-left):(thisInd+right), 'date'].tolist()
        print thisDate[left]
        # thisDate.reverse()
        thisPrice = data.ix[(thisInd-left):(thisInd+right), 'close'].tolist()
        color = 'black'
        # thisPrice.reverse()
        plt.subplot(3, 2, plotInd+1)
        theseTicks = np.arange(0, len(thisDate), 3).tolist()
        plt.xticks(theseTicks, [thisDate[j] for j in theseTicks], fontsize=5, rotation=30)
        plt.yticks(fontsize=6)
        # ax.xaxis.set_major_formatter(myFmt)
        plt.plot(range(len(thisDate)), thisPrice, color=color)
        # plt.plot((left-numDays, left-numDays), (min(thisPrice)-0.2, max(thisPrice)+0.2), 'k-')
        plt.plot((left, left), (min(thisPrice)-0.2, max(thisPrice)+0.2), 'k-')
        plt.grid(True)
        # plt.gcf().autofmt_xdate()
        if plotInd==8 or i==(len(ind)-1):
            pdf.savefig()
            # plt.savefig('/Users/xiao_yang/Documents/Life/Stock/projects/curiosity/plot/spy' + str(i/9) + '.png')

