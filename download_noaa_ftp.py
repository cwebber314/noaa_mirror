"""
To connect with winSCP use the params:
    - file protocol: FTP
    - Host name: ftp.ncdc.noaa.gov
    - Port number: 21
    - encryption: No encryption
    - Host name: anonymous
    - password: shouldn't matter - email address

"""
from ftplib import FTP
import os.path as osp
import os
from urllib.parse import urlparse

#ftp = FTP('ftp.ncdc.noaa.gov')
ftp = FTP('ftp.ncdc.noaa.gov')
ftp.login('anonymous', passwd='password') # don't use an email address

# This is a painful way to specify files, but I already have the list from another script.
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
    pp = urlparse(url)
    localdir = pp.path.split('/')[1:-1]
    localdir = os.sep.join(localdir)

    localfile = pp.path.split('/')[1:]
    localfile = os.sep.join(localfile)

    remotefile = pp.path.split('/')[-1]

    remotedir = pp.path.split('/')[:-1]
    remotedir = '/'.join(remotedir)

    if osp.exists(localfile):
        print("skipping download: {}".format(localfile))
        continue
    if not osp.exists(localdir):
        print("mkdir {}".format(localdir))
        os.makedirs(localdir)

    print("CWD {}".format(remotedir))
    ftp.cwd(remotedir)

    print("RETR {}".format(remotefile))
    print("local file {}".format(localfile))
    with open(localfile, 'wb') as f:
        ftp.retrbinary('RETR {}'.format(remotefile), f.write)