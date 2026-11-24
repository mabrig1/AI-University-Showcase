import unittest
from progress import progress

class ProgressTests(unittest.TestCase):
    def test_partial(self):
        self.assertEqual(progress(["a","b"], ["a","a"]), {"completed":1,"total":2,"percent":50.0,"next":"b"})
    def test_complete(self):
        self.assertIsNone(progress(["a"], ["a"])["next"])
    def test_unknown(self):
        with self.assertRaises(ValueError):
            progress(["a"], ["b"])
    def test_invalid_catalogue(self):
        for modules in ([], ["a","a"], [" "]):
            with self.assertRaises(ValueError):
                progress(modules, [])

if __name__ == "__main__":
    unittest.main()
