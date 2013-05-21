# -*- coding:utf-8 -*-

import urllib2,logging

# url = 'http://my.oschina.net/chihz/blog/96101'
# url = 'http://www.google.ca'

# html = urllib2.urlopen(url).read()

def congifLogger(logFile, logLevel):
	'''配置logging的日志文件以及日志的记录等级'''
	logger = logging.getLogger('Main')
	LEVELS={
			1:logging.CRITICAL, 
			2:logging.ERROR,
			3:logging.WARNING,
			4:logging.INFO,
			5:logging.DEBUG,#数字最大记录最详细
			}
	formatter = logging.Formatter(
			'%(asctime)s %(threadName)s %(levelname)s %(message)s')
	try:
		# http://docs.python.org/2/library/logging.handlers.html?highlight=filehandler#logging.FileHandler
		# The FileHandler class, located in the core logging package, sends logging output to a disk file.
		fileHandler = logging.FileHandler(logFile)
	except IOError, e:
		return False
	else:
		fileHandler.setFormatter(formatter)
		logger.addHandler(fileHandler)
		logger.setLevel(LEVELS.get(logLevel))
		return True

# print html
def main():
	# 设置log的 结构
	logger = logging.getLogger('Main')
	formatter = logging.Formatter('%(asctime)s %(threadName)s %(levelname)s %(message)s')
	# 新建/读取文件的封装 
	fileHandler = logging.FileHandler("log.txt")
	fileHandler.setFormatter(formatter)
	logger.addHandler(fileHandler)
	logger.setLevel(logging.INFO)

if __name__ == '__main__':
	# congifLogger('log.txt',5)
	main()
	log = logging.getLogger('Main.abc')
	log.info('123')
