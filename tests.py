import pytest

from main import BooksCollector


class TestBooksCollector:

    #проверка добавления двух книг
    def test_add_new_book_add_two_books(self, collector, two_books):

        assert len(collector.get_books_genre()) == 2

    #проверка добавления книги без имени
    def test_add_new_book_add_book_without_name(self, collector):
        collector.add_new_book('')

        assert collector.get_books_genre() == {}

    #проверка добавления жанра книге
    def test_set_book_genre_add_genre(self, collector, one_book):

        assert collector.get_books_genre()['1984'] != '' and collector.get_books_genre()['1984'] in collector.genre

    #проверка вывода жанра книги по имени
    def test_get_book_genre_add_book_book_genre(self, collector, one_book):

        assert collector.get_books_genre()['1984'] == 'Фантастика'

    #проверка вывода книг с определенным жанром
    def test_get_books_with_specific_genre_add_all_genres_one_book(self, collector, all_genres):
        genre = 'Мультфильмы'

        assert len(collector.get_books_with_specific_genre(genre)) == 1 and collector.get_books_with_specific_genre(genre)[0] == 'Золушка'

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['1984', 'Фантастика'],
            ['Мастер и Маргарита', 'Ужасы'],
            ['Имя розы', 'Детективы'],
            ['Золушка', 'Мультфильмы'],
            ['Манюня', 'Комедии']
        ]
    )

    #проверка вывода словаря books_genre
    def test_get_books_genre_add_all_genres_all_books(self, name, genre, collector, all_genres):

        assert len(collector.get_books_genre()) == 5 and collector.get_books_genre()[name] == genre

    @pytest.mark.parametrize(
        'index',
        [
            0,
            1,
            2
        ]
    )

    #проверка вывода книг для детей
    def test_get_books_for_children_add_all_genres_books_without_age_rating(self, index, collector, all_genres):

        assert (len(collector.get_books_for_children()) == 3 and collector.get_books_for_children()[index] not in ['Мастер и Маргарита', 'Имя розы'])

    #проверка добавления книги в избранное
    def test_add_book_in_favorites_add_two_books(self, collector, two_favorite_books):

        assert len(collector.favorites) == 2

    #проверка удаления книги из избранного
    def test_delete_book_from_favorites_add_two_books_one_book(self, collector, two_favorite_books):
        collector.delete_book_from_favorites('1984')

        assert len(collector.favorites) == 1

    #проврека вывода списка избранных книг
    def test_get_list_of_favorites_books_add_two_books_two_books(self, collector, two_favorite_books):

        assert collector.favorites == ['1984', 'Мастер и Маргарита']
