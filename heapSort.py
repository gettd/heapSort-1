import numpy as np

def heapSort(A):
  n = len(A)
  buildMaxHeap(A)
  for i in range(n-1, 0, -1): #one by one extract element
      A[0], A[i] = A[i], A[0] #swap
      heapify(A, 0, i) #max heapify to make it max heap again

def buildMaxHeap(A): #create initial max heap from array
  n = len(A)
  for i in range(n//2, -1, -1):#start from last non leaf node and work up (non leaf node is parent of leaf node)
    percolateUp(A, i)

def percolateUp(A, i): #sort array by percolating up, making largest int be at top
  while i > 0:
    parent = (i-1)//2 
    if A[parent] < A[i]:#if child larger than parent, swap
      A[parent], A[i] = A[i], A[parent]
      i = parent #move to parent
    else:
      break #stop when parent is larger than child

def heapify(A, i, n):
  largest = i #initialize largest as current root
  left = 2*i + 1 #left child 
  right = 2*i + 2 #right child
  if left < n and A[left] > A[largest]: #if left child is larger than root
    largest = left
  if right < n and A[right] > A[largest]:#if right child is larger than root
    largest = right
  if largest != i: #if largest is not root
    A[i], A[largest] = A[largest], A[i]
    heapify(A, largest, n) #do again if largest is not root
  

A = np.random.randint(0,100,size=(10)).tolist()
print("unsorted array: ", A)
heapSort(A)
n = len(A)
print("sorted array: ", A)

