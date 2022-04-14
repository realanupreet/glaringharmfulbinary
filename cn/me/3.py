a=[3,5,78,9,4,7,3,2]


def bubble(list_a):
    ilen = len(list_a)-1
    sorted=False
    while not sorted:
        sorted = True
        for i in range(0,ilen):
            if list_a[i]>list_a[i+1]:
                sorted=False
                temp=list_a[i]
                list_a[i]=list_a[i+1]
                list_a[i+1]=temp
    return list_a
a=[3,567,78,4,3,63,2,5,65,74,8]
print(bubble(a))

