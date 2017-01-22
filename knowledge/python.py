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

def fmtCamel(text):
	text = str(text)

	Text("%s = VAR" % format_camel(text)).execute()

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
		"defun <text>" : Function(defun)
		}
	extras = [Dictation("text")]
	defaults = {}

	def _process_recognition(self, value, extras):
		#print("PyLang: %s" % value._action._spec)
		value.execute(extras)
