#Reflection Questions 

#1.The most surprising thing was that lists can change after you make them, so you can append, remove, and sort without
#  making a new list. I also didn't expect negative indexes like inventory[-1] to be a thing, because that makes grabbing
#  the last item way easier.

#2.In a class project, I could have used a list of weekly sales numbers instead of retyping formulas in Excel every
#  time the data changed. With a list I could use sum(), len(), max(), and min() in one line each and just rerun the
#  file when I add a new number.



print("--- Exercise 1: Build the list ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


print("--- Exercise 2: Index Practice ---")

print(inventory[0])                     # first item
print(inventory[-1])                    # last item
print(inventory[len(inventory) // 2])   # middle item, computed from the length
middle = len(inventory) // 2
print(inventory[middle])

print("--- Exercise 3: Slicing Practice ---")

print(inventory[:3])    # first three items
print(inventory[-2:])   # last two items
print(inventory[::2])   # every other item


print("--- Exercise 4: Modifying the list ---")

inventory.append("envelope")
print(f"After append: {inventory}")

inventory.remove("tape")
print(f"After remove: {inventory}")

inventory.sort()
print(f"After sort: {inventory}")


print("--- Exercise 5: Tuple Comparison ---")

coords = (40.7128, -74.0060)   # NYC

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("--- Exercise 6: Average of List of Sales ---")

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")


print("--- Exercise 7: Accumilator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * .9, 2))   # 10% off

print(f"Original: {prices}")
print(f"Discounted: {discounted}")


print("--- Exercise 8: Filter above Threshold ---")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(f"High sales: {high_sales}")
print(f"Count: {len(high_sales)}")
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")
