import quackdns.core as core
import unittest


class CoreTest(unittest.TestCase):
    def test_mock_updater(self):
        """
        Check that the mock implementation adheres to the contract
        defined in AbstractUpdater.

        :return:
        """
        mock_updater = core.MockUpdater(None, None)
        success_response = "Updated!"

        self.assertEqual(mock_updater.update(), success_response)


if __name__ == '__main__':
    unittest.main()
