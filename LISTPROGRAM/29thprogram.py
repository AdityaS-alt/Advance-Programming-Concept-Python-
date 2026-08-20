temperature = []

for i in range(30):
    temp = float(input("Enter temperature: "))
    temperature.append(temp)

highest = max(temperature)
lowest = min(temperature)
average = sum(temperature) / len(temperature)

above = 0
below = 0

for temp in temperature:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest Temperature:", highest)
print("Coldest Temperature:", lowest)
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)