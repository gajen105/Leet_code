def merge(li1,li2):
    n1,n2 = len(li1),len(li2)
    i,j=0,0
    li=[]
    while i<n1 and j<n2:
        if li1[i]<li2[j]:
            li.append(li1[i])
            i+=1
        else:
            li.append(li2[j])
            j+=1
    if i<n1:
        li.extend(li1[i:])
    if j<n2:
        li.extend(li2[j:])
    return li
def mergeSort(li):
    if len(li)<=1:
        return li
    n = len(li)
    mid = n//2
    left = mergeSort(li[:mid])
    right = mergeSort(li[mid:])
    li = merge(left,right)
    return li
nums =[50,20,30,60,10,22,11,25,37,-1,33,4,3,5,3,5,23,5,655]
print(mergeSort(nums))