from redirector import redirect
from flask import Flask, request, Response, make_response
import requests


ITEMS_PATH = 'http://127.0.0.1:5001/'
USERS_PATH = 'http://127.0.0.1:5003/'

app = Flask(__name__)


#выполняется перед КАЖДЫМ запросом. исключить запросы без авторизации
@app.before_request
def check_token():
    #сделать тут исключения для ручек, которым не нужна авторизация, наприме items
    '''
      if('/items/' in request.path):
        return
      else:
         тогда уже делаем то, что ниже
    '''

    users_full_path = 'http://127.0.0.1:5003/user/token'
    response = requests.request(
        method='GET',
        url=users_full_path,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        cookies=request.cookies,
        allow_redirects=False)
    if response.status_code != 200:
        return make_response('check your authorization data',response.status_code , {'Authentication': 'invalid token'})


@app.errorhandler(404)
@app.route("/items/<path>", methods=['GET'])
def items_proxy(path):
    response = redirect(request, ITEMS_PATH)
    return Response(response['content'], response['status_code'], response['headers'])


if __name__ == "__main__":
    app.run(port=5000, debug=True)