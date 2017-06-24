from html.parser import HTMLParser
from urllib import parse
class Linkfinder(HTMLParser):
	def __init__(self,base_url,page_url):
		super().__init__()
		self.base_url=base_url
		self.page_url=page_url
		self.links=set()
	def handle_starttag(self,tag,attr):

		if tag=='a':
			for (attribute,value) in attr:
				#print("Sds")
				if attribute=="href":
					url=parse.urljoin(self.base_url,value)
					self.links.add(url)
	def page_links(self):
		return self.links


		





#finder=Linkfinder()
#finder.feed("<html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>")