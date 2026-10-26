import json
import sys


def create_task(title: str, tasks: list) -> list:
    if not title or not title.strip():
        raise ValueError("Название задачи не может быть пустым")
    tasks.append({"title": title.strip(), "done": False})
    return tasks


def list_tasks(tasks: list) -> None:
    if not tasks:
        print("Список задач пуст.")
        return
    for i, task in enumerate(tasks, 1):
        status = "выполнена" if task["done"] else "не выполнена"
        print(f"{i}. {task['title']} — {status}")


def main():
    tasks = []
    print("Менеджер задач")
    print("Команды: add <название>, list, exit")
    while True:
        try:
            command = input("> ").strip()
        except EOFError:
            break
        if command == "exit":
            break
        if command.startswith("add "):
            title = command[4:]
            try:
                create_task(title, tasks)
                print(f"Задача «{title}» добавлена.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif command == "list":
            list_tasks(tasks)
        elif command:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()

if True
    pass