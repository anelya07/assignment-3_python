
#TASK 3 - A

customer = input("Enter customer name: ")
check = True
count = 0
subtotal = 0

while check == True:
    product = input("Enter product name: ")
    if product == "done":
        check = False
    else:
        price = float(input("Enter price per unit (KZT): "))
        count = count + 1
        subtotal += price

print("=" * 30)
print("         SHOP RECEIPT")
print("=" * 30)

print(f"Customer: {customer.upper()}")
print(f"Items: {count}")
print(f"Subtotal: {subtotal}" + " KZT")

print("-" * 30)

if subtotal < 3000:
    discount = 0.0
    total = subtotal
    print("Discount tier: No discount")
    print(f"Discount: {discount}" + " KZT")
    print(f"Total: {subtotal}" + " KZT")

elif subtotal >= 3000 and subtotal < 7000:
    discount = subtotal * 0.05
    total = subtotal - discount
    print("Discount tier: 5% discount")
    print(f"Discount: {discount}" + " KZT")
    print(f"Total: {total}" + " KZT")
else:
    discount = subtotal * 0.15
    total = subtotal - discount
    print("Discount tier: 15% discount")
    print(f"Discount: {discount}" + " KZT")
    print(f"Total: {total}" + " KZT")


print("-" * 30)
print("Name uppercase: ", customer.upper())
print("Name lowercase: ", customer.lower())
print("Name length: ", len(customer))
if len(customer) > 5:
    print("Long name")
else:
    print("Short name")
print("=" * 30)
