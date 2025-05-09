tasks = []

def add_task():
    task_new = input("Введите задачу, которую хотите добавить: ")
    tasks.append(task_new)

def read_task():
    print("Список задач:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def sort_task():
    tasks.sort()
    print("Задачи отсортированы.")

def del_task():
    read_task()
    what = input("Введите точное название задачи для удаления: ")
    if what in tasks:
        tasks.remove(what)
        print("Задача удалена.")
    else:
        print("Задача не найдена.")

print("Список задач:\n--1. Посмотреть список задач\n--2. Добавить новую задачу\n--3. Сортировать задачи\n--4. Удалить задачу\n--0. Выйти")

while True:
    menu = input("Выберите задачу, введя ее номер: ")
    
    match menu:
        case "1":
            read_task()
        case "2":
            add_task()
        case "3":
            sort_task()
        case "4":
            del_task()
        case "0":
            print("Выход из программы.")
            break
        case _:
            print("Неверный ввод.")