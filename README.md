# Бот для игры в "шляпу"

# Разработчики:
* [Ермаков Владимир](https://github.com/ermakovvova)
* [Леонов Иван](https://github.com/kepolol)

# Инструкция по запуску на локальной машине:

1) Склонировать удаленный репозиторий на локальную машину (git clone git@github.com:kepolol/Alias_game_bot.git)
2) Перейти в директорию с проектом
3) Установить требуемые пакеты (pip install -r requirements.txt)
4) Запустить проект для стандартного порта (python run.py)

Для запуска обучения модели выполнить команду из корня проекта 'python app/data_preparation.py'

# Как это работает:

* Предиктивная модель - word2vec
* Для нахождния ближайших используется annoy (ANN алгоритм)
* При предобработке из заголовков выделялись темы и присоединялись к тестам. Были удалены все спец. символы и знаки препинания.
* Модели лежат на YandexDisk
* Деплой сервиса на heroku
