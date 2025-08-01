def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option(1-4): ")
        if choice == "1":
            item = input("Enter the item to add: ")
            if item:
                shopping_list.append(item)
                print(f"Added '{item}' to the shopping list.")
            else:
                print("Invalid input. Item cannot be empty.")
        elif choice == "2":
            item = input("Enter an item to remove: ")
            if item:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print("Invalid input. Item cannot be empty.")
        elif choice == "3":
            if shopping_list:
                print("\nView Current Shopping List::")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()