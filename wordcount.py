file=open("D:\python-mapreduce-examples-master\python-mapreduce-examples-master\count_and_sum\emp.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print (k , v)
