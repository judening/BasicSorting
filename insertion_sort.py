def insertion_sort(unsorted_array):
    for i in range(len(unsorted_array)):
        for j in range(i):
            if unsorted_array[j] > unsorted_array[i]:
                temp = unsorted_array[i]
                unsorted_array[i] = unsorted_array[j]
                unsorted_array[j] = temp
            
    print unsorted_array

insertion_sort([9,8,4,3,2,3,7,6,5,4,3,2,1])
