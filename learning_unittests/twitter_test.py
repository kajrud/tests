import unittest
import twitter


class TwitterTest(unittest.TestCase):

    def setUp(self) -> None:
        self.twitter = twitter.Twitter()

    def test_init(self):
        self.assertTrue(self.twitter)

    def test_tweet_single(self):
        #Given
        #sytuacja wejściowa, tutaj zapisana w setUp
        #When
        self.twitter.tweet("Test message")
        #Then
        self.assertEqual(self.twitter.tweets, ['Test message'])


if __name__ == '__main__':
    unittest.main()
