# artworks-app

Система рекомендации объектов исскуства музея [The Museum of Modern Art (NY)](https://www.moma.org) по свободному текстовому вопросу. Работа базируется на использованиии предобученной LLM-модели.
> Проект тестировался с использованием компьютера на os windows и IDE pycharm

## Навигация

1. [Установка](https://github.com/project-workshop-dataton/artworks-app/tree/development?tab=readme-ov-file#%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0)
2. [Использование](https://github.com/project-workshop-dataton/artworks-app/tree/development?tab=readme-ov-file#%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
3. [Графики](https://github.com/project-workshop-dataton/artworks-app/tree/development?tab=readme-ov-file#%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%B8)
1. [Установка](#Установка)
2. [Использование](#Использование)
3. [Графики](#Графики)
## Установка
- Использовать автоматическую установку зависимостей

  `pip install -r req.txt`

- Скачать Noda.js

[ссылка для скачивания](https://nodejs.org/en)

## Альтернативная становка
  
- Сервера для запуска приложения [Fast API](https://fastapi.tiangolo.com/) & Uvicorn server

`pip install fastapi "uvicorn[standart]"`

- Инструменты работы с данными numpy, pandas, gensim

`pip install numpy pandas gensim`

- Другие инструменты для загрузки картинок и файлов

`pip install Pillow gdown`

И другие зависимости (см. `req.txt`)

## Загрузка данных

При первом запуске происходит подгрузка данных с гугл диска.
При повторном приоритет отдается локальному файлу. 

Рекомендуется заранее скачать следующие файлы и сохранить в папку `/data` в корне проекта:
- файл модели https://drive.google.com/uc?id=1TAkVgZNWVLvuEiUsEwn_oSbVLFrRfRVG
- файл с базой объектов https://drive.google.com/uc?id=1cWYd9jYG9nGU0jDJDB3G6X6s-GyB2v_6

## Запуск сервера

Сервер запускается с некоторой задержкой, так как необходимо время для инииализации модели.

`uvicorn main:app --reload`

## Использование

- Введите поисковый запрос после запуска сервера

![Alt text](image.png)

- В результате вы получите список рекомендаций

![Alt text](image-1.png)

- Ниже отражены кнопки оценки качества рекоммендации. Можно дать обратную связь. В дальнейшем это поможет улучшать качество поисковой выдачи.

- Команда проекта:

Ефимов Андрей Николаевич, Киселев Виктор Валерьевич, Овечкин Евгений Васильевич, Глазков Тимур Михайлович, Килин Георгий Сергеевич

# Графики

В данном разделе отображены графики построенные на основе обработынных данных, а также работы модели
Нотбук с визуализацией ![ссылка](./data_visualisation.ipynb)

## матрица кореляций признаков дат
![newplot](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/17d6e044-eee8-4f97-8b37-03b3c824b7df)
#### Динамическое отображение
[матрица кореляций признаков дат](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/corr_heatmap.html)

## матрица кореляций признаков дат
![newplot](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/17d6e044-eee8-4f97-8b37-03b3c824b7df)
#### Динамическое отображение
[матрица кореляций признаков дат](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/corr_heatmap.html)

## матрица кореляций признаков дат
![newplot](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/17d6e044-eee8-4f97-8b37-03b3c824b7df)
#### Динамическое отображение
[матрица кореляций признаков дат](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/corr_heatmap.html)
