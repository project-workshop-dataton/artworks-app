# artworks-app

Система рекомендации объектов исскуства музея [The Museum of Modern Art (NY)](https://www.moma.org) по свободному текстовому вопросу. Работа базируется на использованиии предобученной LLM-модели.
> Проект тестировался с использованием компьютера на os windows и IDE pycharm

## Навигация
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
Нотбук с визуализацией [ссылка](./data_visualisation.ipynb)

## Столбчатая диаграмма

### Диаграмма зависимости количества произведений искусства от категории "department"
![newplot (2)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/662c8874-c090-43d3-b8ea-ba33bc1785cd)
#### Динамическое отображение
[матрица кореляций признаков дат](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/diag1.html)


### Диаграмма зависимости количества произведений искусства от категории "classification"

![newplot (3)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/5e824f75-818f-49a3-a4ba-4feccbd99078)

#### Динамическое отображение
[Диаграмма зависимости количества произведений искусства от категории "classification"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/diag2.html)

### Диаграмма зависимости количества произведений искусства от категории "size_category"
![newplot (4)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/69a723dc-b491-4a95-bce7-b94fafe06617)

#### Динамическое отображение
[Диаграмма зависимости количества произведений искусства от категории "size_category"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/diag3.html)


### Диаграмма зависимости количества произведений искусства от категории "duration_category"
![newplot (5)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/3b303502-9df1-4c79-9a3b-bc72225e0466)

#### Динамическое отображение
[Диаграмма зависимости количества произведений искусства от категории "duration_category"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/diag4.html)

### Диаграмма зависимости количества произведений искусства от категории "gender"
![newplot (1)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/662962df-2f25-41ae-8847-5781c83ca995)
#### Динамическое отображение
[Диаграмма зависимости количества произведений искусства от категории "gender"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/diag5.html)

## Тепловая карта

### матрица кореляций признаков дат
![newplot](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/17d6e044-eee8-4f97-8b37-03b3c824b7df)
#### Динамическое отображение
[матрица кореляций признаков дат](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/corr_heatmap.html)

### Распределение к-ва произведений искусства в зависимости от department и size_category
![newplot (6)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/a8deea5a-74c3-4d30-9edd-75ade4e3cab9)

#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от department и size_category](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap1.html)


### Распределение к-ва произведений искусства в зависимости от department и duration_category
![newplot (7)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/d8303e42-89d1-4d67-a80c-5d1b8234648c)


#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от department и duration_category](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap2.html)


### Pаспределение к-ва произведений искусства в зависимости от department и gender
![newplot (8)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/42bcc4c2-547a-4bef-bd4a-45265a64109a)


#### Динамическое отображение
[Pаспределение к-ва произведений искусства в зависимости от department и gender](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap3.html)


### Распределение к-ва произведений искусства в зависимости от classification и size_category
![newplot (9)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/7082b8c3-db29-4d3e-8ce2-3ea4bb1177c1)

#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от classification и size_category](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap4.html)


### Распределение к-ва произведений искусства в зависимости от department и size_category
![newplot (6)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/a8deea5a-74c3-4d30-9edd-75ade4e3cab9)

#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от department и size_category](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap5.html)


### Распределение к-ва произведений искусства в зависимости от department и size_category
![newplot (6)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/a8deea5a-74c3-4d30-9edd-75ade4e3cab9)

#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от department и size_category](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap6.html)



### Распределение к-ва произведений искусства в зависимости от department и size_category
![newplot (6)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/a8deea5a-74c3-4d30-9edd-75ade4e3cab9)

#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от department и size_category](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap7.html)



### Распределение к-ва произведений искусства в зависимости от department и size_category
![newplot (6)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/a8deea5a-74c3-4d30-9edd-75ade4e3cab9)

#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от department и size_category](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap8.html)



### Распределение к-ва произведений искусства в зависимости от department и size_category
![newplot (6)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/a8deea5a-74c3-4d30-9edd-75ade4e3cab9)

#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от department и size_category](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap9.html)



### Распределение к-ва произведений искусства в зависимости от department и size_category
![newplot (6)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/a8deea5a-74c3-4d30-9edd-75ade4e3cab9)

#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от department и size_category](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap10.html)
