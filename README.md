# shop-monorepo

Структруа должна быть как в catelogue, auth и apigateway
каждая папка - отдельный сервис со своим venv
то есть открываешь каждую папку в отдельном окне, создаешь там venv через pycharm

структура в итоге такая:

shop-monorepo/
  catalogue/ <- в этой папке запускаешь flask run, миграции там же
     __init__.py
     venv/
     requirements
     migrations
     catalogue/
       __init__.py
       models.py
       ...

 устанавливаешь зависимости из requirements

 запускаешь как flask run
 параметры запуска конфигурируюется в .flaskenv