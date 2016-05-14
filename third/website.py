#!/usr/bin/env python
# -*- coding:utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import parse
import os

class Dispatcher(object):

	def dispatch(self, prefix, name, attrs=None):
		sname = prefix + name.capitalize()
		dname = 'default' + prefix.capitalize()
		method = getattr(self, sname, None)
		if method: 
			args = ()
		else: 
			args = name,
			method = getattr(self, dname, None)
		if prefix == 'start': args += attrs,
		if callable(method): return method(*args)

	def startElement(self, name, attrs):
		self.dispatch('start', name, attrs)

	def endElement(self, name):
		self.dispatch('end', name)

class WebsiteHandler(Dispatcher, ContentHandler):

	inPage = False

	def __init__(self, diretory):
		super(WebsiteHandler, self).__init__()
		self.directory = [diretory]
		self.ensureDir()

	def ensureDir(self):
		path = os.path.join(*self.directory)
		if not os.path.isdir(path): os.makedirs(path)
	
	def defaultStart(self, name, attrs):
		if self.inPage:
			self.outfile.write('<' + name)
			for key, val in attrs.items():
				self.outfile.write(' %s="%s"' % (key, val))
			self.outfile.write('>')

	def defaultEnd(self, name):
		if self.inPage:
			self.outfile.write('</%s>' % name)
	
	def startDirectory(self, attrs):
		self.directory.append(attrs['name'])
		self.ensureDir()
	
	def endDirectory(self):
		self.directory.pop()

	def startPage(self, attrs):
		filename = os.path.join(*self.directory + [attrs['name'] + '.html'])
		self.outfile = open(filename, 'w')
		self.writeHeader(attrs['title'])
		self.inPage = True
	
	def endPage(self):
		self.writeFooter()
		self.inPage = False

	def writeHeader(self, title):
		self.outfile.write('<html>\n <head>\n\t<title>%s</title>\n </head>\n\t<body>' % title)

	def writeFooter(self):
		self.outfile.write('\n </body>\n</html>\n')
	
	def characters(self, string):
		if self.inPage: self.outfile.write(string)

diretory = 'xmlproject'
parse('website.xml', WebsiteHandler(diretory))
