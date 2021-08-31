from bs4 import BeautifulSoup
import requests

# get hacker news top stories
url = "https://news.ycombinator.com/"
hacker_news = requests.get(url)

# get the html from the url
soup = BeautifulSoup(hacker_news.text, "html.parser")

# get first link
article_tag = soup.find_all("a", {"class": "storylink"})

article_text = [article.get_text() for article in article_tag]
article_link = [article.get("href") for article in article_tag]
article_upvotes = soup.find_all("span", {"class": "score"})
article_upvote = [int(article.get_text().split()[0])
                  for article in article_upvotes]

# Get index of article with highes upvote
max_upvote_index = article_upvote.index(max(article_upvote))
print(
    f"The article with the highest upvote is: the '{article_text[max_upvote_index]}' article, it's link is: {article_link[max_upvote_index]} and it has\
 {article_upvote[max_upvote_index]} upvotes")
