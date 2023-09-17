import requests
from bs4 import BeautifulSoup
import sys

def faz_requisicao(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None

def verifica_tags_e_ordenacao(html):
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all(["html", "head", "body"])
    return tags == sorted(tags, key=lambda x: html.find(str(x)))

def verifica_css_js(html):
    soup = BeautifulSoup(html, "html.parser")
    css_tags = soup.find_all("style")
    js_tags = soup.find_all("script")
    css_inline = any(tag.get_text() for tag in css_tags)
    js_inline = any(tag.get_text() for tag in js_tags)
    css_links = [link["href"] for link in soup.find_all("link", rel="stylesheet") if link.get("href")]
    js_links = [script["src"] for script in soup.find_all("script", src=True)]
    return css_inline, js_inline, css_links, js_links

if len(sys.argv) != 2:
    print("Uso: python3 webscrapping.py <URL>")
    sys.exit(1)

url = sys.argv[1]

html = faz_requisicao(url)

if html:
    tags_ordenadas = verifica_tags_e_ordenacao(html)
    resultados_css_js = verifica_css_js(html)

    if tags_ordenadas and resultados_css_js:
        print(f"As tags 'html', 'head' e 'body' estão presentes e bem ordenadas em {url}")
        css_inline, js_inline, css_links, js_links = resultados_css_js
        print(f"CSS inline encontrado: {css_inline}")
        print(f"JS inline encontrado: {js_inline}")
        print(f"Links CSS externos: {css_links}")
        print(f"Links JS externos: {js_links}")
    else:
        print(f"As tags 'html', 'head' e 'body' não foram encontradas ou não estão bem ordenadas em {url}")
        print("Não foi possível verificar a presença de CSS e JS.")
