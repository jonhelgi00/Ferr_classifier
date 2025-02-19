from icrawler.builtin import GoogleImageCrawler
import os
import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from icrawler.builtin import GoogleImageCrawler


def download_images(query, num_images):
    subfolder = query.replace(" ", "_")
    dest_dir = os.path.join("dataset", "raw_img", subfolder)
    storage = {'root_dir': dest_dir}

    google_crawler = GoogleImageCrawler(storage=storage)
    google_crawler.crawl(keyword=query, max_num=num_images)


if __name__ == '__main__':
    
    queries = {
        "lewis_structure diagram": 2000,
        "connected graph": 2000,
        "calculus equation": 2000
    }
    for query, total in queries.items():
        download_images(query, total)


# def download_images(query, num_images):
#     # Create a crawler that saves images in a folder named after the query
#     storage = {'root_dir': query.replace(" ", "_")}
#     google_crawler = GoogleImageCrawler(storage=storage)
    
#     google_crawler.crawl(keyword=query, max_num=num_images)
#     print(f"Downloaded {num_images} images for query '{query}' into folder '{storage['root_dir']}'.")

# if __name__ == '__main__':
#     query = "puppies"
#     num_images = 5
#     download_images(query, num_images)
