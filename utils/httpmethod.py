import requests


class HTTPMethod:
    headers = {'Content-type': 'aplication/json'}
    cookies = ''

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HTTPMethod.headers, cookies=HTTPMethod.cookies)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, headers=HTTPMethod.headers, cookies=HTTPMethod.cookies, json=body)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, headers=HTTPMethod.headers, cookies=HTTPMethod.cookies, json=body)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, headers=HTTPMethod.headers, cookies=HTTPMethod.cookies, json=body)
        return result
