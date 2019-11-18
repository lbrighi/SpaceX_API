import unittest
from SpaceX_API import app


class SpaceXTest(unittest.TestCase):

    def testNext(self):
        response = app.test_client().get('/next')
        self.assertEqual(200, response.status_code)

    def testLatest(self):
        response = app.test_client().get('/latest')
        self.assertEqual(200, response.status_code)

    def testPast(self):
        response = app.test_client().get('/past')
        self.assertEqual(200, response.status_code)

    def testUpcoming(self):
        response = app.test_client().get('/upcoming')
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
