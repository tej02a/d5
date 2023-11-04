import random

def partition_left(arr, low, high):
  pivot = arr[high]
  i = low
  for j in range(low, high):
    if arr[j] <= pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
  arr[i], arr[high] = arr[high], arr[i]
  return i

def partition_right(arr, low, high):
  r = random.randint(low, high)
  arr[r], arr[high] = arr[high], arr[r]
  return partition_left(arr, low, high)

def quicksort(arr, low, high):
  if low < high:
    p = partition_right(arr, low, high)
    quicksort(arr, low, p - 1)
    quicksort(arr, p + 1, high)

def print_array(arr):
  for item in arr:
    print(item, end=" ")
  print()

if __name__ == "__main__":
  arr = [6, 4, 12, 8, 15, 16]
  n = len(arr)

  print("Original array:", end=" ")
  print_array(arr)

  quicksort(arr, 0, n - 1)

  print("Sorted array:", end=" ")
  print_array(arr)


def partition(arr, low, high):
  pivot = arr[(low + high) // 2]
  i = low - 1
  j = high + 1

  while True:
    i += 1
    while arr[i] < pivot:
      i += 1

    j -= 1
    while arr[j] > pivot:
      j -= 1

    if i >= j:
      return j

    arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr, low, high):
  if low < high:
    pivot_index = partition(arr, low, high)
    quicksort(arr, low, pivot_index)
    quicksort(arr, pivot_index + 1, high)

if __name__ == "__main__":
  arr = [12, 4, 5, 6, 7, 3, 1, 15, 8, 9, 2, 10]

  print("Original array:", end=" ")
  for num in arr:
    print(num, end=" ")
  print()

  quicksort(arr, 0, len(arr) - 1)

  print("Sorted array:", end=" ")
  for num in arr:
    print(num, end=" ")
  print()