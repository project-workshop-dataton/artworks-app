# artworks-app

Система рекомендации объектов исскуства музея [The Museum of Modern Art (NY)](https://www.moma.org) по свободному текстовому вопросу. Работа базируется на использованиии предобученной LLM-модели.

## Уставновка

- Сервера для запуска приложения [Fast API](https://fastapi.tiangolo.com/) & Uvicorn server

`pip install fastapi "uvicorn[standart]"`

- Инструменты работы с данными numpy, pandas, gensim

`pip install numpy pandas gensim`

- Другие инструменты для загрузки картинок и файлов

`pip install Pillow gdown imghdr`

## Загрузка данных

При первом запуске происходит подгрузка данных с гугл диска.
При повторном приоритет отдается локальному файлу. 

Рекомендуется заранее скачать следующие файлы и сохранить в папку `/data` в корне проекта:
- файл модели https://drive.google.com/uc?id=1TAkVgZNWVLvuEiUsEwn_oSbVLFrRfRVG
- файл с базой объектов https://drive.google.com/uc?id=1cWYd9jYG9nGU0jDJDB3G6X6s-GyB2v_6

## Запуск сервера

Сервер запускается с некоторой задержкой, так как необходимо время для инииализации модели.

`uvicorn main:app`

## Исопльзование

- Введите поисковый запрос после запуска сервера

![Alt text](image.png)

- В результате вы получите список рекомендаций

![Alt text](image-1.png)

- Ниже отражены кнопки оценки качества рекоммендации. Можно дать обратную связь. В дальнейшем это поможет улучшать качество поисковой выдачи.

