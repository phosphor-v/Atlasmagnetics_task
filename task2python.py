import statistics 
data = [364, 373, 358, 394, 378, 379, 357, 364, 350, 363, 392, 368, 359, 375, 399, 365, 379, 357, 380]
 
print("Standard Deviation of the sample is % s "% (statistics.stdev(data)))
print("Mean of the sample is % s " % (statistics.mean(data)))
print("Median of the sample is % s " % (statistics.median(data)))
print("Mode of the sample is % s " % (statistics.mode(data))) 
