from helperFunctions import findSubSequence
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.dates as mdates

data = pd.read_csv('/Users/xiao_yang/Documents/Life/Stock/projects/curiosity/data/spy.csv')

data = data.reindex(index=data.index[::-1])
data = data.reset_index(drop=True)
print data.head()

myFmt = mdates.DateFormatter('%d')

# print data.head()
print data.tail()
data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
# data.date = pd.to_datetime(data.date)

numDays = 8
seq = data['close'].tolist()
ind = findSubSequence(seq, numDays)
print ind
print len(ind)

left = 8
right = 8

with PdfPages('/Users/xiao_yang/Documents/Life/Stock/projects/curiosity/plot/spy.pdf') as pdf:
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
        # thisDate.reverse()
        thisPrice = data.ix[(thisInd-left):(thisInd+right), 'close'].tolist()
        # thisPrice.reverse()
        plt.subplot(3, 3, plotInd+1)
        theseTicks = np.arange(0, len(thisDate), 3).tolist()
        plt.xticks(theseTicks, [thisDate[j] for j in theseTicks], fontsize=5, rotation=30)
        plt.yticks(fontsize=6)
        # ax.xaxis.set_major_formatter(myFmt)
        plt.plot(range(len(thisDate)), thisPrice)
        plt.plot((left-numDays, left-numDays), (min(thisPrice)-0.2, max(thisPrice)+0.2), 'k-')
        plt.plot((left, left), (min(thisPrice)-0.2, max(thisPrice)+0.2), 'k-')
        plt.grid(True)

        # plt.gcf().autofmt_xdate()
        if plotInd==8 or i==(len(ind)-1):
            pdf.savefig()

            # plt.savefig('/Users/xiao_yang/Documents/Life/Stock/projects/curiosity/plot/spy' + str(i/9) + '.png')