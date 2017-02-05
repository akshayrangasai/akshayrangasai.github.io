#Imports for solution
import numpy as np
import scipy.stats as sp
from matplotlib.pyplot import *
#Setting Distribution variables
##All rates are in per Minute.

QUEUE_ARRIVAL_RATE = 6
QUEUE_BUFFER_TIME = 4 #Takes 15 seconds to cover queue
N_SCANNERS = 1
SCANNER_BAG_CHECKING_RATE = 3 #Takes 20 seconds to put your bag on Scanner
FRISK_MACHINES_PER_SCANNER = 1 #Number of people checking machine per scanner
N_FRISK_MACHINES = N_SCANNERS*FRISK_MACHINES_PER_SCANNER
FRISK_CHECKING_RATE = 2 #Half a minute per frisk
SCANNER_RATE = SCANNER_BAG_CHECKING_RATE*N_SCANNERS
FRISK_RATE = FRISK_CHECKING_RATE*N_FRISK_MACHINES
FRISK_ARRIVAL_RATE = SCANNER_RATE
#Modeling First Part of the Queue
ARRIVAL_PATTERN = sp.poisson.rvs(QUEUE_ARRIVAL_RATE,size = 60) #for an hour

ARRIVAL_LIST = []

for index, item in enumerate(ARRIVAL_PATTERN):
    ARRIVAL_LIST += [index]*item

#print ARRIVAL_LIST

TIMEAXIS = np.linspace(1,60,60)


arrivalfig = figure()
arrivalplot = plot(TIMEAXIS,ARRIVAL_PATTERN,'o')
show()


SCAN_PATTERN = sp.poisson.rvs(SCANNER_RATE,size=60)
SCAN_LIST = []
for index, item in enumerate(SCAN_PATTERN):
    SCAN_LIST += [index]*item

arrivalfig = figure()
arrivalplot = plot(TIMEAXIS,SCAN_PATTERN,'o')
show()


FRISK_PATTERN = sp.poisson.rvs(FRISK_RATE,size=60)
FRISK_LIST = []
for index, item in enumerate(FRISK_PATTERN):
    FRISK_LIST += [index]*item

arrivalfig = figure()
arrivalplot = plot(TIMEAXIS,FRISK_PATTERN,'o')
show()

EXIT_NUMER = zip(FRISK_PATTERN,SCAN_PATTERN)
EXIT_NUMBER = [min(k) for k in EXIT_NUMER]

EXIT_PATTERN = []

for index, item in enumerate(EXIT_NUMBER):
    EXIT_PATTERN += [index]*item

RESIDUAL_ARRIVAL_PATTERN = ARRIVAL_LIST[0:len(EXIT_PATTERN)]
WAIT_TIMES = [m-n for m,n in zip(EXIT_PATTERN,RESIDUAL_ARRIVAL_PATTERN)]

#print EXIT_PATTERN

'''
for i,val in EXIT_PATTERN:
    WAIT_TIMES += [ARRIVAL_PATTERN(i) - val]
'''

plot(WAIT_TIMES,'r-')
show()
