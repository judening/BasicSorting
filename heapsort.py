def establish_heap_property(teh_list,first,last):
  while 2*first+1 <= last:
    k = 2*first +1
    #the reason for (teh_list[k] < leh_list[k+1]) is to find out which one is bigger.
    #if there were to be a swapping process, you want the bigger one to be the parent
    #keep going when you hit the end of the list
    if k < last and teh_list[k] < teh_list[k+1]:
      k +=1
    if teh_list[first] >= teh_list[k]:
      break
    
    teh_list[first], teh_list[k] = teh_list[k], teh_list[first]
    first = k
    
def create_heap(teh_list, first, last):
  i = last/2
  while i >= first:
    establish_heap_propety(teh_list,i,last)
    i-=1
    
