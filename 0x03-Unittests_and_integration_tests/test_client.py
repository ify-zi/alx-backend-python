#!/usr/bin/env python3
"""
    Client modules test suite, test every method in the client
    class
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
client = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
        Class test suite of client of GithubOrgClient
        methods
    """

    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch("client.get_json")
    def test_org(self, param: str, mock_json):
        """Test that org() returns the correct value"""
        cli = client(param)
        cli.org()
        test_url = f'https://api.github.com/orgs/{input}'
        mock_json.assert_called_once_with('test_url')


if __name__ == '__main__':
    unittest.main()
