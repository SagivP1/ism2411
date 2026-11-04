print("---Exercise 1--- ")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spent": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spent"])
print(customer)

print("---Exercise 2---")
customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print("---Exercise 3---")

print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as e:
    print("KeyError Caught:", e)

print("---Exercise 4---")
for key, value in customer.items():
    print(f"{key}: {value}")

# Iterating without .items() only yields the keys, not the values.
# .items() yields (key, value) pairs, so we can unpack both in the loop.

for key in customer:
    print(key)

print("---Exercise 5---")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
rate = tier_discounts.get(customer["tier"], 0)
price = 200
final_price = price * (1 - rate)
print(f"Tier: {customer['tier']} | Discount: {rate:.0%} | Final price: ${final_price:.2f}")

print("---Exercise 6---")
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Carol", "tier": "bronze"},
    {"name": "Dave", "tier": "gold"},
]
for record in customers:
    discount = 300 * tier_discounts.get(record["tier"], 0)
    print(f"{record['name']} ({record['tier']}): discount ${discount:.2f} on $300")

print("---Exercise 7---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} ({info['stock']} left)")

print("---Exercise 8---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
summary = {}
for t in transactions:
    summary[t["region"]] = summary.get(t["region"], 0) + t["amount"]
for region in sorted(summary):
    print(f"{region}: {summary[region]}")

#Reflection:

#1.I'd use .get() when the key might not be there, like an optional field such as a customer's email, so the program 
#doesn't crash. I'd use bracket notation when the key has to exist, because then a KeyError tells me something is wrong
#with the data.

#2. It reminds me of a pivot table or a SUMIF in Excel, where you add up totals for each category. The Python version is
#more useful for large datasets because it can handle huge files that would slow down or crash Excel, and I can rerun
#the same code on new data without redoing the steps by hand.
