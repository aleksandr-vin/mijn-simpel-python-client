import requests
import http.cookiejar


def _url(path):
    return 'https://mijn.simpel.nl/api/' + path
#    return 'http://localhost:4444/api/' + path


class ApiError(Exception):
    """An API Error Exception"""

    def __init__(self, resp):
        self.resp = resp

    def __str__(self):
        return "ApiError: {}".format(vars(self.resp))

    
class Session():

    def __init__(self):
        self.s = requests.Session()
        self.s.cookies = http.cookiejar.LWPCookieJar("mijn_simpel_cookie.txt")
        try:
            self.s.cookies.load(ignore_discard=True, ignore_expires=True)
        except FileNotFoundError:
            pass

    def _save_session(self):
        self.s.cookies.save(ignore_discard=True, ignore_expires=True)

    def login(self, username, password):
        resp = self.s.post(_url('login'), json={
            "username": username,
            "password": password,
            "remember": None
        })
        if resp.status_code != 200:
            raise ApiError(resp)
        else:
            self._save_session()
            return True

    def account_subscription_overview(self):
        resp = self.s.get(_url('account/subscription-overview'))
        if resp.status_code != 200:
            raise ApiError(resp)
        else:
            self._save_session()
            return resp.json()
        
    def dashboard(self, subscriptionId):
        resp = self.s.get(_url('dashboard'), params={
            "sid": subscriptionId
        })
        if resp.status_code != 200:
            raise ApiError(resp)
        else:
            self.s.cookies.save()
            return resp.json()

    def close(self):
        self.s.close()
        
