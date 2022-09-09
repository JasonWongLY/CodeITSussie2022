from itertools import groupby


# function for to_cumulative()
def gather(x):
    return_list = [x[0][0][0]]
    quantity = 0
    notional = 0
    for i in x:
        for j in i:
            quantity += int(j[2])
            notional += float(j[2]) * float(j[3])
        return_list.append(j[1])
        return_list.append(str(quantity))
        return_list.append(str(notional))
        quantity = 0
        notional = 0
    return ",".join(return_list)


# function for to_cumulative_delayed
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


def to_cumulative(stream: list):
    stream.sort()
    stream = [i.split(',') for i in stream]
    key_func = lambda x: x[0]
    tick_func = lambda x: x[1]
    x = [list(j) for i, j in groupby(stream, key_func)]
    y = [[list(j) for i, j in groupby(idx, tick_func)] for idx in x]
    return_list = []
    for i in y:
        return_list.append(gather(i))
    return return_list


def to_cumulative_delayed(stream: list, quantity_block: int):
    return_list = []
    stream = [i.split(',') for i in stream]
    tick_func = lambda x: x[1]
    x = [list(j) for i, j in groupby(stream, tick_func)]
    for i in x:
      i.sort()
      return_list.append(sum(i,quantity_block))
    return_list.sort()
    return_list=[item for l in return_list for item in l]  
    return return_list
