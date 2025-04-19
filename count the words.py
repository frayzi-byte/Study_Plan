with open("C:\\Users\\andre\\Downloads\\Новая папка\\HZ.txt") as file:
    TEXT = file.read()
    words = TEXT.split()
    word_count = len(words)
    print(word_count)