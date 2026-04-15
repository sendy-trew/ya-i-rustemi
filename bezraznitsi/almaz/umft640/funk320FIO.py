import random
def funk320FIO(n, k):
    n = int(input("Введите n: "))
    k = int(input("Введите k: "))
    arr = []
    for i in range(k):
        arr.append(random.randint(1, n))
    return arr
