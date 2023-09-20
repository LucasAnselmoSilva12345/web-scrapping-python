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

def encontrar_e_imprimir_atributo_alt(img):
    alt_text = img.get('alt', None)
    return alt_text

def contar_atributos_alt(imagens):
    atributos_alt_encontrados = 0
    atributos_alt_preenchidos = 0

    for img in imagens:
        alt_text = encontrar_e_imprimir_atributo_alt(img)
        if alt_text:
            src = img.get('src', 'N/A')
            print(f"Valor do atributo 'alt' na imagem \"{src}\": {alt_text}")
            atributos_alt_encontrados += 1
            if alt_text.strip():# Verifica se o valor não está vazio ou contém apenas espaços em branco
                atributos_alt_preenchidos += 1
    
    return atributos_alt_encontrados, atributos_alt_preenchidos

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 webscrapping.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    html = faz_requisicao(url)

    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')

    # Encontre todas as tags <img> no HTML
    imagens = soup.find_all('img')

    atributos_alt_encontrados, atributos_alt_preenchidos = contar_atributos_alt(imagens)
    print(f"Total de atributos 'alt' encontrados: {atributos_alt_encontrados}")
    print(f"Total de atributos 'alt' com valor preenchido: {atributos_alt_preenchidos}")

if __name__ == "__main__":
    main()

