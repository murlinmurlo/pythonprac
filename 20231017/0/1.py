import timeit

snippet = input()

t = timeit.Timer(stmt=snippet)
number, time_taken = t.autorange()

print(f"Количество итераций: {number}")
print(f"Время выполнения: {time_taken} секунд")
