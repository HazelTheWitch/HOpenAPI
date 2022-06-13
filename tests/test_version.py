import unittest
from typing import Generator

from hopenapi.version import Version


class TestVersionInitialization(unittest.TestCase):
    def test_integers(self):
        v = Version(1, 0, 2)

        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.patch, 2)

    def test_string(self):
        v = Version('1.0.2')

        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.patch, 2)

        v = Version('v1.0.2')

        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.patch, 2)

    def test_tuple(self):
        v = Version((1, 0, 2))

        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.patch, 2)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            Version('1.0.2', 1)

        with self.assertRaises(ValueError):
            Version(1, 0, 's')

        with self.assertRaises(ValueError):
            Version(1.2, 3, 4)

        with self.assertRaises(ValueError):
            Version((1.2, 3, 4))


class TestVersionOrdering(unittest.TestCase):
    def setUp(self):
        self.versions = [
            Version('0.0.1'),
            Version('0.0.2'),
            Version('0.1.0'),
            Version('1.1.0'),
            Version('3.1.0'),
            Version('3.2.1')
        ]

    def iterateVersions(self) -> Generator[tuple[int, Version, int, Version], None, None]:
        for i, v0 in enumerate(self.versions):
            for j, v1 in enumerate(self.versions):
                yield i, v0, j, v1

    def test_lt(self):
        for i, v0, j, v1 in self.iterateVersions():
            self.assertEqual(i < j, v0 < v1)

    def test_gt(self):
        for i, v0, j, v1 in self.iterateVersions():
            self.assertEqual(i > j, v0 > v1)

    def test_le(self):
        for i, v0, j, v1 in self.iterateVersions():
            self.assertEqual(i <= j, v0 <= v1)

    def test_ge(self):
        for i, v0, j, v1 in self.iterateVersions():
            self.assertEqual(i >= j, v0 >= v1)

    def test_eq(self):
        self.assertEqual(Version('3.2.1'), Version('3.2.1'))

    def test_ne(self):
        self.assertNotEqual(Version('3.2.1'), Version('3.2.2'))


if __name__ == '__main__':
    unittest.main()
