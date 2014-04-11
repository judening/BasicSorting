import random

def quick_sort(teh_list,left,right):
    if (right-left) <=0:
         return
    else:
        start = left
        end = right
        pivot = (right+left)/2
        while start < end:
            
            while(teh_list[start] < teh_list[pivot]):
                start+=1
            while(teh_list[end] > teh_list[pivot]):
                end-=1
                
            if start< end:
                temp = teh_list[start]
                teh_list[start] = teh_list[end]
                teh_list[end] = temp
                
        quick_sort(teh_list,left,pivot)
        quick_sort(teh_list,pivot+1,right)

def quicksort(teh_list):
    quick_sort(teh_list,0,len(teh_list)-1)
    print teh_list    
        
