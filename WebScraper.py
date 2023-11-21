from bs4 import BeautifulSoup
import requests

url ="https://www.boat-lifestyle.com/collections/?utm_source=Google&utm_medium=Search&utm_campaign=SB_Search_Brand_India_Sep2020&gad_source=1&gclid=Cj0KCQiApOyqBhDlARIsAGfnyMp9OcPWB3s_dV21dzQa1nQ7OqYOwCcFczN3rPy1j5-ZngJdFnjgHHgaAsWAEALw_wcB"

response = requests.get(url)
#print(response.status_code)
#print(response.content)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')
print(soup.prettify())


