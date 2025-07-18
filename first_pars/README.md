
```markdown
# Парсер текстов песен с сайта text-pesenok.ru

Этот скрипт на Python позволяет извлекать тексты песен с сайта [text-pesenok.ru](https://text-pesenok.ru) с помощью библиотек `requests` и `lxml`.

## Установка

1. Убедитесь, что у вас установлен Python 3.8 или новее.
2. Установите необходимые зависимости:

```bash
pip install requests lxml
```

## Использование

1. Запустите скрипт:

```bash
python parser.py
```

2. По умолчанию скрипт парсит текст песни по URL:  
   `https://text-pesenok.ru/t115007365-taro`

## Как изменить URL для парсинга

Откройте файл `parser.py` и измените значение переменной `url` в функции `main()`:

```python
def main():
    url = "https://text-pesenok.ru/ВАШ_URL_ЗДЕСЬ"  # ← Замените этот URL
    first_pars(url)
```

## Функционал

- `first_pars(url)` - основная функция парсинга, которая:
  - Делает GET-запрос к указанному URL
  - Извлекает текст песни с помощью XPath
  - Выводит текст построчно в консоль

## Возможные улучшения

1. Добавить обработку ошибок (404, соединения и т.д.)
2. Реализовать сохранение в файл (txt/csv)
3. Добавить аргументы командной строки
4. Реализовать парсинг других элементов (название песни, исполнитель)

## Зависимости

- requests
- lxml
