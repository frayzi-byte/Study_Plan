file_path = r"c:\Users\andre\OneDrive\Изображения\Документы\programming\Новая папка\HZ.txt"
while True:
    print("\nChoose an option:")
    print("1 - Read file contents")
    print("2 - Write to file")
    print("3 - Exit")

    choice = input("Enter option number: ").strip()

    if choice == '1':
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print("\n--- File Contents ---")
                print(content if content else "[Empty file]")
        except FileNotFoundError:
            print("File not found. Check the path.")

    elif choice == '2':
        text = input("Enter the text you want to add to the file: ").strip()
        if text:
            try:
                with open(file_path, 'a', encoding='utf-8') as file:
                    file.write(text + '\n')
                print("Text added successfully!")
            except FileNotFoundError:
                print("File not found. Check the path.")
        else:
            print("Empty text. Nothing was written.")

    elif choice == '3':
        print("Leaving... See you soon!")
        break

    else:
        print("Invalid option. Please try again.")