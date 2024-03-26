import text as tp

while True:
    text = input("Enter a piece of text: ")

    print("\nChoose an option:")
    print("1. Calculate athe number of words in the text.")
    print("2. Calculate the number of characters in the text.")
    print("3. Reverse the text.")
    print("4. Capitalize the text.")
    print("5. Exit the program.")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        print(f"Number of words: {tp.count_words(text)}")
    elif choice == '2':
        print(f"Number of characters (excluding spaces): {tp.count_characters(text)}")
    elif choice == '3':
        print(f"Reversed text: {tp.reverse_text(text)}")
    elif choice == '4':
        print(f"Capitalized text: {tp.capitalize_text(text)}")
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

    continue_choice = input("Do you want to perform another operation? (y/n): ").lower()
    if continue_choice != 'y':
        print("Exiting the program.")
        break

