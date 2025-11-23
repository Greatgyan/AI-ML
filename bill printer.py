print("------ MENU ------")
print("1. Pizza - 199")
print("2. Burger - 149")
print("3. Pasta - 199")
print("4. Fries - 139")
print("5. Cold Coffee - 149")
print("6. Soft Drink - 70")
print("7. Ice Cream - 50")
print("8. Water Bottle - 20")
print("9. Soda - 40")
print("------------------")

total = 0

while True:
        choice = input("Enter item number (0 to finish): ")

        try:
            choice = int(choice)
        except:
            print("Enter a valid number!")
            continue

        if choice == 0:
            break

        if choice == 1:
            price = 199

        elif choice == 2:
            price = 149

        elif choice == 3:
            price = 199

        elif choice == 4:
            price = 139

        elif choice == 5:
            price = 149

        elif choice == 6:
            price = 70

        elif choice == 7:
            price = 50

        elif choice == 8:
            price = 20

        elif choice == 9:
            price = 40
            
        else:
            print("Invalid item number!")
            continue
        
        q = int(input("Quantity: "))
        total += price * q
        print("Added!")

print("\nSubtotal =", total)
try:
        tax = float(input("Enter tax %: "))
except:
        tax = 0

tax_amt = (tax / 100) * total
grand_total = total + tax_amt

print("\n------ BILL ------")
print(f"Subtotal: {total}")
print(f"Tax: {tax_amt:.2f}")
print(f"Total: {grand_total:.2f}")
print("------------------")

