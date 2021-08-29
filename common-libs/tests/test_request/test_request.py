import unittest

from request.learn_resquest import RequestUtils


class TestRequest(unittest.TestCase):
    def test_request_use(self):
        print("ok")
        requestUtils = RequestUtils()
        requestUtils.tmp([123])

if __name__ == '__main__':
    unittest.main()
