from bs4 import BeautifulSoup
import requests

search = 'your search terms here.'
url = 'https://www.google.com/search?q=spanish topic greetings'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}
parameters = {'q': search}

content = requests.get(url, headers=headers, params=parameters).text
soup = BeautifulSoup(content, 'html.parser')

search = soup.find(id='search')
first_link = search.find('a')

print(first_link['href'])
