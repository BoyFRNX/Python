import unittest
from python_repos import get_request


class TestPythonRepos(unittest.TestCase):
    """Tests for 'python_repos.py'."""

    def test_get_request(self):
        """Does the status code equal 200?"""
        r = get_request()
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
