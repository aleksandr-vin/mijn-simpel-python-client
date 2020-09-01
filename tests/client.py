from unittest import TestCase, skip
from mijn_simpel.client import Session
from os import getenv

class TestClient(TestCase):

    @skip("rate limit")
    def test_login(self):
        s = Session()
        resp = s.login(
            getenv('MIJN_SIMPEL_USERNAME'),
            getenv('MIJN_SIMPEL_PASSWORD')
        )
        print(resp)

    def test_account_subscription_overview(self):
        s = Session()
        resp = s.account_subscription_overview()
        print(resp)

    def test_dashboard(self):
        s = Session()
        resp = s.account_subscription_overview()
        resp = s.dashboard(resp['mainSubscription']['subscriptionId'])
        print(resp)


if __name__ == '__main__':
    unittest.main()
