#!/usr/bin/env python3
"""
    Client modules test suite
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
client = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
        Class test suite of client
    """

    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch("client.get_json")
    def test_org(self, param, mock_json):
        """test definition"""

        cli = client(param)
        cli.org()
        test_url = f'https://api.github.com/orgs/{input}'
        mock_json.assert_called_once_with('test_url')


if __name__ == '__main__':
    unittest.main()
