# Проект "Сигнализация"

Проект разработан с целью определения человека в зоне действия камеры и оповещения в случае несанкционированного доступа

Проект состоит из двух частей: 
1. Модуль записи и оповещения:
Берет изображение с камеры, анализирует на наличие человека, отправляет оповещение на почту и пишет изображение в базу sqlite

2. Веб-приложение:
Предоставляет доступ к базе и просмотру изображений через веб-интерфейс, работает только с авторизованными пользователями

### Установка

1. Клонируйте репозиторий, создайте виртуальное окружение
2. Установите зависимости `pip install -r requirements.txt`
3. Создайте файл settings.py следующего содержания:
  ```
  # WebCam settings:
  # Set 0 if use notebook webcam or you have only one usb-webcam
  # Set 1 if you use additional webcam
  CAM_ID = 0
  # width of picture
  CAM_WIGHT = 1280
  # height of picture
  CAM_HEIGHT = 720
  # image recording frequency in seconds
  IMG_FREQUENCY = 15
  # neural network sensitivity (from 0 to 1)
  NETWORK_SENSITIVITY = 0.6
  # pause between sending email (IMG_FREQUENCY * EMAIL_PAUSE)
  EMAIL_PAUSE = 4
  ```
