from itertools import groupby
# def sum(x):
    # return_list=[x[0][0],x[0][1],0,0]
    # for i in x:
    #     return_list[2]+=int(i[2])
    #     return_list[3]+=float(i[2])*float(i[3])
    # return return_list

def sum(x):
    return_list=[x[0][0][0]]
    quantity=0
    notional=0
    for i in x:
        for j in i:
            quantity+=int(j[2])
            notional+=float(j[2])*float(j[3])
        return_list.append(j[1])
        return_list.append(j[2])
        return_list.append(j[3])
        quantity=0
        notional=0
    return ",".join(return_list)

def to_cumulative(str):
    str.sort()
    str=[i.split(',') for i in str]
    key_func=lambda x:x[0]
    tick_func=lambda x:x[1]
    x=[list(j) for i,j in groupby(str,key_func)]
    y=[[list(j) for i,j in groupby(idx,tick_func)] for idx in x]
    return_list=[]
    for i in y:
        return_list.append(sum(i))
    return return_list

test=["00:06,A,1,5.6","00:05,A,1,5.6","00:00,A,1,5.6","00:00,A,2,4.5","00:00,B,1,2.7","00:02,A,1,5.6","00:03,A,1,5.6","00:04,A,1,5.6"]
print(to_cumulative(test))
