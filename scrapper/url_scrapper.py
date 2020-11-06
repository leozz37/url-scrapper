#!/usr/bin/env python3
#
#   This is a tool for getting image URLs from the internet
#
import argparse
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup


# html = urlopen('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')
# bs = BeautifulSoup(html, 'html.parser')
# images = bs.find_all('img', {'scrapper':re.compile('.jpg')})
# for image in images:
#     print(image['scrapper']+'\n')

class Scrapper:
    def create_url(self, keyword: str) -> str:
        """
        Remove the spaces on the keyword and returns a Google Image URL

        :param: keyword: Keyword to be searched
        :return: Google Image's URL with Keyword
        :type: str
        """
        formatted_keyword = keyword.replace(" ", "%20")
        url = "https://www.google.com/search?tbm=isch&q=" + formatted_keyword
        return url


if __name__ == '__main__':
    """
    Main program entrypoint
    """
    # Command line parser
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-l", "--limit", dest="limit", action="store",
                            required=True, default="1",
                            help="The quantity of URL to get")

    arg_parser.add_argument("-k", "--keyword", dest="keyword", action="store", required=True,
                            help="The keyword to be searched")

    args = arg_parser.parse_args()

    print(Scrapper().create_url(args.keyword))
