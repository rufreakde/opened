import unittest
import os
from opened import opened
import tempfile
from .console_colors import colors
import textwrap


class TestCurrentDirectory(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.txt'

    def pretty_test_print(self, filepath, expected):
        try:
            self.assertEqual(filepath, expected)
        except AssertionError:
            print(textwrap.dedent(f"""
            {colors.WARNING}#COMPARE:
                {colors.FAIL}result:    {filepath}
                {colors.GREEN}expected: {expected}
            {colors.ENDC}"""))
            raise

        print(textwrap.dedent(f"""
        {colors.WARNING}#COMPARE:
            {colors.GREEN}result:   {filepath}
            {colors.GREEN}expected: {expected}
        {colors.ENDC}"""))

    def test_dot_S(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/{self.filename}"

            with opened('./', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_dot_SBS(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/{self.filename}"

            with opened('.\\', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_dot(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/{self.filename}"

            with opened('.', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_dot_subfolder(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/subfolder/{self.filename}"

            with opened('./subfolder', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_dot_subfolder_BS(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/subfolder/{self.filename}"

            with opened('.\\subfolder', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_dot_subfolder_S(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/subfolder/{self.filename}"

            with opened('./subfolder/', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_dot_subfolder_SBS(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/subfolder/{self.filename}"

            with opened('.\\subfolder\\', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_dot_subfolder_dot_dot_S(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/{self.filename}"

            with opened('./subfolder/../', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_dot_subfolder_dot_dot(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/{self.filename}"

            with opened('./subfolder/..', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_dot_subfolder_dot_dot_SBS(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/{self.filename}"

            with opened('.\\subfolder\\..\\', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_dot_subfolder_dot_dot_BS(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/{self.filename}"

            with opened('.\\subfolder\\..', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    # TODO now all cases :P ALL!

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
