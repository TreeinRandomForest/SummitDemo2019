import sys

from icrawler.builtin import GoogleImageCrawler


try:
    keyword = sys.argv[1]
    num_img = int(sys.argv[2])
    target_dir = sys.argv[3]
    
except:
    raise ValueError("Usage: python download_data.py [search keyword] [num images to download] [target dir]")

crawler = GoogleImageCrawler(storage={'root_dir': target_dir})
crawler.crawl(keyword = keyword, max_num = num_img)
