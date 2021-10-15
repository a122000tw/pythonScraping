import os
from urllib.request import urlretrieve
import requests

os.makedirs('img/', exist_ok=True)
IMAGE_URL = "https://www.arfarf.tw/wp-content/uploads/10%E4%BB%B6%E4%BA%8B-1024x677.jpg"

# urlretrieve(IMAGE_URL, 'img/image1.jpg')

# r = requests.get(IMAGE_URL)
# with open('img/image2.jpg', 'wb') as f:
#     f.write(r.content)

# 連續下載
r = requests.get(IMAGE_URL, stream=True)
with open('img/image1.jpg', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
