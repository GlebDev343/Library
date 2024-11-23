import json
from  typing import List, Dict


class Library:
    
    def __init__(self, data_file: str = "data.json"):
        self.data_file = data_file
        self.books = self._load_books()

    def _load_books(self) -> List[Dict]:
        """Загружает книги из файла."""
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_books(self):
        """Сохраняет книги в файл."""
        with open(self.data_file, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """Добавляет книгу в библиотеку"""
        new_book = {
            "id": len(self.books) + 1,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии"
        }
        self.books.append(new_book)
        self._save_books()
        print(f"Книга '{title}' добавлена.")

    def delete_book(self, book_id: int):
        """Удаляет книгу по id"""
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                self._save_books()
                print(f"Книга с ID {book_id} удалена")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, query: str, field: str):
        """Ищет книги по указанному полю"""
        if field not in {"title", "author", "year"}:
            print("Некорректное поле для поиска.")
            return
        results = [book for book in self.books if str(book[field]).lower() == query.lower()]
        if results:
            for book in results:
                self._print_book(book)
        else:
            print("Книги не найдены.")
    
    def list_books(self):
        """Отображает все книги."""
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            self._print_book(book)
    
    def update_status(self, book_id: int, status: str):
        """Изменяет статус книги."""
        if status not in {"в наличии", "выдана"}:
            print("Некорректный статус. Используйте 'в наличии' 'или выдана'.")
            return
        for book in self.books:
            if book["id"] == book_id:
                book["status"] = status
                self._save_books()
                print(f"Статус книги с ID {book_id} обновлен на '{status}'.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def _print_book(self, book: Dict):
        """Форматированный вывод информации о книге"""
        print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
              f"Год: {book['year']}, Статус: {book['status']}")