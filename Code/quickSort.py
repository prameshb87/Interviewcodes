def quick_sort(a, low, high):

  def partition(l, h):
    pivot = a[l]
    i, j = l, h-1
    while i < j:
      while i < h and a[i] <= pivot:
        i+=1
      while j > l and a[j] > pivot:
        j-=1
      if i < j:
        a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

  if low < high:
    j = partition(low, high)
    quick_sort(a, low, j)
    quick_sort(a, j+1, high)
  return a



print(quick_sort([5,3,7,1,9,0,11,15,2], 0, 9))
# print(quick_sort([10,5,8,9,3,6,15,12,16,0], 0, 10))
