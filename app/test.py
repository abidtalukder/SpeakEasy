from bs4 import BeautifulSoup
import requests
topic = "Culture"
searches = {"English "+topic+" terms and vocab", "Spanish "+topic+" vocab", "Portuguese "+topic+" vocab", "French "+topic+" vocab", "Hindi "+topic+" vocab"}
url = 'https://www.google.com/search?'
for search in searches:
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.82',
    }
    parameters = {'q': search}

    content = requests.get(url, headers=headers, params=parameters).text
    soup = BeautifulSoup(content, 'html.parser')

    search = soup.find(id='search')
    first_link = search.find('a')

    print(first_link['href'])
