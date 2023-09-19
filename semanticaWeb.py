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

def verifica_elementos(html, elementos):
    soup = BeautifulSoup(html, "html.parser")
    elementos_presentes = {}
    for elemento in elementos:
        elementos_tags = soup.find_all(elemento)
        elementos_presentes[elemento] = len(elementos_tags)
    return elementos_presentes

def verifica_css_js(html):
    soup = BeautifulSoup(html, "html.parser")
    css_tags = soup.find_all("style")
    js_tags = soup.find_all("script")
    css_inline = any(tag.get_text() for tag in css_tags)
    js_inline = any(tag.get_text() for tag in js_tags)
    css_links = [link["href"] for link in soup.find_all("link", rel="stylesheet") if link.get("href")]
    js_links = [script["src"] for script in soup.find_all("script", src=True)]
    return css_inline, js_inline, css_links, js_links

def verifica_script_e_noscript(html):
    soup = BeautifulSoup(html, "html.parser")
    script_tags = soup.find_all("script")
    noscript_tags = soup.find_all("noscript")
    return len(script_tags) > 0, len(noscript_tags) > 0

def verifica_img_gif(html):
    soup = BeautifulSoup(html, "html.parser")
    img_tags = soup.find_all("img")
    for img in img_tags:
        src = img.get("src")
        if src and src.endswith(".gif"):
            return True
    return False

def verifica_lang(html):
    soup = BeautifulSoup(html, "html.parser")
    html_tag = soup.find("html")
    if html_tag:
        lang = html_tag.get("lang")
        if lang:
            return True
    return False

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 webscrapping.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    html = faz_requisicao(url)

    if not html:
        return

    tags_ordenadas = verifica_tags_e_ordenacao(html)
    elementos = ["embed", "applet", "blink", "marquee"]
    elementos_presentes = verifica_elementos(html, elementos)
    resultados_css_js = verifica_css_js(html)
    script_e_noscript = verifica_script_e_noscript(html)
    img_gif_presente = verifica_img_gif(html)
    lang_presente = verifica_lang(html)

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

    script_presente, noscript_presente = script_e_noscript

    if script_presente:
        if noscript_presente:
            print("A tag <script> está presente, e a tag <noscript> também está presente.")
        else:
            print("A tag <script> está presente, mas a tag <noscript> não está presente.")
    else:
        print("A tag <script> não foi encontrada no HTML.")

    for elemento, quantidade in elementos_presentes.items():
        if quantidade > 0:
            print(f"A tag <{elemento}> foi encontrada {quantidade} vez(es) no HTML.")
        else:
            print(f"A tag <{elemento}> não foi encontrada no HTML.")
    
    if img_gif_presente:
        print("Pelo menos uma tag <img> com atributo 'src' terminando em '.gif' foi encontrada.")
    else:
        print("Nenhuma tag <img> com atributo 'src' terminando em '.gif' foi encontrada.")

    if lang_presente:
        print("A tag <html> possui o atributo 'lang' preenchido.")
    else:
        print("A tag <html> não possui o atributo 'lang' preenchido.")

if __name__ == "__main__":
    main()
