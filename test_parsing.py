import requests
from bs4 import BeautifulSoup

def test_parsing():
    url = 'https://krebsonsecurity.com/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        print("BeautifulSoup parsing successful")
        posts = soup.select('div.post')
        print(f"Number of posts found: {len(posts)}")
        if posts:
            first_post = posts[0]
            title = first_post.select_one('h2.entry-title a').get_text()
            author = first_post.select_one('span.byline a').get_text()
            date = first_post.select_one('time').get_text()
            summary = first_post.select_one('div.entry-summary p').get_text()
            link = first_post.select_one('h2.entry-title a')['href']
            print("First post details:")
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Date: {date}")
            print(f"Summary: {summary}")
            print(f"Link: {link}")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    test_parsing()
