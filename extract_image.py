import requests
import os
import wget                     # https://pypi.python.org/pypi/wget
from bs4 import BeautifulSoup


def extract_img(urls, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    file_idx = 1

    for url in urls:
        req = requests.get(url)
        html = req.text                              # get html code

        soup = BeautifulSoup(html, 'html.parser')  # BeautifulSoup Constructor parse html
        # print(soup.prettify())
        img_tag_list = soup.find_all('img')         # find all 'img' tag

        for img_tag in img_tag_list:
            try:
                img_tag = str(img_tag)
                start_idx = img_tag.find('src')
                start_idx = img_tag.find('http', start_idx)
                end_idx = img_tag.find('jpg', start_idx)       # find 'jpg' from start_idx
                if end_idx == -1:
                    continue
                end_idx += 3                                    # jump 'jpg'
                link = img_tag[start_idx:end_idx]
                out_file_path = os.path.join(save_dir, str(file_idx) + '.jpg')
                wget.download(link, out=out_file_path)
                file_idx += 1
                print(link)
            except:
                print(link)
                print('Error Occur!')



if __name__ == '__main__':
    extract_img(['https://pixabay.com/ko/photos/?min_height=&image_type=&cat=&q=street&min_width=&pagi=2'], 'data/street')