import numpy
data = numpy.loadtxt('input_samples_50k.txt')

import time
start_time = time.time()

# Delay (lag) range that we are interesting in
lags = range(10)

''' Statsmodels '''

import statsmodels.api as sm

acorr = sm.tsa.acf(data, nlags = len(lags)-1)
#print(acorr)
print("Execution Time: %s seconds" % (time.time() - start_time))
