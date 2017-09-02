import quackdns.core as core
import unittest

__TEST_TOKEN__ = "b10eae0b-4153-41cc-8be1-1c811de51c0d"
__TEST_DOMAIN__ = "test-quackdns"


class MockUpdaterTest(unittest.TestCase):
    def test_mock_updater(self):
        """
        Check that the mock implementation adheres to the contract
        defined in AbstractUpdater.

        :return:
        """
        mock_updater = core.MockUpdater()
        success_response = "Updated!"

        self.assertEqual(mock_updater.update(), success_response)


class UpdaterTest(unittest.TestCase):
    def test_updater(self):
        updater = core.Updater(token=__TEST_TOKEN__, domains=__TEST_DOMAIN__)
        updater.update()
        self.assertIsNotNone(updater)


if __name__ == '__main__':
    unittest.main()
