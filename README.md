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

## Гистограмма + коробчатая

### распределение признака "release_date"
![newplot (10)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/b4626d46-bc57-4e86-9b63-fe747f5e8358)

#### Динамическое отображение
[распределения признака "release_date"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/hist1.html)


### распределение признака "birth_year"
![newplot (11)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/6356b5bb-fae9-4ef7-bb94-de173d8c5c94)


#### Динамическое отображение
[распределение признака "birth_year"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/hist2.html)


### распределение признака "death_year"
![newplot (12)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/4ef1f428-22e2-4851-98f6-e0ce69a71eca)


#### Динамическое отображение
[распределение признака "death_year"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/hist3.html)

## Гистограмма

### Диаграмма распределений признака "release_date" в зависимости от категории "department"
![newplot (13)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/8f5b7c9c-f101-4019-8ceb-c443a993de8b)


#### Динамическое отображение
[Диаграмма распределений признака "release_date" в зависимости от категории "department"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/diag_hist1.html)


### Диаграмма распределений признака "release_date" в зависимости от категории "size_category"

![newplot (14)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/ea42f4ae-17c8-4090-830b-5905944ff527)

#### Динамическое отображение
[Диаграмма распределений признака "release_date" в зависимости от категории "size_category"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/diag_hist2.html)


### Диаграмма распределений признака "release_date" в зависимости от категории "duration_category"

![newplot (15)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/9b426f24-3f45-4b20-8747-dc1f51b356af)

#### Динамическое отображение
[Диаграмма распределений признака "release_date" в зависимости от категории "duration_category"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/diag_hist3.html)

### Диаграмма распределений признака "release_date" в зависимости от категории "gender"

![newplot (16)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/19ab83e9-adb0-48dc-a14d-c96ce7725758)

#### Динамическое отображение
[Диаграмма распределений признака "release_date" в зависимости от категории "gender"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/diag_hist4.html)

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


### Распределение к-ва произведений искусства в зависимости от категории "gender"
![newplot (17)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/77a29b84-701c-4854-a4ca-8a96681e6fa0)

#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от категории "gender"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap5.html)


### Распределение к-ва произведений искусства в зависимости от "classification" и "gender"
![newplot (18)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/f578ef07-77cb-4f10-836c-207117f5cde6)


#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от "classification" и "gender"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap6.html)



### Распределение к-ва произведений искусства в зависимости от "nationality" и "gender"
![newplot (19)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/3372cb70-01c0-4482-855a-d0fbd7c2f5ff)




#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от "nationality" и "gender"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap7.html)



### Распределение к-ва произведений искусства в зависимости от "nationality" и "department"
![newplot (20)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/1c4f616a-3049-4c1c-8572-467f2a698177)


#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от "nationality" и "department"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap8.html)



### Распределение к-ва произведений искусства в зависимости от "nationality" и "size_category"
![newplot (21)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/73ff6616-4e96-40a5-9f37-9cc80038543a)


#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от "nationality" и "size_category"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap9.html)




### Распределение к-ва произведений искусства в зависимости от "nationality" и "duration_category"
![newplot (23)](https://github.com/project-workshop-dataton/artworks-app/assets/68296704/554e3a41-7548-4bfa-a598-327a38b697fa)

#### Динамическое отображение
[Распределение к-ва произведений искусства в зависимости от "nationality" и "duration_category"](http://htmlpreview.github.io/?https://github.com/project-workshop-dataton/artworks-app/blob/development/plots/heatmap10.html)

[В начало](#Навигация)
