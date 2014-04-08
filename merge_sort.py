def conquer(start,mid,end,unsorted_array):
    

def merge_sort(start,end,unsorted_array):    
    if(end-start) < 2:
        return;
    mid = (start+end)/2
    merge_sort(start,mid,unsorted_array)
    merge_sort(mid,end,unsorted_array)
    conquer(start,mid,end,unsorted_array)
