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
 
### как запускать docker неправильно
docker build -t catalogue-im . 
- билдим

docker run --name catalogue-service -p 5001:5001 catalogue-im 
- запускаем

если добавить -d, будет без консоли, как демон. прибивать из клиента в dashboards
порты брать в flaskenv

###правильный способ запуска:
для запуска и пересборки всего из docker-compose: 
- в корне делаешь `docker-compose up --build`

для просто перезапуска:
- в корне делаешь `docker-compose up`



