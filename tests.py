import unittest
import datetime
import requests
import config


class Test(unittest.TestCase):
    def test_html(self):
        request_url = "http://" + config.Config.SERVER_NAME
        test_date = datetime.date.today().strftime("%d-%m-%Y")
        r = requests.get(request_url)
        print(r.text[:50])
        self.assertTrue(r.ok)
        self.assertIn('<table border="1">', r.text)
        self.assertIn(test_date, r.text)

if __name__ == "__main__":
    unittest.main()
