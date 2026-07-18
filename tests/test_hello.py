import io
import sys
import unittest

from hello import hello


class TestHelloFunction(unittest.TestCase):
    def test_hello_default(self):
        captured = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured

        try:
            hello()
        finally:
            sys.stdout = sys_stdout

        self.assertEqual(captured.getvalue().strip(), "hello Julian")

    def test_hello_custom_name(self):
        captured = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured

        try:
            hello("Alice")
        finally:
            sys.stdout = sys_stdout

        self.assertEqual(captured.getvalue().strip(), "hello Alice")


if __name__ == "__main__":
    unittest.main()
