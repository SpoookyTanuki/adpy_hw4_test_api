import requests

with open('YaDisk_token.txt') as file_object:
    yadisk_token = file_object.read().strip()


def put_album(ya_token):

    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                            params={'path': 'NEW ALBUM'},
                            headers={'Authorization': f'OAuth {ya_token}'})
    response_code = response.status_code
    return response_code


class TestCommands():
    def setup(self):
        print('method setUp')

    def teardown(self):
        print('method tearDown')

    def test_put_album(self):
        assert put_album(yadisk_token), 200
