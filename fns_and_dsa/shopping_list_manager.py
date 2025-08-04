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
        choice = input("Enter your choice: ")

        if choice == '1':
            item = str(input("Please enter the item name: "))
            print(shopping_list.append(item))
            print(f"{item} has been added!")
        elif choice == '2':
            item = str(input("Please enter the item name: "))
            if item not in shopping_list:
                print(f"The item '{item}' is not in your shopping list!")
            else:
                print(shopping_list.remove(item))
                print(f"{item} has been removed!")
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()