import requests
from bs4 import BeautifulSoup

# Scrape top news from 'Krebs Security'
def krebs_news():
    url = 'https://krebsonsecurity.com/'
    response = requests.get(url)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        print("Soup object created")

        articles = []
        posts = soup.find_all('a', title=True, rel='bookmark')
        print(f"Number of posts found: {len(posts)}")
        
        # Retrieving the 5 most recent posts
        # This can be changed depending on how many articles you want to see
        
        for post in posts[:5]:
            title = post.get_text()
            link = post['href']
            
            # Since other details like author, date, and summary might be in other parts, 
            # we will simplify and only use title and link for this example.

            articles.append({
                'title': title,
                'url': link,
                'author': 'N/A',  # Placeholder if author information is not found
                'date': 'N/A',    # Placeholder if date information is not found
                'summary': 'N/A'  # Placeholder if summary information is not found
            })
        print(f"Number of articles extracted: {len(articles)}")
        return articles
    else:
        print("Failed to fetch the webpage")
        return []

# Scrape top news from 'The Hacker News'
def hacker_news():
    url = 'https://thehackernews.com/'
    response = requests.get(url)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        print("Soup object created")

        articles = []
        posts = soup.select('a.story-link')  # Select the main article link
        print(f"Number of posts found: {len(posts)}")
        
        # Retrieving the 5 most recent posts
        # This can be changed depending on how many articles you want to see
        
        for post in posts[:5]:
            title_element = post.select_one('h2.home-title')
            link = post['href']
            date_element = post.select_one('span.h-datetime')
            summary_element = post.select_one('div.home-desc')

            title = title_element.get_text() if title_element else 'No title'
            date = date_element.get_text() if date_element else 'No date'
            summary = summary_element.get_text() if summary_element else 'No summary'

            articles.append({
                'title': title,
                'url': link,
                'author': 'N/A',  # Placeholder if author information is not found
                'date': date,
                'summary': summary
            })
        print(f"Number of articles extracted: {len(articles)}")
        return articles
    else:
        print("Failed to fetch the webpage")
        return []

# Scrape top news posts from 'Dark Reading'
def dark_reading_news():
    url = 'https://www.darkreading.com/'
    response = requests.get(url)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        print("Soup object created")

        articles = []
        posts = soup.find_all('a', class_='ListPreview-Title', attrs={'data-testid': 'preview-default-title'})
        print(f"Number of posts found: {len(posts)}")

        # Retrieving the 5 most recent posts
        # This can be changed depending on how many articles you want to see

        for post in posts[:5]:  
            title = post.get_text()
            link = url.rstrip('/') + post['href']  # Ensure full URL
            
            # Locate the parent element to find additional details
            parent = post.find_parent('div', class_='ListPreview')
            date_element = parent.select_one('span.ListPreview-Date[data-testid="list-preview-date"]')
            author_element = parent.select_one('a.Contributors-ContributorName[data-testid="contributor-name"]')

            date = date_element.get_text() if date_element else 'N/A'
            author = author_element.get_text() if author_element else 'N/A'

            articles.append({
                'title': title,
                'url': link,
                'author': author,
                'date': date,
                'summary': 'N/A'  # Placeholder if summary information is not found
            })
        print(f"Number of articles extracted: {len(articles)}")
        return articles
    else:
        print("Failed to fetch the webpage")
        return []

if __name__ == "__main__":
    krebs_articles = krebs_news()
    hacker_news_articles = hacker_news()
    dark_reading_articles = dark_reading_news()
    
    # Combining and printing all news sources for display and debugging
    news_all = krebs_articles + hacker_news_articles + dark_reading_articles
    print(news_all)
