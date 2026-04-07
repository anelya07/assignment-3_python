
#TASK 3 - A

print("=" * 30)
store_info = ("FreshMart", "Astana, Respublika Ave 1", "+7 700 000 0000")
print(store_info[0])
print(store_info[1])
print(store_info[2])
print("=" * 30)

weekly_products = set()
names = []
prices = []
check = True

while check == True:
    name = input("Enter product name (or 'done' to finish): ")
    if name == "done":
        check = False
    else:
        names.append(name)
        price = float(input("Enter price per unit (KZT): "))
        prices.append(price)

print("-" * 30)
print(f"Your cart ({len(names)} items): ")
print("-" * 30)

for i in range(len(names)):
    print(f"{names[i]} - {prices[i]} KZT")
print("-" * 30)

check = True
while check == True:
    unique_name = input("Enter product name (or 'done' to finish): ")
    if unique_name == "done":
        check = False
    else:
        weekly_products.add(unique_name)
print(f"Unique products: {len(weekly_products)}")
print(weekly_products)

customer = input("Enter customer name: ")
receipt = {"customer": customer, "items": len(names), "subtotal": sum(prices), "discount": 0.0, "total": 0.0}

print("=" * 30)
print("RECEIPT - FreshMart")
print("=" * 30)
print("Customer: ", receipt["customer"])
print("Items: ", receipt["items"])
print("-" * 30)
for i in range(receipt["items"]):
    print(f"{names[i]} - {prices[i]} KZT")
print("-" * 30)

if receipt["subtotal"] < 3000:
    receipt["total"] = receipt["subtotal"]
    print(f'Subtotal: {receipt["subtotal"]}')
    print(f'Discount: {receipt["discount"]} KZT (No discount)')
    print(f'Total: {receipt["total"]} KZT')

elif receipt["subtotal"] >= 3000 and receipt["subtotal"] < 7000:
    receipt["discount"] = receipt["subtotal"] * 0.05
    receipt["total"] = receipt["subtotal"] - receipt["discount"]
    print(f'Subtotal: {receipt["subtotal"]}')
    print(f'Discount: {receipt["discount"]} KZT (Standard discount)')
    print(f'Total: {receipt["total"]} KZT')

else:
    receipt["discount"] = receipt["subtotal"] * 0.15
    receipt["total"] = receipt["subtotal"] - receipt["discount"]
    print(f'Subtotal: {receipt["subtotal"]}')
    print(f'Discount: {receipt["discount"]} KZT (Premium discount)')
    print(f'Total: {receipt["total"]} KZT')

print("=" * 30)

