import unittest
from opened import opened
import tempfile
from .console_colors import colors
import textwrap
import os


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

        print(textwrap.dedent(f"{colors.CYAN}{filepath}{colors.ENDC}"))

    def test_dot_S(self):
        with tempfile.TemporaryDirectory() as temporary_directory:

            expected: str = f"/private{temporary_directory}/{self.filename}"

            with opened('./', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_not_extended(self):
        with opened('./', f"{self.filename}-2", extended=False) as file:
            pass

        if os.path.isfile(f"./{self.filename}-2"):
            pass
        else:
            raise Exception(f"./{self.filename}-2 does not exist")

        os.remove(f"./{self.filename}-2")
        print(
            f"{colors.CYAN}Created and removed file {self.filename}-2{colors.ENDC} succesfully")

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

    def test_dot_not_root_changed(self):
        expected: str = f"{os.getcwd()}/{self.filename}"

        with opened('./', self.filename, extended=True, dot_root='.') as file:
            self.pretty_test_print(file.filepath, expected)

        os.remove(f"./{self.filename}")

    def test_dot_dot_not_root_changed(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            expected: str = f"/private{temporary_directory[::-1].split('/', 1)[1][::-1][:-2]}/{self.filename}"

            with opened('../', self.filename, extended=True, dot_root=temporary_directory) as file:
                self.pretty_test_print(file.filepath, expected)

    def test_error_Unkown_String_Beginning(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            try:
                with opened(None, self.filename, extended=True, dot_root=temporary_directory) as file:
                    pass
            except Exception:
                print(textwrap.dedent(
                    f"{colors.CYAN}Error Raised Expectedly{colors.ENDC}"))
                return True

    def tearDown(self):
        pass
