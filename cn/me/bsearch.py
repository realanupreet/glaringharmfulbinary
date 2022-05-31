# binary search example of divide and conquer technique


def binary(list, val):
    list_size = len(list)-1
    idx0=0
    idxn=list_size
    while idx0 <= idxn:
        midval=(idx0+idxn)//2
        if list[midval]==val:
            return midval
    if val>list[midval]:
        idx0=midval+1
    else:
        idxn=midval-1
    if idx0 > idxn:
        return None

list=[2,4,5,6,7]
print(binary(list,67))