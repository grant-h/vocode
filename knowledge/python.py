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
		"whomp set" : Text("set()"),

                # for loop
                "for [from] <start> to <end>" : Text("for i in range(%(start)d, %(end)d):") + Key("enter,tab"),
                # if statement
                "if <var>" : Text("if %(var)s: ") + Key("enter,tab"),
                # else statement
                "else if <var>" : Text("elif %(var)s: ") + Key("enter,tab")
                #"if <var1> [is] less [than] <var2>" : Text("for i in range(%(start)d, %(end)d): "),
                #"if <var1> [is] equal [to] <var2>" : Text("for i in range(%(start)d, %(end)d): "),
                #"if <var1> [is] greater [than] <var2>" : Text("for i in range(%(start)d, %(end)d): "),
      }
	extras = [
            Dictation("text"),
            Dictation("var"),
            IntegerRef("total_line", 1, 100),
            IntegerRef("start", 1, 100),
            IntegerRef("end", 1, 100)
            ]
        defaults = {
            "text" : "",
            "total_line" : 1,
            "start": 0,
            "end": 5
            }

	def _process_recognition(self, value, extras):
		print("PY: %s" % str(value._action))
		value.execute(extras)
