import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()

    return collector

@pytest.fixture
def one_book(collector):

    collector.add_new_book('1984')
    collector.set_book_genre('1984', 'Фантастика')

@pytest.fixture
def two_books(collector):
    collector.add_new_book('1984')
    collector.set_book_genre('1984', 'Фантастика')
    collector.add_new_book('Мастер и Маргарита')
    collector.set_book_genre('Мастер и Маргарита', 'Ужасы')

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

@pytest.fixture
def two_favorite_books(collector, two_books):

    collector.add_book_in_favorites('1984')
    collector.add_book_in_favorites('Мастер и Маргарита')
