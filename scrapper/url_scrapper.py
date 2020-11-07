#!/usr/bin/env python3
#
#   This is a tool for getting image URLs from the internet
#
import errno
import re
import os
import sys

from urllib.request import urlopen
from bs4 import BeautifulSoup, ResultSet


class Scrapper:
    def create_url(self, keyword: str) -> str:
        """
        Remove the spaces on the keyword and returns a Wikipedia URL

        :param: keyword: Keyword to be searched
        :return: Wikipedia URL with Keyword formatted
        :type: str
        """
        formatted_keyword = keyword.replace(" ", "_")
        return "https://en.wikipedia.org/wiki/" + formatted_keyword

    def get_urls(self, search_url: str) -> ResultSet:
        """
        Scrap the Wikipedia page and get the images URL

        :param: search_url: Wikipedia URL
        :return: set of images URL
        :type: ResultSet (bs)
        """
        html = urlopen(search_url)
        bs = BeautifulSoup(html, 'html.parser')
        images_url = bs.find_all('img', {'src': re.compile('.jpg')})
        return images_url

    def save_urls_to_file(self, images_url: ResultSet) -> bool:
        """
        Save the images URL to a txt file

        :param: Set of images URL
        :return: True if succeed
        :type: bool
        """
        # Creating directory and file if doesn't exists
        file_path = "../data/images_urls.txt"
        if not os.path.exists(os.path.dirname(file_path)):
            try:
                os.makedirs(os.path.dirname(file_path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        # Saving content to txt file
        with open(file_path, "w") as f:
            for image in images_url:
                f.write("https:" + image['src'] + '\r\n')

        return True


if __name__ == '__main__':
    """
    Main program entrypoint
    """
    keyword = sys.argv[1]

    scrapper = Scrapper()
    url = scrapper.create_url(keyword)
    images_url = scrapper.get_urls(url)
    scrapper.save_urls_to_file(images_url)
    print(f'{len(images_url)} images found!')
