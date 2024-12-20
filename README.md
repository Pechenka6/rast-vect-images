# Image Info Reader

**IIReader** — это приложение на Python с графическим интерфейсом, предназначенное для анализа изображений в указанной папке. Программа считывает основные характеристики изображений и отображает их в удобном списке.

## Возможности

- **Поддержка популярных форматов**: `.jpg`, `.jpeg`, `.gif`, `.tif`, `.bmp`, `.png`, `.pcx`.
- **Сбор информации о файлах**:
  - Имя файла.
  - Размер (в пикселях).
  - DPI (если доступно).
  - Глубина цвета.
  - Тип сжатия (если доступно).
- Удобный просмотр данных через интерфейс с прокруткой.

## Установка

1. Убедитесь, что у вас установлен Python версии 3.7 или выше.
2. Установите необходимые зависимости:

   ```bash
   pip install pillow

## Использование

1. Сохраните код в файл, например `IIReader.py`.

2. Запустите приложение:

   ```bash
   python IIReader.py

## Использование

- Выберите папку с изображениями, нажав кнопку **Browse**.
- Информация об изображениях отобразится в списке в главном окне программы.

## Функции

- **get_image_info(directory)**:  
  Сканирует указанную директорию, извлекает данные об изображениях и возвращает список информации.

- **load_directory()**:  
  Открывает окно выбора папки и запускает анализ изображений.

- **display_info(image_info)**:  
  Отображает информацию о каждом изображении в графическом интерфейсе.

## Пример вывода

Программа отображает следующую информацию:

```plaintext
example.jpg: 1920 x 1080, DPI: 300, Color Depth: RGB, Compression: jpeg
sample.png: 800 x 600, DPI: N/A, Color Depth: RGBA, Compression: N/A
```

## Ограничения

- Если файл изображения поврежден или его невозможно прочитать, программа пропустит его и выведет сообщение об ошибке в консоли.
- DPI и тип сжатия доступны не для всех форматов.

## Зависимости

- **tkinter**: встроенная библиотека Python для создания графического интерфейса.
- **Pillow**: библиотека для работы с изображениями.

## Требования

- Python 3.7+
- Операционная система с поддержкой `tkinter` (Windows, macOS, Linux).

## Исходный код

Исходный код приложения доступен на [GitHub](https://github.com/pechenka6/rast-vect-images). Вы можете ознакомиться с кодом, внести свои предложения или доработки.

## Обратная связь

Если у вас возникли вопросы, предложения или вы обнаружили ошибку, пожалуйста, свяжитесь с разработчиком:

* **Email**: 2709400@gmail.com
* **GitHub**: [Pechenka6](https://github.com/pechenka6)


## Лицензия

Этот проект распространяется под лицензией MIT. Вы можете свободно использовать, изменять и распространять код в соответствии с условиями лицензии.
