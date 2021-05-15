arr=[
    ("A",18,"nam"),
    ("K",15,"nu"),
    ("B",20,"nu"),
    ("P",61,"nam"),
]
#1
arr.sort(key=lambda x: x[0])
print(arr)
#2
arr.sort(key=lambda x: x[1])
print(arr)
#3
arr.sort(key=lambda x: x[2], reverse=True)
print(arr)
#4
def my_sort (item):
    if item[1]<=15:
        return item[1]
    elif item[1]>=60:
        return 1999-item[1]
    elif item[2]=="nu":
        return item[1]+3000
    else :
        return item[1]+4000
 arr.sort(key=lambda x: my_sort(arr))        
 print(arr)