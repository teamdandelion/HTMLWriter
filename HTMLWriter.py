class HTMLElement:
	def __init__(self, tagname, parent, attributes={}, selfclosing=False):
		self.tagname = tagname
		self.attributes = {}
		self.parent = parent
		self.children = []
		self.selfclosing = selfclosing

	def __repr__(self):
		strlist = []
		if self.parent == None: # this is the root
			strlist = ["<!DOCTYPE html>\n"]
		else:
			strlist = []

		strlist.append("<")
		strlist.append(self.tagname)
		
		for attr, val in self.attributes.iteritems():
			strlist.append(attr + "=\"" + val + "\"")

		if self.selfclosing:
			assert self.children == [] # self-closing elements can't have children
			strlist.append("/>\n")
		else:
			strlist.append(">\n")
			for c in self.children:
				strlist.append(str(c))
			strlist.append("</" + self.tagname + ">\n")
		return ''.join(strlist)

	def makeEChild(self, tagname, attributes={}, selfclosing=False):
		child = HTMLElement(tagname, self, attributes, selfclosing)
		self.children.append(child)
		return child

	def makeTChild(self, text):
		self.children.append(text + "\n")
		return True


def newRoot():
	return HTMLElement("html", None)


def basicDocument(title):
	root = newRoot()
	head = root.makeEChild("head")
	t = head.makeEChild("title")
	t.makeTChild(title)
	body = root.makeEChild("body")

	return root, head, body


