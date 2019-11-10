import requests
from bs4 import BeautifulSoup


# Get the weather page
response = requests.get("https://weather.com/weather/today/l/48.15,17.11")

# TODO: Find the temperature in the response


# Using beautiful soup
soup = BeautifulSoup(response.text, "html.parser")
soup.p
soup.p['class']
soup.find_all('a')
soup.find_all('h1')
soup.find(id="main-ContentMedia-7ec77050-ff5e-4047-b4de-1795be528c69")
soup.find_all(class_="today_nowcard-temp")
soup.find(class_="today_nowcard-temp").children
