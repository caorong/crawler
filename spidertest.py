# -*- coding:utf-8 -*-

import urllib2,logging

# url = 'http://my.oschina.net/chihz/blog/96101'
url = 'http://www.google.ca'

html = urllib2.urlopen(url).read()

# print html
def main():
	# 设置log的 结构
	formatter = logging.Formatter('%(asctime)s %(threadName)s %(levelname)s %(message)s')
	# 新建/读取文件的封装 
	fileHandler = logging.FileHandler("log")
	fileHandler.setFormatter

if __name__ == '__main__':
	main()