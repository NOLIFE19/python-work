# ონლაინ მაღაზიის ინვენტარისა და მომხმარებლების ანალიზატორი

inventory = {
    "laptop": {"price": 2500, "stock": 5, "release": 2026},
    "phone": {"price": 1200, "stock": 10, "release": 2026},
    "tablet": {"price": 800, "stock": 7, "release": 2025}
}

# 1. პროდუქტის დამატება ან რაოდენობის განახლება
while True:
    print("1. Add new product")
    print("2. Update product stock")
    print("3. Finish")

    user = input("Choose option: ")

    if user == "1":
        try:
            name = input("Enter product name: ").strip().lower()

            if name in inventory:
                print("Product already exists!")
                continue

            price = int(input("Enter price: "))
            stock = int(input("Enter stock: "))
            release = int(input("Enter release year: "))

            if price <= 0 or stock < 0 or release <= 0:
                print("Enter correct data!")
                continue

            inventory[name] = {
                "price": price,
                "stock": stock,
                "release": release
            }

            print("Product added successfully!")

        except ValueError:
                    print("Enter correct numeric data!")

    elif user == "2":
        name = input("Enter product name: ").strip().lower()

        if name in inventory:
            try:
                stock = int(input("Enter new stock: "))

                if stock < 0:
                    print("Stock cannot be negative!")
                else:
                    inventory[name]["stock"] = stock
                    print("Stock updated successfully!")

            except ValueError:
                print("Enter a valid number!")

        else:
            print("Product not found!")

    elif user == "3":
        break

    else:
        print("Invalid option!")
print("\n--- FULL INVENTORY ---")

for name, details in inventory.items():
    print(
        f"Product: {name} | "
        f"Price: {details['price']} GEL | "
        f"Stock: {details['stock']} | "
        f"Release: {details['release']}"
    )


total_value = 0

for details in inventory.values():
    total_value += details["price"] * details["stock"]

print("\nTotal inventory value:", total_value, "GEL")


print("\n--- PRODUCTS IN STOCK ---")

for name, details in inventory.items():
    if details["stock"] > 0:
        print(name, "-", details["stock"], "units")



if inventory:
    most_expensive = max(
        inventory,
        key=lambda name: inventory[name]["price"]
    )

    print("\nMost expensive product:", most_expensive)
    print("Price:", inventory[most_expensive]["price"], "GEL")


active_users = {"jeff@gmail.com", "gio@gmail.com", "mariam@gmail.com"}
vip_users = {"ivaniSvili@gmail.com", "bezos@gmail.com", "giorgi@gmail.com"}

all_users = active_users | vip_users
active_vips = active_users & vip_users
active_non_vips = active_users - vip_users

print("\n--- USER ANALYTICS ---")

print("All unique users:", all_users)
print("Active VIP users:", active_vips)
print("Active non-VIP users:", active_non_vips)
