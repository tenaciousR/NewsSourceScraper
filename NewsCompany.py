import json

# this writes the JSON file of sources for the articles used

sources = {
  "cnbc": {
    "link": "https://www.cnbc.com/us-news/"
  },
  "nbcnews": {
    "link": "http://www.nbcnews.com/"
  },
  "yahoo": {
    "link": "https://news.yahoo.com/"
  },
  "washingtonpost": {
    "link": "https://www.washingtonpost.com/"
  }
}


with open('sources.txt', 'w') as outfile:
    json.dump(sources, outfile)

