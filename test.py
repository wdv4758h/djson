from djson import request_json
import unittest

class TestDjson(unittest.TestCase):
    def test_request_json(self):
        class A:
            body = '{"asd": 123}'

        @request_json
        def f(data):
            return data.json

        self.assertEqual(f(A()), {'asd': 123})

if __name__ == '__main__':
    unittest.main()
