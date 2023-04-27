import requests as Re
from bs4 import BeautifulSoup as BS

# Configuração Headers

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

# Moeda
moeda = str(input("Digite moeda desejada:"))

# Get pagina

page = Re.get(
    f'https://www.google.com/search?q=cota%C3%A7%C3%A3o+{moeda}&oq=cota%C3%A7%C3%A3o+%7Bmoeda%7D&aqs=chrome..69i57.2231j0j1&sourceid=chrome&ie=UTF-8', headers=headers)
page_hora = Re.get("https://www.google.com/search?q=hora+certa&sxsrf=APwXEdeOJLAoM7ryyzTdeQw5JIQDmxRGhg%3A1682542619849&ei=G5BJZO7CM8Kf5OUP3KiegAs&ved=0ahUKEwiuvLPZt8j-AhXCD7kGHVyUB7AQ4dUDCA8&uact=5&oq=hora+certa&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIOCAAQgAQQsQMQgwEQyQMyCAgAEIAEEJIDMgUIABCABDIICAAQgAQQsQMyCAgAEIoFELEDMggIABCKBRCxAzIFCAAQgAQyBQgAEIAEMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwE6BAgjECc6CwgAEIoFELEDEIMBOgsILhCABBDHARDRAzoHCAAQigUQQzoKCAAQigUQsQMQQzoNCC4QigUQxwEQ0QMQQzoQCC4QigUQsQMQxwEQ0QMQQzoLCC4QigUQsQMQgwE6EwguEIoFELEDEIMBEMcBENEDEEM6DQgAEIoFELEDEIMBEEM6EAgAEIoFELEDEIMBEMkDEEM6CAgAEIoFEJIDOggILhCABBCxA0oECEEYAFAAWP8ZYL4aaARwAHgAgAGvAYgB3Q2SAQQwLjExmAEAoAEBwAEB&sclient=gws-wiz-serp", headers=headers)


# Coletor Html
coleta = BS(page.content, "html.parser")
coleta_hora = BS(page_hora.content, "html.parser")

# Busca do valor

dolar = coleta.find_all("span", class_="DFlfde SwHCTb")[0]
moedas = coleta.find_all("span", class_="vLqKYe")[0]
hora = coleta_hora.find_all("div", class_="gsrt vk_bk FzvWSb YwPhnf")[0]
data = coleta_hora.find_all("span", class_="KfQeJ")[0]

print(f'', moedas.text, 'esta igual a R$: ', dolar.text,
      'Real brasileiro. \n Hora de pesquisa:', hora.text, '\n Data de pesquisa:', data.text)
