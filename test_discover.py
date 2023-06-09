import unittest

def suite():
    test_suite = unittest.TestSuite()

    # discoverメソッドを用いて、testディレクトリ以下からテストクラスを探索する
    all_test_suite = unittest.defaultTestLoader.discover("test", pattern="test_*.py")

    for ts in all_test_suite:
        test_suite.addTest(ts)
    return test_suite

if __name__ == "__main__":
    myTestSuite = suite()
    unittest.TextTestRunner().run(myTestSuite)
