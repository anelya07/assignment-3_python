
#TASK 3 - A

print("=" * 30)

store_info = ("FreshMart", "Astana, Respublika Ave 1", "+7 700 0000000")
print(store_info[0])
print(store_info[1])
print(store_info[2])

print("=" * 30)

names = []
prices = []
check = True
#subtotal = 0

while check == True:
    name = input("Enter product name: ")
    if name == "done":
        check = False
    else:
        names.append(name)
        price = float(input("Enter price per unit (KZT): "))
        prices.append(price)
        #subtotal += price

print("-" * 30)
print(f"Your cart ({len(names)} items): ")
print("-" * 30)

for i in range(len(names)):
    print(f"{names[i]} - {prices[i]} KZT")

print("-" * 30)







