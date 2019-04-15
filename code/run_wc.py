import os
import sys
import time

print("----------------File1ForLab3.txt----------------\n")

start = time.time()
os.system('python wordcount_simple.py ' + 'File1ForLab3.txt' + ' simpleWC_dir')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the WordCount: ", timeTaken)

print("")

start = time.time()
os.system('python3 TopKQuery.py ' + 'File1ForLab3.txt' + ' outputDir')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the TopKQuery: ", timeTaken)


print("")

start = time.time()
os.system('python WordIndex.py ' + 'File1ForLab3.txt' + ' simpleWC_dir')
end =time.time()
timeTaken = (end-start)
print("Time Taken for WordIndex: ", timeTaken)

print("")

print("----------------File1ForLab3.txt----------------\n")
start = time.time()
os.system('python wordcount_simple.py ' + 'File2ForLab3.txt' + ' simpleWC_dir')
end =time.time()
timeTaken = (end-start)
print("Time Taken for the WordCount: ", timeTaken)

print("")
start = time.time()
os.system('python WordIndex.py ' + 'File2ForLab3.txt' + ' simpleWC_dir')
end =time.time()
timeTaken = (end-start)
print("Time Taken for WordIndex: ", timeTaken)

print("")


