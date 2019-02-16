import webget
import sys

for url in sys.argv[1:]:
    webget.download_2(url)
