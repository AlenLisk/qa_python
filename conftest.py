import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()

    return collector

@pytest.fixture
def one_book_without_genre(collector):
    book_name = '1984'
    collector.add_new_book(book_name)

    return book_name

@pytest.fixture
def one_book_with_genre(collector):
    book_name = '1984'
    book_genre = 'Фантастика'
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, book_genre)

    return book_name, book_genre

@pytest.fixture
def all_genres(collector):
    collector.add_new_book('1984')
    collector.set_book_genre('1984', 'Фантастика')
    collector.add_new_book('Мастер и Маргарита')
    collector.set_book_genre('Мастер и Маргарита', 'Ужасы')
    collector.add_new_book('Имя розы')
    collector.set_book_genre('Имя розы', 'Детективы')
    collector.add_new_book('Золушка')
    collector.set_book_genre('Золушка', 'Мультфильмы')
    collector.add_new_book('Манюня')
    collector.set_book_genre('Манюня', 'Комедии')

    return list(collector.books_genre.keys()), list(collector.books_genre.values())

@pytest.fixture
def one_favorite_book(collector, one_book_without_genre):
    book_name = one_book_without_genre
    collector.add_book_in_favorites(book_name)

    return book_name
