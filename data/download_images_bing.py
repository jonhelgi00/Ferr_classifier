from icrawler.builtin import BingImageCrawler  
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def download_images(query, num_images):
    subfolder = query.replace(" ", "_")
    dest_dir = os.path.join("dataset", "raw_img","bing", subfolder)
    storage = {'root_dir': dest_dir}

    bing_crawler = BingImageCrawler(storage=storage)  
    bing_crawler.crawl(keyword=query, max_num=num_images)


if __name__ == '__main__':
    queries = {
        "lewis_structure diagram": 2000,
        "connected graph": 2000,
        "calculus equation": 2000
    }
    for query, total in queries.items():
        download_images(query, total)


