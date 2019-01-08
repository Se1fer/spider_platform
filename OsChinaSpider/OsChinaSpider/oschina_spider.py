import os
import time

while True:
    time.sleep(20)
    os.system("scrapy crawl OsChina -s CLOSESPIDER_TIMEOUT=3600")
