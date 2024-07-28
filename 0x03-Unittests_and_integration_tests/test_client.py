#!/usr/bin/env python3
"""
    Client modules test suite
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
client = __import__('client').GithubOrgClient


class TestGithhubOrgClient(unittest.TestCase):
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
        mock_json.return_value = {"payload": True}
        self.assertEqual(cli.org, {"payload": True})


if __name__ == '__main__':
    unittest.main()
