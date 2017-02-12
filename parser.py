from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

from utilities.helpers import correct_url
from driver import Driver

import pdb

class Parser(object):
    def __init__(self, url):
        self.url = correct_url(url)
        self.driver = Driver()

    # yield items
    def parse_user(self, user_id, depth):
        if depth == 0:
            return

        # print(user_id, depth)

        time.sleep(1)

        # render the whole page and make it into a beautiful soup :)
        this_url = urljoin(self.url, user_id) + "/followers"
        self.driver.get(this_url)

        self.driver.scroll_down(50)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # print this_url, driver.current_url, len(html)

        # find the information of this user
        # pdb.set_trace()

        user_soup = soup.find("span", class_="user")
        if user_soup:
            name = user_soup.get_text()
        else:
            name = ""
        credential_soup = soup.find("span", class_="UserCredential IdentityCredential")
        if credential_soup:
            credential = credential_soup.get_text()
        else:
            credential = ""
        description_soup = soup.find("p", class_="qtext_para")
        if description_soup:
            description = description_soup.get_text()
        else:
            description = ""

        # find the information of his/her followers and recursively crawl the followers
        followers = []
        for follower in soup.find_all("a", class_="user"):
            follower_name = follower.get_text()
            partial_href = follower.get("href")
            # print(follower_name, partial_href)
            follower_id = partial_href.split('/')[-1]
            followers.append([follower_id, follower_name])
            for item in self.parse_user(follower_id, depth-1):
                yield item

        yield {
            "_id": user_id,
            "name": name,
            "credential": credential,
            "description": description,
            "followers": followers
        }