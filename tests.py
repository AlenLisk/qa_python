import pytest

from main import BooksCollector

class TestBooksCollector:
    # проверка добавления книги
    def test_add_new_book_add_one_book(self, collector):
        book_name = '1984'
        collector.add_new_book(book_name)

        assert len(collector.get_books_genre()) == 1

    # проверка добавления книги без имени
    def test_add_new_book_add_book_without_name(self, collector):
        book_name = ''
        collector.add_new_book(book_name)

        assert collector.get_books_genre() == {}

    # проверка добавления жанра книге
    def test_set_book_genre_add_genre(self, collector, one_book_without_genre):
        book_name = one_book_without_genre
        book_genre = collector.genre[3]
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_genre()[book_name] != '' and collector.get_books_genre()[book_name] in collector.genre

    # проверка вывода жанра книги по имени
    def test_get_book_genre_add_book_book_genre(self, collector, one_book_with_genre):
        book_name, book_genre = one_book_with_genre
        assert collector.get_books_genre()[book_name] == book_genre

    # проверка вывода книг с определенным жанром
    def test_get_books_with_specific_genre_add_all_genres_one_book(self, collector, all_genres):
        book_name, book_genre = all_genres

        assert len(collector.get_books_with_specific_genre(book_genre[3])) == 1 and collector.get_books_with_specific_genre(book_genre[3])[0] == book_name[3]

    @pytest.mark.parametrize(
        'book_name,book_genre',
        [
            ['1984', 'Фантастика'],
            ['Мастер и Маргарита', 'Ужасы'],
            ['Имя розы', 'Детективы'],
            ['Золушка', 'Мультфильмы'],
            ['Манюня', 'Комедии']
        ]
    )

    # проверка вывода словаря books_genre
    def test_get_books_genre_add_all_genres_all_books(self, book_name, book_genre, collector, all_genres):

        assert len(collector.get_books_genre()) == 5 and collector.get_books_genre()[book_name] == book_genre

    @pytest.mark.parametrize(
        'index',
        [
            0,
            1,
            2
        ]
    )

    # проверка вывода книг для детей
    def test_get_books_for_children_add_all_genres_books_without_age_rating(self, index, collector, all_genres):
        book_with_age_rating = ['Мастер и Маргарита', 'Имя розы']

        assert (len(collector.get_books_for_children())) == 3 and collector.get_books_for_children()[index] not in book_with_age_rating

    # проверка добавления книги в избранное
    def test_add_book_in_favorites_add_one_book(self, collector, one_book_without_genre):
        book_name = one_book_without_genre
        collector.add_book_in_favorites(book_name)

        assert len(collector.get_list_of_favorites_books()) == 1

    # проверка удаления книги из избранного
    def test_delete_book_from_favorites_add_one_books_empty_list(self, collector, one_favorite_book):
        book_name = one_favorite_book
        collector.delete_book_from_favorites(book_name)

        assert collector.get_list_of_favorites_books() == []

    # проверка вывода списка избранных книг
    def test_get_list_of_favorites_books_add_one_books_one_books(self, collector, one_favorite_book):

        assert collector.get_list_of_favorites_books()[0] == one_favorite_book
