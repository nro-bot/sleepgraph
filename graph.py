# major use of http://datadebrief.blogspot.com/2010/10/plotting-sunrise-sunset-times-in-python.html
# major use of http://stackoverflow.com/questions/5498510/creating-graph-with-date-and-time-in-axis-labels-with-matplotlib
# inspiration from http://stackoverflow.com/questions/886716/controling-bars-width-in-matplotlib-with-per-month-data
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates
import datetime
from matplotlib.ticker import FuncFormatter as ff
#data appears like so:

#date,init time,end time,elapsed time
#3/6/2013,4:30:00,8:45:00,4:15:00

data = genfromtxt('data.csv', delimiter=",", skiprows=1, dtype='string')
print data[1]

day = data[:,0]
hour1 = data[:,1]
hour2 = data[:,2]
hour3 = data[:,3]

inittime = [a+' '+b for a,b in zip(day, hour1)]
elapsedtime = [a+' '+b for a,b in zip(day, hour3)]

def dt2m(dt):
    return (dt.hour*60) + dt.minute
    
print inittime[0]

inittime = [datetime.datetime.strptime(foo,'%m/%d/%Y %H:%M:%S') for foo in inittime]
elapsedtime = [datetime.datetime.strptime(foo,'%m/%d/%Y %H:%M:%S') for foo in elapsedtime]

def m2hm(x, i):
    h = int(x/60)
    m = int(x%60)
    return '%(h)02d:%(m)02d' % {'h':h,'m':m}

inittime_mins = [dt2m(foo) for foo in inittime]
elaptime_mins = [dt2m(foo) for foo in elapsedtime]
#heights = [60,120,240]
print inittime_mins


fig = plt.figure(figsize=(12,7)) #figsize in inches
ax = fig.add_subplot(1, 1, 1)
ax.bar(inittime,elaptime_mins,bottom=inittime_mins)

plt.xticks(rotation='vertical')

# matplotlib date format object
hfmt = dates.DateFormatter('%b %d')
ax.xaxis.set_major_formatter(hfmt)
ax.xaxis.set_major_locator(MultipleLocator(1.0)) #a tick mark a day

ax.set_ylim([0, 24*60])
ax.yaxis.set_major_formatter(ff(m2hm))
ax.yaxis.set_major_locator(pylab.MultipleLocator(60)) #a tick mark an hour
     
