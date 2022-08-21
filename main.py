'''
Author: Blueness
Date: 2022-08-19 21:08:27
LastEditTime: 2022-08-19 21:58:59
LastEditors: Blueness
Description: 为pz做的一个自动把存档每隔多少分钟打包保存到另外一个文件夹里的玩意
FilePath: /timingzip/main.py
'''
import zipfile, os, time

from loguru import logger


out_zip_name = 'pz_save.zip'
outpath = '/home/w0330t/Zomboid/SavesBak/'
inpath = '/home/w0330t/Zomboid/Saves/'
interval = 120

while True:
    z = zipfile.ZipFile(outpath + out_zip_name,'w')

    for dirpath, dirnames, filenames in os.walk(inpath):
        fpath = dirpath.replace(inpath,'') #这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''#这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
    z.close()
    logger.info('保存完成。')
    time.sleep(interval)
