from unittest.mock import patch, Mock, MagicMock
from twitter import Twitter
import pytest
import requests

class ResponseGetMock():
    def json(self):
        return {'avatar_url': 'test'}

@pytest.fixture(params=[None, 'python'])
def username(request):
    return request.param

@pytest.fixture(params=['list', 'backend'], name='twitter')
def fixture_twitter(backend, username, request, monkeypatch):
    if request.param == 'list':
        twitter = Twitter(username=username)
    elif request.param == 'backend':
        twitter = Twitter(backend=backend, username=username)

    # def monkey_return():
    #     return 'test'
    #
    # monkeypatch.setattr(twitter, 'get_user_avatar', monkey_return)

    return twitter

def test_twitter_init(twitter):
    assert twitter

def test_tweet_single_message(twitter):
    with patch.object(twitter, 'get_user_avatar', return_value='test'):
        twitter.tweet("Test message")
        assert twitter.tweet_messages == ["Test message"]

def test_tweet_long_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet('test' * 41)
    assert twitter.tweet_messages == []

def test_initialize_two_twitter_classes(backend):
    twitter1 = Twitter(backend=backend)
    twitter2 = Twitter(backend=backend)
    twitter1.tweet('Test 1')
    twitter1.tweet('Test 2')

    assert twitter2.tweet_messages == ['Test 1', 'Test 2']



@pytest.mark.parametrize("message, expected",(
                         ("Test #first message", ["first"]),
                         ("#first Test message", ["first"]),
                         ("#FIRST Test message", ["first"]),
                         ("Test message #first", ['first']),
                         ("Test message #first #second", ['first', 'second'])
                         ))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected

@patch.object(Twitter, 'get_user_avatar', return_value='test')
def test_tweet_with_username(avatar_mock, twitter):
    if not twitter.username:
        pytest.skip()

    twitter.tweet('Test message')
    assert twitter.tweets == [{'message' : 'Test message', 'avatar' : 'test', 'hashtags': []}]
    avatar_mock.assert_called()

@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_with_hashtag_mock(twitter):
    twitter.find_hashtags = Mock()
    twitter.find_hashtags.return_value = ['first']
    twitter.tweet('Test #second')
    assert twitter.tweets[0]['hashtags'] == ['first']
    twitter.find_hashtags.assert_called_with('Test #second')

def test_twitter_version(twitter):
    twitter.version = MagicMock()
    twitter.version.__eq__.return_value = '2.0'
    assert twitter.version == '2.0'
