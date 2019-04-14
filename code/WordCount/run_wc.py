import os
import sys
import time


start = time.time()
os.system('python wordcount_simple.py ' + 'File1ForLab3.txt' + ' simpleWC_dir')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the program to sort: ", timeTaken)
