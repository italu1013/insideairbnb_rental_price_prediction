from tqdm import tqdm
import urllib, os
import pandas as pd
import urllib.request
from multiprocessing.dummy import Pool


listings = pd.read_csv("data/listings.csv.gz")

cmd = "mkdir -p host_pics"
os.system(cmd)

def list_packer(l, pack_size=30):
    while l:
        l, pack = l[pack_size:], l[:pack_size]
        yield pack
        

def download_job1(i):
    DOWNLOADS_DIR = "./host_pics/"
    url = listings.host_picture_url[i]
    filename = os.path.join(DOWNLOADS_DIR, "%s.png" % listings["id"][i] )
    if not os.path.isfile(filename):
        try:
            urllib.request.urlretrieve(url, filename)
        except:
            print(filename)
    
idxs = list(range(listings.shape[0]))
with Pool() as p:
    p.map(download_job1, idxs)
    

# DOWNLOADS_DIR = "./host_pics/"
# for i, url in tqdm(enumerate(listings.host_picture_url)):
#     filename = os.path.join(DOWNLOADS_DIR, "%s.png" % listings["id"][i] ) 
#     if not os.path.isfile(filename):
#         try:
#             urllib.request.urlretrieve(url, filename)
#         except:
#             print(filename)

cmd = "mkdir -p house_pics"
os.system(cmd)

def download_job2(i):
    DOWNLOADS_DIR = "./house_pics/"
    url = listings.picture_url[i]
    filename = os.path.join(DOWNLOADS_DIR, "%s.png" % listings["id"][i] )
    if not os.path.isfile(filename):
        try:
            urllib.request.urlretrieve(url, filename)
        except:
            print(filename)

with Pool() as p:
    p.map(download_job2, idxs)
            
            

