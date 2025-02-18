from icrawler.builtin import GoogleImageCrawler
import os

def download_images(query, num_images):
    subfolder = query.replace(" ", "_")
    # dest_dir = os.path.join("data", "dataset", "raw_img", subfolder)
    dest_dir = os.path.join("dataset", "raw_img", subfolder)
    storage = {'root_dir': dest_dir}
    google_crawler = GoogleImageCrawler(storage=storage)
    google_crawler.crawl(keyword=query, max_num=num_images)
    print(f"Downloaded {num_images} images for query '{query}' into folder '{dest_dir}'.")

if __name__ == '__main__':
    queries = {
    "lewis_structure diagrams": 232,
    "connected graphs": 232,
    "calculus equations": 232
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
#     # Set your search query and number of images to download
#     query = "puppies"
#     num_images = 5
#     download_images(query, num_images)
