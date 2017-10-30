import requests
import os
import wget                     # https://pypi.python.org/pypi/wget
from bs4 import BeautifulSoup


def extract_txt(urls, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    file_idx = 1

    for url in urls:
        req = requests.get(url)
        html = req.text                              # get html code

        soup = BeautifulSoup(html, 'html.parser')  # BeautifulSoup Constructor parse html
        html_body = str(soup.find('body'))

        flag = True
        origin = ""
        for chr in html_body:
            if chr == '<':
                flag = False
            elif chr == '>':
                flag = True
            elif flag == True:
                origin += chr
        origin = origin.strip()
        file = open(os.path.join(save_dir, str(file_idx) + '.txt'), 'w', encoding='utf8') # solve UnicodeEncodeError
        file.write(origin)
        file_idx += 1

if __name__ == '__main__':
    extract_txt(['https://codereview.stackexchange.com/questions/23759/download-an-image-from-a-webpage'], 'data/txt')