from library import Library


def main():
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("0. Выход")

        choice = input("Выберите действие: ")
        match choice:
            case "1":
                title = input("Введите название: ")
                author = input("Введите автора: ")
                year = int(input("Введите год издания: "))
                library.add_book(title, author, year)
            case "2":
                book_id = int(input("Введите ID книги для удаления: "))
                library.delete_book(book_id)
            case "3":
                field = input("Поиск по (title/author/year): ").strip()
                query = input("Введите запрос: ").strip()
                library.search_books(query, field)
            case "4":
                library.list_books()
            case "5":
                book_id = int(input("Введите ID книги: "))
                status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
                library.update_status(book_id, status)
            case "0":
                print("Выход из программы.")
                break
            case _:
                print("Некорректный выбор.")
if __name__ == "__main__":
    main()