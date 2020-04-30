from twitter import Twitter
import pytest

def test_twitter_init():
    twitter = Twitter()
    assert twitter

def test_tweet_single_message():
    twitter = Twitter()
    twitter.tweet("Test message")
    assert twitter.tweets == ["Test message"]

def test_tweet_long_message():
    twitter = Twitter()
    with pytest.raises(Exception):
        twitter.tweet('test' * 41)
    assert twitter.tweets == []