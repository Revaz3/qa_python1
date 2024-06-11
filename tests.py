from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    from main import BooksCollector

    # класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
    # обязательно указывать префикс Test
    class TestBooksCollector:

        # пример теста:
        # обязательно указывать префикс test_
        # дальше идет название метода, который тестируем add_new_book_
        # затем, что тестируем add_two_books - добавление двух книг
        def test_add_new_book_add_two_books(self):
            # создаем экземпляр (объект) класса BooksCollector
            collector = BooksCollector()

            # добавляем две книги
            collector.add_new_book('Гордость и предубеждение и зомби')
            collector.add_new_book('Что делать, если ваш кот хочет вас убить')

            # проверяем, что добавилось именно две
            # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
            assert len(collector.get_books_rating()) == 2

        # напиши свои тесты ниже
        # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

        def test_add_new_book(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            new_book = collector.add_new_book('Гарри Поттер')
            assert new_book == ['Гарри Поттер']

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
            collector.add_new_book('Война и мир')
            collector.set_book_genre('Война и мир', 'Классика')
            books_classik = collector.get_books_with_specific_genre('Классика')
            assert books_classik == ['Война и мир']

        def test_get_book_genre(self):
            collector = BooksCollector()
            collector.add_new_book('Война и мир')
            collector.set_book_genre('Война и мир', 'Классика')
            collector.add_new_book('Гарри Поттер')
            collector.set_book_genre('Гарри Поттер', 'Фунтези')

            expected_books_genre = {
                'Война и мир' 'Классика'
                'Гарри Поттер' 'Фентези'
            }
            assert collector.get_book_genre() == expected_books_genre

        def test_get_books_for_children(self):
            collector = BooksCollector()
            collector.add_new_book('Алиса в cтране чудес')
            collector.set_book_genre('Алиса в cтране чудес', 'Детская литература')
            books_for_children = collector.get_books_for_children()
            assert books_for_children == ['Алиса в cтране чудес']

        def test_add_book_in_favorite(self):
            collector = BooksCollector()
            collector.add_new_book('Война и мир')
            collector.set_book_genre('Война и мир', 'Классика')
            collector.add_book_in_favorites('Война и мир')
            assert 'Война и мир' in collector.favorites

        def test_delete_book_from_favorite(self):
            collector = BooksCollector()
            collector.add_new_book('Война и мир')
            collector.set_book_genre('Война и мир', 'Классика')
            collector.add_book_in_favorites('Война и мир')
            collector.delete_book_from_favorites('Война и мир')
            assert 'Война и мир' not in collector.favorites

        def test_get_list_of_favorites_books(self):
            collector = BooksCollector()
            collector.add_new_book('Война и мир')
            collector.set_book_genre('Война и мир', 'Классика')
            collector.add_book_in_favorites('Война и мир')
            favorites_list = collector.get_list_of_favorites_books()
            assert favorites_list == ['Война и мир']




