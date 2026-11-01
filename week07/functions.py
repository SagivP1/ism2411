#Reflection Questions

#1. I caught a basic IndentationError right away just by reading the error message traceback. It shows my tech 
# instincts are pretty solid since I looked at the logs first instead of just staring at the code blindly.

#2. You basically give it a price and a membership rank, and it spits back the new cheaper price after the discount.
#A friend could totally drop it right into their code and use it without needing to know how it works inside.

#3. The AI definitely helped me actually learn because I only used it to explain what the errors meant

# Exercise 1

def calculate_tax(price, rate):
    return price * rate

#calling the function 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(50, 0.05):.2f}")

#Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85  # 20% discount
    elif tier == "silver":
        return price * 0.90  # 10% discount
    elif tier == "bronze":
        return price * 0.95  # 5% discount
    else:
        return price  # no discount



    price = 200
    tiers = ["gold", "silver", "bronze", "none"]

    for tier in tiers:
        print(f"{tier}: ${apply_discount(price, tier):.2f}")

#Exercise 3


discount = apply_discount(200, "gold")
tax = calculate_tax(discount, 0.07)
after_tax = discount + tax
print(f"After gold discount: ${after_tax:.2f}")
print(f"After tax: ${tax:.2f}")



def final_price(price, tier, tax_rate):
    discount = apply_discount(price, tier)
    tax = calculate_tax(discount, tax_rate)
    return discount + tax


print(f"Final price ${final_price(200, 'gold', 0.07):.2f}")


#Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


#Exercise 6

# Scope: a variable created inside a function is local, so it only exists
# while that function runs. Assigning x = 999 inside double_it() makes a new
# local x and does not touch the global x = 100 outside the function.

x = 100   # global variable

def double_it():
    x = 999   # local variable, different from global x
    return x * 2

print(x)           # prints 100
print(double_it()) # prints 1998 (local x is 999, doubled)
print(x)           # prints 100, the global x never changed
