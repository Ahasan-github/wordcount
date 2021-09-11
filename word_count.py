import fileinput
import time

start_time= time.time()
wordcount= ''
files = fileinput.input()
for line in files:
 if fileinput.filelineno():
  wordcount = wordcount + line
  words = wordcount.split()
  #print(words)
  count = {}
  for word in words:
   if word in count:
    count[word] = count[word] + 1
   else:
    count[word] = 1
    #print(count)

print(' -> ' + wordcount, end='')
print(count)
print("\n")
print("Time taken by program \n ")
print("--- %s seconds ---" % (time.time() - start_time))

