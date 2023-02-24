# Our data set 
import time
start_time = time.time()
data = numpy.loadtxt('input_samples_50k.txt')
# Delay (lag) range that we are interesting in
lags = range(10)

''' numpy.correlate '''

import numpy

x = numpy.array(data) 

# Mean
mean = numpy.mean(data)

# Variance
var = numpy.var(data)

# Normalized data
ndata = data - mean

acorr = numpy.correlate(ndata, ndata, 'full')[len(ndata)-1:] 
acorr = acorr / var / len(ndata)
#print(acorr)
print("Execution Time: %s" % (time.time() - start_time))
