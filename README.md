# qa_python - проект для тестирования приложения BooksCollector

**Название приложения:** BooksCollector  
**Описание приложения:** BooksCollector позволяет установить жанр книг и добавить их в избранное   
**Тип тестирования:** Unit-тестирование  
**Фреймворк:** Pytest  
**Перечень тестов:**  
*test_add_new_book_add_one_book* - проверка добавления книги 
*test_add_new_book_add_book_without_name* - проверка добавления книги без имени  
*test_set_book_genre_add_genre* - проверка добавления жанра книге  
*test_get_book_genre_add_book_book_genre* - проверка вывода жанра книги по имени   
*test_get_books_with_specific_genre_add_all_genres_one_book* - проверка вывода книг с определенным жанром  
*test_get_books_genre_add_all_genres_all_books* - проверка вывода словаря books_genre  
*test_get_books_for_children_add_all_genres_books_without_age_rating* - проверка вывода книг для детей  
*test_add_book_in_favorites_add_one_book* - проверка добавления книги в избранное  
*test_delete_book_from_favorites_add_one_books_empty_list* - проверка удаления книги из избранного  
*test_get_list_of_favorites_books_add_one_books_one_books* - проверка вывода списка избранных книг  
**Запуск тестов:**  
*Через терминал:* 
1. Запустить терминал
2. Перейти в директорию проекта - cd .../qa_python  
3. Запустить автотесты - pytest -v tests.py    
*флаг -v обозначает подробный вывод результатов*  

*Через Pycharm:*    
1. Запустить Pycharm  
2. Открыть директорию проекта  
3. Запустить файл tests.py  
*ПКМ по файлу —> Run*  

**Участники:**  
AlenLisk
