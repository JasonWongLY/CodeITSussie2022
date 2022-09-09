from itertools import groupby
import math

def sum(x,num):
    return_list = []
    quantity=0
    notional=0
    for i in x:
        quantity += int(i[2])
        if quantity <num :
            notional += float(i[2])*float(i[3])
        elif quantity >=num:
            quantity-=num
            notional += (float(i[2])-quantity)*float(i[3])
            return_string="{},{},{},{}".format(i[0],i[1],num,notional)
            return_list.append(return_string)
    return return_list

# def sum(x):
#     return_list = [x[-1][0]]
#     quantity = 0
#     notional = 0
#     for i in x:
#         quantity += int(i[2])
#         notional += float(i[2]) * float(i[3])
#     return_list.append(x[-1][1])
#     return_list.append(str(quantity))
#     return_list.append(str(round(notional, 1)))
#     return ",".join(return_list)

# def to_cumulative_delayed(str,num):
#     return_list=[]
#     str=[i.split(',') for i in str]
#     key_func=lambda x:x[0]
#     tick_func=lambda x:x[1]
#     x=[list(j) for i,j in groupby(str,tick_func)]
#     print(x)
#     for i,j in enumerate(x):
#         j.sort()
#         idx=len(j)%num
#         x[i]=j[:len(j)-idx]
#     for i in x:
#         for k in [i[j:j+num] for j in range(0,len(i),num)]:
#             return_list.append(sum(k))
#     return return_list

def to_cumulative_delayed(str,num):
    return_list=[]
    str=[i.split(',') for i in str]
    key_func=lambda x:x[0]
    tick_func=lambda x:x[1]
    x=[list(j) for i,j in groupby(str,tick_func)]

    for i in x:
        i.sort()
        return_list.append(sum(i,num))
    return_list.sort()
    return return_list

test=[
      '00:01,A,5,5.5',
      '00:00,A,4,5.6',
      '00:00,B,5,5.5',
      '00:02,B,4,5.6',
      ]
print(to_cumulative_delayed(test,5))


