import requests
from bs4 import BeautifulSoup as bs
import pdfkit

base = "http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/"

def main():
    toc = requests.get(base+"toc.htm")
    soup = bs(toc.content, "html.parser")
    links = soup.findAll('a')
    
    for link in links:
        href = link.get('href')
        filename = '_'.join(link.getText().split()) + '.pdf'
        page = base+href
         
        pdfkit.from_url(page, filename)

if __name__ == "__main__":
    main()
