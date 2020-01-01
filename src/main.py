import argparse
import json
import os
import shutil
import sys
from os import path
from google_images_download import google_images_download 

class SearchTool():
    def __init__(self):
        SearchTool.flag = False

    def get_search_parameters(self):
        parser = argparse.ArgumentParser(description="Image search tool")
        parser.add_argument("-t", action="store", dest="title", required=True, help="Search title")
        parser.add_argument("-s", action="store", dest="size",  required=True, help="Search size")
        parser.add_argument("-d", "--download", action="store_true", dest="donwload_flag",  required=False, help="Download image")
        arguments = parser.parse_args()
        SearchTool().set_flag(arguments.donwload_flag)
        return int(arguments.size), arguments.title

    def set_flag(self, download_flag):
        if download_flag:
            SearchTool.flag = True

    def get_search_json(self, search_title, search_size):
        arguments = {
            "keywords"     : search_title,
            "limit"        : search_size,
            "print_urls"   : True,
            "size"         : ">2MP",
        }
        return arguments

    def get_urls(self, arguments):
        orig_stdout = sys.stdout
        f = open('URLS.txt', 'w')
        sys.stdout = f
        response = google_images_download.googleimagesdownload()
        paths = response.download(arguments)
        sys.stdout = orig_stdout
        f.close()
        with open('URLS.txt') as f:
            content = f.readlines()
        f.close()
        urls = []
        for j in range(len(content)):
            if content[j][:9] == 'Completed':
                urls.append(content[j-1][11:-1])
        with open('images.txt', 'w+') as f:
           for url in urls:
                f.write(url + "\n")
        
    def cleanup(self):
        if path.exists("URLS.txt"):
            os.remove("URLS.txt")
        if SearchTool.flag == False and path.exists("Downloads"):
            shutil.rmtree("Downloads")

def main():
    res = SearchTool()
    res.cleanup()

    search_size, search_title = res.get_search_parameters()
    arguments = res.get_search_json(search_title, search_size)
    res.get_urls(arguments)
    res.cleanup()

if __name__ == "__main__":
    main()