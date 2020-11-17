import os.path as osp
import os
import requests
from urllib.parse import urlparse

urls = [
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2015/CRNH0203-2015-TX_Edinburg_17_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2016/CRNH0203-2016-TX_Edinburg_17_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2017/CRNH0203-2017-TX_Edinburg_17_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2018/CRNH0203-2018-TX_Edinburg_17_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2019/CRNH0203-2019-TX_Edinburg_17_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2020/CRNH0203-2020-TX_Edinburg_17_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2015/CRNH0203-2015-TX_Port_Aransas_32_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2016/CRNH0203-2016-TX_Port_Aransas_32_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2017/CRNH0203-2017-TX_Port_Aransas_32_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2018/CRNH0203-2018-TX_Port_Aransas_32_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2019/CRNH0203-2019-TX_Port_Aransas_32_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2020/CRNH0203-2020-TX_Port_Aransas_32_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2015/CRNH0203-2015-TX_Bronte_11_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2016/CRNH0203-2016-TX_Bronte_11_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2017/CRNH0203-2017-TX_Bronte_11_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2018/CRNH0203-2018-TX_Bronte_11_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2019/CRNH0203-2019-TX_Bronte_11_NNE.txt',
    'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2020/CRNH0203-2020-TX_Bronte_11_NNE.txt',
]

for url in urls:
    localdir = pp.path.split('/')[1:-1]
    localdir = os.sep.join(localdir)

    localfile = pp.path.split('/')[1:]
    localfile = os.sep.join(localfile)

    if osp.exists(localfile):
        print("skipping download: {}".format(localfile))
        continue
    if not osp.exists(localdir):
        print("mkdir -p {}".format(localdir))
        os.makedirs(localdir)

    pp = urlparse(url)
    r = requests.get(url)
    s = r.content

    with open(localfile, 'w') as f:
        f.write(s)
