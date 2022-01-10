import requests
from bs4 import BeautifulSoup
from lxml import etree

def  todosProductos(producto):
    siguiente = 'https://listado.mercadolibre.com.pe/'+producto

    lista_titulo = []
    lista_precios = []
    lista_url = []
    while True:
        r = requests.get(siguiente)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            #titulo
            titulos = soup.find_all('h2', attrs={"class":"ui-search-item__title"})
            titulos = [i.get_text() for i in titulos]
            lista_titulo.extend(titulos)
            
            #precio
            dom = etree.HTML(str(soup))
            precios =  dom.xpath('//li[@class="ui-search-layout__item"]/div/div/div[2]/div[2]/div/div[1]/div/div/span//span[@class="price-tag-amount"]//span[@class="price-tag-fraction"]')
            precios = [i.text for i in precios]
            lista_precios.extend(precios)
            
            #url
            urls = soup.find_all('a', attrs={"class":"ui-search-item__group__element ui-search-link"})
            urls = [i.get('href') for i in urls]
            lista_url.extend(urls)
            
            ini =soup.find('span',attrs={"class":"andes-pagination__link"}).text
            ini = int(ini)
            can = soup.find('li', attrs={"class":"andes-pagination__page-count"}).text
            can = int(can.split(" ")[1])
            
        else:
            break
        print(ini, "/", can)
        if ini ==can:
            break
        siguiente = dom.xpath('//div[@class="ui-search-pagination"]/ul//li[contains(@class, "--next")]/a')[0].get('href')
    
    return lista_titulo, lista_url, lista_precios
    
def limite_producto(producto, limite):
    siguiente = 'https://listado.mercadolibre.com.pe/'+producto
    lista_titulo = []
    lista_precios = []
    lista_url = []
    while True:
        r = requests.get(siguiente)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            #titulo
            titulos = soup.find_all('h2', attrs={"class":"ui-search-item__title"})
            titulos = [i.get_text() for i in titulos]
            lista_titulo.extend(titulos)
            
            #precio
            dom = etree.HTML(str(soup))
            precios =  dom.xpath('//li[@class="ui-search-layout__item"]/div/div/div[2]/div[2]/div/div[1]/div/div/span//span[@class="price-tag-amount"]//span[@class="price-tag-fraction"]')
            precios = [i.text for i in precios]
            lista_precios.extend(precios)
            
            #url
            urls = soup.find_all('a', attrs={"class":"ui-search-item__group__element ui-search-link"})
            urls = [i.get('href') for i in urls]
            lista_url.extend(urls)
            
            ini =soup.find('span',attrs={"class":"andes-pagination__link"}).text
            ini = int(ini)
            can = soup.find('li', attrs={"class":"andes-pagination__page-count"}).text
            can = int(can.split(" ")[1])
            
        else:
            break
        print(ini, "/", can)
        
        if len(lista_titulo) >= int(limite):
            return lista_titulo[:limite], lista_url[:limite], lista_precios[:limite]
        if ini ==can:
            break
        siguiente = dom.xpath('//div[@class="ui-search-pagination"]/ul//li[contains(@class, "--next")]/a')[0].get('href')
    
    return lista_titulo, lista_url, lista_precios
 

    