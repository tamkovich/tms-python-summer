## Common

### Review notes:
1. Не перемещайте \_\_init__.py file
2. Не удаляйте \_\_init__.py file
3. Пожалуйста, удалите ненужные комментарии
4. Пожалуйста, именуйте файлы с заданием по шаблону
5. Проверьте строку перед тем как переводить в число через .isdigit() или try-except
6. Проверьте и уберите лишние print()
7. Название переменных не отражают суть того, что в них содержится
8. try-except блок должен оборачивать только те строчки в которых может произойти ожидаемая ошибка
9. Добавьте описание задач в шапку файла (через docstring)
10. Пожалуйста, оставьте в Pull Request только домашку к текущему заданию
11. Удалите ненужные переменные
12. Добавьте описание к каждой функции/классу docstring:
```python
def func(a: str) -> int:
    """Выполняет какой-то код, который работает"""

class Cat:
    """Класс для работы с котами"""
```

13. Проверьте отступы
14. Назовите функции так, чтобы сразу было понятно, что они делают
15. Не выполняйте код, если проверка на число не прошла
16. Удалите ненужные commits:
https://htmlacademy.ru/blog/boost/tools/how-to-squash-commits-and-why-it-is-needed
17. Не называйте переменные зарезервированными (built-in) именами.

Список built-in функций: 
- https://docs.python.org/3/library/functions.html
- https://pythonworld.ru/osnovy/vstroennye-funkcii.html
18. Добавьте typing к каждой функции:
```python
def func(a: str) -> int:
```
19. Если переменная в цикле не используется, то лучше ее назвать с _i или _:
```python
for _ in range(10):
```
20. Закрывайте файлы после работы с ними
21. Замените следующие выражения:

```python
if x == True:
if x == False:
```
на
```python
if x:
if not x:
if x is True:
if x is not False:
```
22. Поправьте структуру класса по списку ниже:
```python
class Cat
    
    # CONSTANTS

    def __new__(cls):
        pass

    def __init__(self):
        pass
    
    # public methods

    # protected methods

    # private methods
```