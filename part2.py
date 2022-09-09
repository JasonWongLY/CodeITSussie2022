from itertools import groupby
def to_cumulative_delayed(str,num):
    # str.sort()
    # str[:,num-index]
    str=[i.split(',') for i in str]
    key_func=lambda x:x[0]
    tick_func=lambda x:x[1]
    x=[list(j) for i,j in groupby(str,tick_func)]
    for i,j in enumerate(x):
        j.sort()
        idx=len(j)%num
        x[i]=j[:len(j)-idx]
        
    print(x)

test=['00:06,A,1,5.6','00:05,A,1,5.6','00:00,A,1,5.6','00:02,A,1,5.6','00:03,A,1,5.6','00:04,A,1,5.6','00:06,B,1,5.6','00:05,B,1,5.6','00:00,B,1,5.6','00:02,B,1,5.6','00:03,B,1,5.6','00:04,B,1,5.6']
to_cumulative_delayed(test,5)