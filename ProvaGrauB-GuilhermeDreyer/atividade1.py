import random

def shuffle_array(arr):
    n = len(arr)
    for _ in range(n):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def ImprimirArray(arr):
    print(' '.join(arr))

if __name__ == "__main__":
    array = ['a', 'b', 'c', 'd', 'e']
    print("Array inicial:")
    ImprimirArray(array)
    
    ArrayEmbaralhado = shuffle_array(array)
    print("Array embaralhado:")
    ImprimirArray(ArrayEmbaralhado)
