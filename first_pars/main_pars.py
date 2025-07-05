import requests
from lxml import etree
import lxml.html
import csv

def first_pars(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_orig = tree.xpath('/html/body/div[3]/div/div[2]/div[2]/p/text()')
    for i in range(len(text_orig)):
        print(text_orig[i])
    
    
    
def main():
    url = "https://text-pesenok.ru/t115007365-taro"
    first_pars(url)


if __name__ == '__main__':
    main()