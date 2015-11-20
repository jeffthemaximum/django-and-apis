from requests import get


class ApiGet(object):
    def __init__(self, url, request):
        self.url = url
        self.request = request

    def get_string_response(self):
        r = get(self.url).text
        return r

    def get_json_response(self):
        r = get(self.url).json()
        return r
