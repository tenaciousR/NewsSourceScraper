# News Source Article Scraper

## Introduction
* Automate gathering new headlines from various news sources which is then saved as a JSON file.
* **This Repo & Python code is a work in progress**

## Setup/Usage
* This Python 3 code imports [json](https://docs.python.org/3/library/json.html), [feedparser](https://pypi.org/project/feedparser/), [newspaper](https://newspaper.readthedocs.io/en/latest/), [mktime](https://docs.python.org/2/library/time.html), and [datetime](https://docs.python.org/3/library/datetime.html). 
 
## Data
* [NewsCompany](https://github.com/tenaciousR/NewsSourceScraper/blob/master/NewsCompany.py) is the file containing the desired News Sources' website link. Then opens a `.txt` file and saves it as `sources`. 
* [sources](https://github.com/tenaciousR/NewsSourceScraper/blob/master/sources.txt) is the json of the sources listed in NewsCompany.

## Process 
* [NewsSourceScraper.py](https://github.com/tenaciousR/NewsSourceScraper/blob/master/NewsSourceScraper.py) gathers the most recent news articles from the sources listed, and create groups of compiled articles per news website. This file does not include RSS link configuration processes, more comments are within the file as well.

