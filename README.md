# Image url search tool

Python Script for searching Google images url

Installation
============
Make sure you have [Python 3](https://www.python.org/) installed.

Clone this repository to your machine
```bash
git clone https://github.com/leozz37/image-url-search.git
```

Go to the repository directory
```bash
cd image-url-search
```

Install the dependencies
```bash
pip install -r requirements.txt
```

Running
=======

This code requires two flags:

    -t: Search title

    -s: Search quantity
    
    -d, --download: Download the images

**Run example:** 
```bash
python3 main.py -t "Ricardo Milos" -s 100 -d
```

Side Note
=========

The execution time depends on your internet speed and on the quantity. The higher the quantity, the higher should be the execution time.
