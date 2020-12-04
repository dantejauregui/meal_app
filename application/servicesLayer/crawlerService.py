import requests
from bs4 import BeautifulSoup

def get_web(search_term):
    URL = f'https://www.allrecipes.com/search/results/?wt={search_term}&sort=re'
    response = requests.get(URL)

    htmlcode = BeautifulSoup(response.content, 'html.parser')
    receipts = htmlcode.find_all('h3', class_='fixed-recipe-card__h3')
    final_data = []

    #just slice 5 receipts in the FOR loop, in order to avoid a lot of database rows
    for r in receipts[:5]:
        r_name = r.find('span', class_='fixed-recipe-card__title-link')
        r_url = r.find('a')['href']
        if None in (r_name, r_url):
            continue
        final_data.append( ( r_name.text, r_url ) )

    return final_data
    print(final_data)


#resultados = get_web("orange")
#print(resultados)

