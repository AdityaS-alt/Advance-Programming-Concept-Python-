numbers = [10, 20, 10, 30, 20, 10, 40, 30]

visited = []

for i in numbers:
    if i not in visited:
        count = 0
        for j in numbers:
            if i == j:
                count += 1
        print(i, "appears", count, "times")
        visited.append(i)