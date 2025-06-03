import unittest


def runTest():
    loader = unittest.TestLoader()
    suite = loader.discover('.')

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    runTest()
