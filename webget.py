import urllib.request as req
from urllib.parse import urlparse


def download(urls):
    
    for i in range(len(urls)):  
        url = urls[i]
        parsed_result = urlparse(url)
        url_paths = parsed_result.path.split('/')
        file_name = url_paths[-1]
        req.urlretrieve(url, file_name)
