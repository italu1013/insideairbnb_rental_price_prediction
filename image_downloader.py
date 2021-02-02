from tqdm import tqdm
import urllib, os
import pandas as pd
import urllib.request

listings = pd.read_csv("data/listings.csv.gz")

cmd = "mkdir -p host_pics"
os.system(cmd)

DOWNLOADS_DIR = "./host_pics/"
for i, url in tqdm(enumerate(listings.host_picture_url)):
    filename = os.path.join(DOWNLOADS_DIR, "%s.png" % listings["id"][i] ) 
    if not os.path.isfile(filename):
        try:
            urllib.request.urlretrieve(url, filename)
        except:
            print(filename)

            
cmd = "mkdir -p house_pics"
os.system(cmd)

DOWNLOADS_DIR = "./house_pics/"
for i, url in tqdm(enumerate(listings.picture_url)):
    filename = os.path.join(DOWNLOADS_DIR, "%s.png" % listings["id"][i] )
    if not os.path.isfile(filename):
        try:
            urllib.request.urlretrieve(url, filename)
        except:
            print(filename)