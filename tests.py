from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_book(self):
        collector = BooksCollector()

        book_name = 'Приключения Алисы'
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

        book_name_empty = ''
        collector.add_new_book(book_name_empty)
        assert book_name_empty not in collector.books_genre


    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        assert collector.books_genre["1984"] == "Фантастика"

        collector.set_book_genre("1984", "Неизвестный жанр")
        assert collector.books_genre["1984"] != "Неизвестный жанр"

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_book_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        books_horror = collector.get_books_with_specific_genre('Ужасы')
        assert books_horror == ['Чужой']

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')


        assert collector.get_book_genre('Чужой') == 'Ужасы'
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Алиса в cтране чудес')
        collector.set_book_genre('Алиса в cтране чудес', 'Мультфильмы')
        books_for_children = collector.get_books_for_children()
        assert books_for_children == ['Алиса в cтране чудес']

    def test_add_book_in_favorite(self):
        collector = BooksCollector()
        collector.books_genre = {'Чужой': 'Ужасы'}
        collector.add_book_in_favorites('Чужой')
        assert 'Чужой' in collector.favorites

    def test_delete_book_from_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        collector.add_book_in_favorites('Чужой')
        collector.delete_book_from_favorites('Чужой')
        assert 'Чужой' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Чужой')
        collector.set_book_genre('Чужой', 'Ужасы')
        collector.add_book_in_favorites('Чужой')
        favorites_list = collector.get_list_of_favorites_books()
        assert favorites_list == ['Чужой']


