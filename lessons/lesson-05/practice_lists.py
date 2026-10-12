# Lesson 5, Part A: lists and loops (plain Python - no browser!)
# Read it first. Guess what each print() will show. Then run it.

prices = []

print(prices)
print(len(prices))
#print(prices[0])

for price in prices:
    print("Checking:", price)

numbers = []
for price in prices:
    number = float(price.replace("$", ""))
    numbers.append(number)

print(numbers)
print(numbers == sorted(numbers))
