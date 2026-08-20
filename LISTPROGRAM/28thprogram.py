scores = []

for i in range(10):
    run = int(input("Enter score: "))
    scores.append(run)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

century = 0
half_century = 0

for score in scores:
    if score >= 100:
        century += 1
    elif score >= 50:
        half_century += 1

print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half-Centuries:", half_century)