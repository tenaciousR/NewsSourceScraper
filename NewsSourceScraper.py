import json
import feedparser as fp
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime

# This sets the limit for how many articles are downloaded per URL
LIMIT = 5

# This stores the scraped data
data = {}
data['newspapers'] = {}

with open('sources.txt') as data_file:
    companies = json.load(data_file)
# print(companies)

count = 1

# Iterates through each news company using python newspaper library to extract articles, this does NOT take 
# into account RSS feeds. However if RSS feeds are what is needed, add it to NewsCompany.py
for company, value in companies.items():
    print("Building site for ", company)
    paper = newspaper.build(value["link"], memoize_articles = False)
    newsPaper = {
        "link": value["link"],
        "articles": []
    }
    noneTypeCount = 0
    for content in paper.articles:
        if count > LIMIT:
            break
        try:
            content.download()
            content.parse()
        except Exception as e:
            print(e)
            print("continuing...")
            continue
        # If we get too many articles without a publish date from the same company, we will skip the company
        if content.publish_date is None:
            print(count, " Article has a date of type None...")
            noneTypeCount = noneTypeCount + 1
            if noneTypeCount > 10:
                print("Too many articles with no date type, aborting...")
                noneTypeCount = 0
                break
            count = count + 1
            continue
        article = {}
        article['title'] = content.title
        article['text'] = content.text
        article['link'] = content.url
        article['published'] = content.publish_date.isoformat()
        newsPaper['articles'].append(article)
        print(count, " articles downloaded from", company, " using newspaper, url: ", content.url)
        count = count + 1
        noneTypeCount = 0
    count = 1
    data['newspapers'][company] = newsPaper

# Articles are saved in a JSON file
try:
    with open("scraped_articles.json", "w") as outfile:
        json.dump(data, outfile)
except Exception as e: print(e)

