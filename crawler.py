from storer import Storer
from parser import Parser

class Crawler(object):
    def __init__(self):
        self.storer = Storer(db="Quora", collection="user")
        self.parser = Parser("http://www.quora.com/profile/")

    def crawl(self, user_id, depth):
        for item in self.parser.parse_user(user_id, depth):
            self.storer.save(item)


if __name__ == "__main__":
    crawler = Crawler()
    crawler.crawl("Justin-Li-65", 1)