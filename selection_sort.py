def selection_sort(unsorted_array):
    for i in range(len(unsorted_array)):
        min = i
        for j in range(i+1,len(unsorted_array)):
            if unsorted_array[j] < unsorted_array[i]:
                min = j
        
        temp = unsorted_array[i]
        unsorted_array[i] = unsorted_array[min]
        unsorted_array[min] = temp
    print unsorted_array
