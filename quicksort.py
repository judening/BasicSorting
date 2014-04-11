import random

def quick_sort(teh_list,split):
    if len(teh_list) <=1:
         return
    else:
        start = 0
        end = split
        pivot = random.ranint(start,end)
        while start < end:
            
            while(teh_list[start] < teh_list[pivot]):
                start+=1
            while(teh_list[end] > teh_list[pivot]):
                end-=1
                
            if start< end:
                temp = teh_list[start]
                teh_list[start] = teh_list[end]
                teh_list[end] = temp
                
        quick_sort(teh_list[])
        quick_sort(teh_list[pivot:])
        
