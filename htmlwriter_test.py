import HTMLWriter as hw

def assertEQ(expected, actual, title=None):
	if expected == actual: return True

	if title != None:
		s = title + ": \n"
	else:
		s = ""
	s += "Expected: \n\"" + expected + "\"\n Actual: \n\"" + actual + "\""
	print s
	raise AssertionError

def testRoot():
	r = hw.newRoot()
	expected = """<!DOCTYPE html>\n<html>\n</html>\n"""
	return assertEQ(expected, str(r), "testRoot")

def testMakeEChild():
	r = hw.newRoot()
	h = r.makeEChild("head")
	b = r.makeEChild("body")
	t = h.makeEChild("title")
	expected = """<!DOCTYPE html>\n<html>\n<head>\n<title>\n</title>\n</head>\n<body>\n</body>\n</html>\n"""
	return assertEQ(expected, str(r), "testRoot")

def testBasicDocument():
	# Implicitly tests makeTChild (the text node) as well
	t = "Test Title!"
	root, head, body = hw.basicDocument(t)
	expected = """<!DOCTYPE html>\n<html>\n<head>\n<title>\nTest Title!\n</title>
</head>\n<body>\n</body>\n</html>\n"""
	return assertEQ(expected, str(root), "Basic Document test")




def allTests():
	testRoot()
	testMakeEChild()
	testBasicDocument()
	return True



def main():
	allTests()

if __name__ == '__main__':
	main()