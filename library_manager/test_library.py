import unittest
from library import Library
import os
import json

class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Инициализация тестовой библиотеки перед каждым тестом."""
        self.test_file = "test_data.json"
        self.library = Library(self.test_file)

        # Подготовка тестовых данных
        self.sample_books = [
            {"id": 1, "title": "Book One", "author": "Author A", "year": 2001, "status": "в наличии"},
            {"id": 2, "title": "Book Two", "author": "Author B", "year": 2002, "status": "в наличии"},
            {"id": 3, "title": "Book Three", "author": "Author C", "year": 2003, "status": "выдана"}
        ]

        with open(self.test_file, "w") as file:
            json.dump(self.sample_books, file)

        # Перезагружаем библиотеку для работы с тестовыми данными
        self.library = Library(self.test_file)

    def tearDown(self):
        """Удаление тестового файла после каждого теста."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book("New Book", "New Author", 2020)
        self.assertEqual(len(self.library.books), 4)
        self.assertEqual(self.library.books[-1]["title"], "New Book")

    def test_delete_book(self):
        """Тест удаления книги."""
        self.library.delete_book(2)
        self.assertEqual(len(self.library.books), 2)
        self.assertFalse(any(book["id"] == 2 for book in self.library.books))

    def test_delete_nonexistent_book(self):
        """Тест удаления несуществующей книги."""
        self.library.delete_book(99)  # Книга с таким ID не существует
        self.assertEqual(len(self.library.books), 3)  # Количество книг не изменилось

    def test_search_books_by_title(self):
        """Тест поиска книги по названию."""
        results = [book for book in self.library.books if book["title"] == "Book One"]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["author"], "Author A")

    def test_search_books_by_author(self):
        """Тест поиска книги по автору."""
        results = [book for book in self.library.books if book["author"] == "Author B"]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Book Two")

    def test_search_books_by_year(self):
        """Тест поиска книги по году."""
        results = [book for book in self.library.books if book["year"] == 2003]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Book Three")
    def testupdatestatus(self):
        """Тест изменения статуса книги."""
        self.library.update_status(1, "выдана")
        updated_book = next(book for book in self.library.books if book["id"] == 1)
        self.assertEqual(updated_book["status"], "выдана")

    def test_update_status_invalid(self):
        """Тест попытки установить некорректный статус."""
        self.library.update_status(1, "на складе")  # Неверный статус
        original_book = next(book for book in self.library.books if book["id"] == 1)
        self.assertEqual(original_book["status"], "в наличии")  # Статус не изменился

    def test_list_books(self):
        """Тест вывода всех книг."""
        self.assertEqual(len(self.library.books), 3)

if __name__== "__main__":
    unittest.main()