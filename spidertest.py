# -*- coding:utf-8 -*-

import urllib2,logging
from bs4 import BeautifulSoup
import sys,codecs,re

def gprint(s):
	print s.decode('utf8').encode('gbk')

# url = 'http://my.oschina.net/chihz/blog/96101'
def main():
	# 解决Python2.7的UnicodeEncodeError: ‘ascii’ codec can’t encode异常错误
	# http://wangye.org/blog/archives/629/
	reload(sys)
	sys.setdefaultencoding('utf-8')
	
	url = 'http://www.lovelucy.info/python-crawl-pages.html'
	# url = 'https://news.ycombinator.com/'
	html = urllib2.urlopen(url).read()
	# print html.decode('utf8').encode('gbk')
	# soup = BeautifulSoup(codecs.decode(html,'utf8'))
	soup = BeautifulSoup(html,fromEncoding='utf8')
	# print soup.prettify().decode('utf8').encode('gbk')
	# print len(soup.find_all('tr'))
	# tr_num = len(soup.find_all('tr'))
	# for i in soup.find_all('tr'):
	# 	print i.get('td')
		# for j in soupp.find_all('td'):
		# 	print j
	# pstr = """<a href="http://www.evanmiller.org/statistical-formulas-for-programmers.html">"""
	# tr_list = soup.body.center.table.find_all('tr')
	# print soup.body.chi

	for i in soup.find_all(text=True):
		gprint (i)
		pass



	match = re.findall(r"""<a href="http[s]{0,1}://([-=_?#0-9a-zA-Z./;\&]*)"\s{0,1}(rel="nofollow"){0,1}>""", str(soup))
	# print match.group(1).decode('utf8').encode('gbk')
	# print [i.split]
	for i in match:
		if(i[0].split('.')[0] != 'ycombinator'):
			pass
			# print i[0]
			
		# print i.group(0).decode('utf8').encode('gbk')
		# print i.decode('utf8').encode('gbk')
		


if __name__ == '__main__':
	main()

