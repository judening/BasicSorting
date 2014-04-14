def quick_sort(teh_list,left,right):
    if (right-left) <=0:
         return
    else:
        start = left
        end = right
        pivot = start
        while start < end:
            
            while(teh_list[start] <= teh_list[pivot]) and start<end:
                start+=1
            while(teh_list[end] > teh_list[pivot]) and start<=end:
                end-=1
                
            if start < end:
                teh_list[start],teh_list[end] = teh_list[end] , teh_list[start]
        teh_list[pivot],teh_list[end] = teh_list[end], teh_list[pivot]        
        quick_sort(teh_list,left,end-1)
        quick_sort(teh_list,end+1,right)

def quicksort(teh_list):
    quick_sort(teh_list,0,len(teh_list)-1)
    print teh_list  
