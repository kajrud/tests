import re

class Twitter():
    version = "1.0"

    def __init__(self, backend=None):
        self.backend = backend
        self.__tweets = []

    @property
    def tweets (self):
        if self.backend and not self.__tweets:
            with open(self.backend) as twitter_file:
                self.__tweets = [line.rstrip("\n") for line in self.backend.readlines()]
        return self.__tweets

    def tweet(self, message):
        if len(message) > 160:
            raise Exception("Message too long!")
        self.tweets.append(message)
        if self.backend:
            with open (self.backend, "w") as twitter_file:
                self.backend.write("\n".join(self.tweets))

    def find_hashtags(self, message):
        return [m.lower() for m in re.findall("#(\w+)",message)]