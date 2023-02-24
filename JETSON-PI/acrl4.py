# Our data set 
data = numpy.loadtxt('input_samples_50k.txt')

import time
start_time = time.time()

# Delay (lag) range that we are interesting in
lags = range(10)

''' Fourier transform implementation '''

import numpy

# Nearest size with power of 2
size = 2 ** numpy.ceil(numpy.log2(2*len(data) - 1)).astype('int')

# Variance
var = numpy.var(data)

# Normalized data
ndata = data - numpy.mean(data)

# Compute the FFT
fft = numpy.fft.fft(ndata, size)

# Get the power spectrum
pwr = numpy.abs(fft) ** 2

# Calculate the autocorrelation from inverse FFT of the power spectrum
acorr = numpy.fft.ifft(pwr).real / var / len(data)
#print(acorr)
print("Execution Time: %s" % (time.time() - start_time))
