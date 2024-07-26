#!/usr/bin/env python3
"""
    Unittest module for utils module
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from typing import Mapping, Sequence
utils = __import__('utils')


class TestAccessNestedMap(unittest.TestCase):
    """
        Test object for utils modules
    """

    @parameterized.expand([
        ({"a": 1}, ["a", ], 1),
        ({"a": {"b": 2}}, ["a", ], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
        ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence, expected):
        """test definition"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a", ]),
        ({"a": 1}, ["a", "b"]),
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """test definition"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
        tests utils.get_json() in utils module
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url: str, test_payload: dict):
        """Test definition"""
        with patch("utils.get_json") as mocked_get:
            mocked_get.return_value = test_payload
            resp = mocked_get(test_url)

            mocked_get.assert_called_once_with(test_url)
            self.assertEqual(resp, test_payload)


class TestMemoize(unittest.TestCase):
    """ Test suite for memoize function """
    def test_memoize(self):
        """ Test case for memoize function """
        class TestClass:
            """ Test class """
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_memo:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property

        mock_memo.assert_called_once()


if __name__ == '__main__':
    unittest.main()
