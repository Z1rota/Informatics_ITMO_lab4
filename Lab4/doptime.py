import time

main, dopsa1, dopsa2, dopsa3 = 0, 0, 0, 0

start_time = time.perf_counter()
for i in range(100):
    import task1
end_time = time.perf_counter()

main = end_time - start_time

start_time = time.perf_counter()
for i in range(100):
    import task3
end_time = time.perf_counter()

dopsa1 = end_time - start_time

start_time = time.perf_counter()
for i in range(100):
    import task4
end_time = time.perf_counter()

dopsa2 = end_time - start_time

start_time = time.perf_counter()
for i in range(100):
    import task5
end_time = time.perf_counter()

dopsa3 = end_time - start_time


print("\n\n\n\n\n\n\n")

print(f"Основное задание - {main}")

print(f"Дополнительное задание 1 - {dopsa1}")

print(f"Дополнительное задание 2 - {dopsa2} ")

print(f"Дополнительное задание 3 - {dopsa3} ")