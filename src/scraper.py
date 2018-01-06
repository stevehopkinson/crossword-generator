import json
import urllib2
from bs4 import BeautifulSoup
from multiprocessing import Pool

baseUrl = 'https://www.theguardian.com/crosswords/quick/'
firstIndex = 9251
lastIndex = 14871

def scrapePage(i):
  	try:
		url = baseUrl + str(i)
		page = urllib2.urlopen(url)
		dom = BeautifulSoup(page, 'html.parser')
		crosswordElement = dom.find('div', attrs={'class': 'js-crossword'})
		crosswordDataJson = crosswordElement.get('data-crossword-data')
		crosswordData = json.loads(crosswordDataJson)
		print crosswordData['name']
		return crosswordData		
  	except:
		print 'Scraping crossword data failed:'
		print i

def outputResults(results):
	sanitisedResults = list(filter(lambda x: x is not None, results))
	output = open('crosswords.txt', 'w')
	outputJson = json.dumps(sanitisedResults)
	output.write(outputJson)
	output.close()
	print 'Done! Total crosswords parsed:'
	print len(results)

if __name__ == '__main__':
	pool = Pool()
	r = pool.map_async(scrapePage, range(firstIndex, lastIndex + 1), callback=outputResults)
	r.wait()
