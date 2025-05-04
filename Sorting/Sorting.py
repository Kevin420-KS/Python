import copy
import math

# Bubble Sort
def bubble_sort(arr):
    a = arr.copy()
    print("\n[ Bubble Sort ]")
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            print(f"Step {i}.{j}: {a}")
    return a

# Selection Sort
def selection_sort(arr):
    a = arr.copy()
    print("\n[ Selection Sort ]")
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Step {i}: {a}")
    return a

# Insertion Sort
def insertion_sort(arr):
    a = arr.copy()
    print("\n[ Insertion Sort ]")
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(f"Step {i}: {a}")
    return a

# Merge Sort
def merge_sort(arr):
    def merge(left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result

    def recursive_merge_sort(a, depth=0):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = recursive_merge_sort(a[:mid], depth+1)
        right = recursive_merge_sort(a[mid:], depth+1)
        merged = merge(left, right)
        print(f"Depth {depth}: {merged}")
        return merged

    print("\n[ Merge Sort ]")
    return recursive_merge_sort(arr.copy())

# Quick Sort
def quick_sort(arr):
    def recursive_quick_sort(a, depth=0):
        if len(a) <= 1:
            return a
        pivot = a[0]
        left = [x for x in a[1:] if x <= pivot]
        right = [x for x in a[1:] if x > pivot]
        print(f"Depth {depth}: Pivot={pivot}, Left={left}, Right={right}")
        return recursive_quick_sort(left, depth+1) + [pivot] + recursive_quick_sort(right, depth+1)

    print("\n[ Quick Sort ]")
    return recursive_quick_sort(arr.copy())

# Heap Sort
def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"Heapify at {i}: {arr}")
        heapify(arr, n, largest)

def heap_sort(arr):
    a = arr.copy()
    print("\n[ Heap Sort ]")
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        print(f"Extract max: {a}")
        heapify(a, i, 0)
    return a

# Counting Sort
def counting_sort(arr):
    a = arr.copy()
    print("\n[ Counting Sort ]")
    if not a:
        return []
    max_val = max(a)
    count = [0] * (max_val + 1)
    for num in a:
        count[num] += 1
    print(f"Count array: {count}")
    sorted_arr = []
    for i, c in enumerate(count):
        sorted_arr.extend([i] * c)
        if c > 0:
            print(f"Add {c} x {i}: {sorted_arr}")
    return sorted_arr

# Radix Sort
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    return output

def radix_sort(arr):
    a = arr.copy()
    print("\n[ Radix Sort ]")
    if not a:
        return []
    max_num = max(a)
    exp = 1
    while max_num // exp > 0:
        a = counting_sort_by_digit(a, exp)
        print(f"Digit {exp}: {a}")
        exp *= 10
    return a

# Bucket Sort
def bucket_sort(arr):
    a = arr.copy()
    print("\n[ Bucket Sort ]")
    if not a:
        return []
    max_val = max(a)
    size = max_val / len(a)
    buckets = [[] for _ in range(len(a))]
    for i in a:
        index = min(int(i / size), len(a)-1)
        buckets[index].append(i)
    for i, bucket in enumerate(buckets):
        buckets[i] = insertion_sort(bucket)
        print(f"Bucket {i} sorted: {buckets[i]}")
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result

# Menu
def tampilkan_menu():
    print("\nPilih jenis sorting yang diinginkan:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")
    print("7. Counting Sort")
    print("8. Radix Sort")
    print("9. Bucket Sort")

# Input Data
while True:
    try:
        n = int(input("Berapa banyak angka yang ingin diinput (minimal 3)? "))
        if n < 3:
            print("❌ Minimal 3 angka. Silakan coba lagi.")
            continue
        break
    except ValueError:
        print("❌ Masukkan angka bulat.")

data_awal = []
for i in range(n):
    while True:
        try:
            angka = int(input(f"Masukkan angka ke-{i+1}: "))
            data_awal.append(angka)
            break
        except ValueError:
            print("❌ Masukkan angka yang valid.")

# Program Utama
while True:
    data = copy.deepcopy(data_awal)
    tampilkan_menu()
    pilihan = input("Masukkan nomor pilihan (1-9): ")

    if pilihan == "1":
        hasil = bubble_sort(data)
        metode = "Bubble Sort"
    elif pilihan == "2":
        hasil = selection_sort(data)
        metode = "Selection Sort"
    elif pilihan == "3":
        hasil = insertion_sort(data)
        metode = "Insertion Sort"
    elif pilihan == "4":
        hasil = merge_sort(data)
        metode = "Merge Sort"
    elif pilihan == "5":
        hasil = quick_sort(data)
        metode = "Quick Sort"
    elif pilihan == "6":
        hasil = heap_sort(data)
        metode = "Heap Sort"
    elif pilihan == "7":
        hasil = counting_sort(data)
        metode = "Counting Sort"
    elif pilihan == "8":
        hasil = radix_sort(data)
        metode = "Radix Sort"
    elif pilihan == "9":
        hasil = bucket_sort(data)
        metode = "Bucket Sort"
    else:
        print("❌ Pilihan tidak valid.")
        continue

    print(f"\nData asli       : {data_awal}")
    print(f"Hasil {metode} : {hasil}")

    lanjut = input("\nIngin mencoba sorting lain? (y/n): ").lower()
    if lanjut != 'y':
        print("Program selesai. Terima kasih!")
        break
