from bs4 import BeautifulSoup
from lxml import etree
from urllib.request import urlopen

perfil = input("Nome de usuário Github: ")

url = "https://github.com/" + perfil
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
dom = etree.HTML(str(soup))

try: 
    name = dom.xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1/span[1]')[0].text.strip()
    followers = dom.xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]/span')[0].text
    following = dom.xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/a[2]/span')[0].text
    repositories = dom.xpath('//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[2]/span')[0].text
    projects = dom.xpath('//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[3]/span')[0].text
    packages = dom.xpath('//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[4]/span')[0].text
    stars = dom.xpath('//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[5]/span')[0].text
    contributions = dom.xpath('//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/h2')[0].text.split(" ")[6]


    print('----------------------------------------\n')
    print(f'Nome: {name}\nSeguidores: {followers}\nSeguindo: {following}\nRepositórios: {repositories}\nProjetos: {projects}\nPacotes: {packages}\nFavoritos: {stars}\nContribuições no último ano: {contributions}')
    print('----------------------------------------')
except:
    print('----------------------------------------')
    print('Esse perfil não existe.')
    print('----------------------------------------')