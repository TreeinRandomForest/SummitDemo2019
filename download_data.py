import sys
import os
import subprocess

from icrawler.builtin import GoogleImageCrawler


try:
    keyword = sys.argv[1]
    num_img = int(sys.argv[2])
    target_dir = sys.argv[3]
    
except:
    raise ValueError("Usage: python download_data.py [search keyword] [num images to download] [target dir]")


def download(keyword, target_dir, num_img):
    crawler = GoogleImageCrawler(downloader_threads=8, storage={'root_dir': target_dir})
    crawler.crawl(keyword = keyword, max_num = num_img)

def clean_dir(target_dir):
    files_to_remove = []

    #convert everything to png
    for file in os.listdir(target_dir):    
        
        filename = file.split('.')[0]
        extension = file.split('.')[1].lower()

        filenamepath = f'{target_dir}/{file}'
        
        if extension == 'gif':
            #ignore gif files
            files_to_remove.append(filenamepath)
            continue
        
        if extension != 'png':
            subprocess.call(['convert', filenamepath, f'{target_dir}/{filename}.png'])
            files_to_remove.append(filenamepath)

    #remove files
    for f in files_to_remove:
        print(f'Removing {f}')
        os.remove(f)

if __name__=="__main__":
    download(keyword, target_dir, num_img)
    clean_dir(target_dir)