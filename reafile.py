file_path = r"C:\Users\Jhonatan\Documents\teste_python.txt"

while True:
    print("\nChoose an option:")
    print("1 - Read file contents")
    print("2 - Write to file")
    print("3 - Delete a line from the file")
    print("4 - Exit")

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
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            if not lines:
                print("The file is empty.")
                continue

            print("\n--- File Lines ---")
            for i, line in enumerate(lines, start=1):
                print(f"{i}: {line.strip()}")

            line_number = input("Enter the line number you want to delete: ").strip()

            if not line_number.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            index = int(line_number) - 1

            if index < 0 or index >= len(lines):
                print("Line number out of range.")
                continue

            removed_line = lines.pop(index)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)

            print(f"Line deleted successfully: {removed_line.strip()}")

        except FileNotFoundError:
            print("File not found. Check the path.")

    elif choice == '4':
        print("Leaving... See you soon!")
        break
    
    else:
        print("Invalid option. Please try again.")
