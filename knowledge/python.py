from dragonfly import *

def format_camel(text):
	"""
	Format the sentence divided by spaces in to camelCaseSpelling
	"""
	output = ""
	for i,w in enumerate(text.split(" ")):
		if i > 0:
			output += w[0].upper() + w[1:]
		else:
			output += w
	return output

def format_default(text):
	"""
	Format the sentence divided by spaces in to default_spacing
	"""
	output = []
	for i,w in enumerate(text.split(" ")):
		output += [w.lower()]
	return "_".join(output)

def format_class(text):
	"""
	Format the sentence divided by spaces in to ClassCasing
	"""
	output = []
	for i,w in enumerate(text.split(" ")):
		output += [w[0].upper() + w[1:]]
	return "".join(output)


# default - this_is_a_variable
# camel   - thisIsAVariable
# class   - ThisIsAVariable

def fmtVarCamel(text):
	text = str(text)

	Text("%s" % format_camel(text)).execute()

def fmtVarDefault(text):
	text = str(text)

	Text("%s" % format_default(text)).execute()

def fmtVarClass(text):
	text = str(text)

	Text("%s" % format_class(text)).execute()

def defun(text):
	text = str(text)
	Text("def %s():\npass" % format_camel(text)).execute()
	Key("up,end,left,left").execute()

def lang_import(text):
	text = str(text)
	Text("import %s\n" % text).execute()

class PythonRules(MappingRule):
	name = "python_lang"
	mapping = {
		"[new] import <text>" : Function(lang_import),
		"defun <text>" : Function(defun),

		# Writing variables
		"var camel <text>" : Function(fmtVarCamel),
		"var default <text>" : Function(fmtVarDefault),
		"var class <text>" : Function(fmtVarClass),
		"assign to" : Text(" = "),

		# Python version of None
		"none" : Text("None"),
		"false" : Text("False"),
		"true" : Text("True"),

		# Python types
		"whomp (array | access)" : Text("[]") + Key("left"),
		"whomp (lookup|dictionary)" : Text("dict()"),
		"whomp set" : Text("set()")
		}
	extras = [Dictation("text")]
	defaults = {}

	def _process_recognition(self, value, extras):
		print("PY: %s" % str(value._action))
		value.execute(extras)
