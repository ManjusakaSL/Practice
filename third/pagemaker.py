#!/usr/bin/env python
# -*- coding:utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import parse

class PageMaker(ContentHandler):

	inPage = False

	def startElement(self, name, attrs):
		if name == 'page':
			self.inPage = True
			self.outfile = open(attrs['name'] + '.html', 'w')
			self.outfile.write('<html><head>\n')
			self.outfile.write('<title>%s</title>\n' % attrs['title'])
			self.outfile.write('</head><body>\n')
		elif self.inPage:
			self.outfile.write('<%s' % name)
			for key, val in attrs.items():
				self.outfile.write(' %s="%s"' % (key, val))
			self.outfile.write('>')

	def endElement(self, name):
		if name == 'page':
			self.inPage = False
			self.outfile.write('\n</body></html>')
			self.outfile.close()
		elif self.inPage:
			self.outfile.write('</%s>' % name)

	def characters(self, string):
		if self.inPage: self.outfile.write(string)

parse('website.xml', PageMaker())
