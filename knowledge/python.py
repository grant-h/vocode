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
	(Text("import %s" % text)+Key("enter")).execute()

def var_binop(varA, varB, op):
        left = str(varA)
        right = str(varB)

        print "BINOP",left, right
        left = format_default(left)
        right = format_default(right)
        action = Text(left) + Text(" " + op + " ") + Text(right)
        action.execute()

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
		"pass" : Text("pass"),

		# Python types
		"whomp (array | access)" : Text("[]") + Key("left"),
		"whomp (lookup|dictionary)" : Text("dict()"),
		"whomp set" : Text("set()"),

                # for loop
                "for [from] <start> to <end>" : Text("for i in range(%(start)d, %(end)d):") + Key("enter,tab"),

                # if statement bool
                "if <var>" : Text("if %(var)s:") + Key("enter,tab"),
                # else if statement bool
                "else if <var>" : Text("elif %(var)s: ") + Key("enter,tab"),

                # if equals int
                "if equals <varA> <varB>" : Text("if %(varA)s == %(varB)s:") + Key("enter,tab"),
                #simple else statement
                "else" : Text("else:") + Key("enter,tab"),
                #while statement
                "while" : Text("while :") + Key("left"),
                #comparitor
                "double equal" : Text(" == "),
                #arithmatic
                "<numA> plus <numB>" : Text("%(numA)d + %(numB)d"),
                "<numA> minus <numB>" : Text("%(numA)d - %(numB)d"),
                "<numA> divide <numB>" : Text("%(numA)d / %(numB)d"),
                "<numA> (mult|multiply|times) <numB>" : Text("%(numA)d * %(numB)d"),
                "<numA> mod[ulus] <numB>" : Text("%(numA)d") + Text("%%") + Text("%(numB)d"),
                # Variable versions
                "<varA> plus <varB>" : Function(var_binop, op="+"),
                "<varA> minus <varB>" : Function(var_binop, op="-"),
                "<varA> divide <varB>" : Function(var_binop, op="/"),
                "<varA> (mult|multiply|times) <varB>" : Function(var_binop, op="*"),
                "<varA> mod[ulus] <varB>" : Function(var_binop, op="%"),

                #### begin untested code
                #less or greater than NUM
                "<numA> less equal <numB>" : Text("%(numA)d <= %(numB)d"),
                "<numA> great equal <numB>" : Text("%(numA)d >= %(numB)d"),
                "<numA> great <numB>" : Text("%(numA)d > %(numB)d"),
                "<numA> less <numB>" : Text("%(numA)d < %(numB)d"),
                 #less or greater than VARS
                "<varA> (less equal | L-E) <varB>" : Function(var_binop, op="<="),
                "<varA> great equal <varB>" : Function(var_binop, op=">="),
                "<varA> great <varB>" : Function(var_binop, op=">"),
                "<varA> less <varB>" : Function(var_binop, op="<"),

                #basic for
                "for" : Text("for :") + Key("left"),
                #basic if
                "if" : Text("if :") + Key("left"),

                "plus equals" : Text(" += ")

                # String handling
      }
	extras = [
            Dictation("text"),
            Dictation("var"),
            Dictation("varA"),
            Dictation("varB"),
            IntegerRef("total_line", 1, 1000),
            IntegerRef("start", 1, 1000),
            IntegerRef("end", 1, 1000),
            IntegerRef("numA", 1, 10000),
            IntegerRef("numB", 1, 10000)
            ]
        defaults = {
            "text" : "",
            "total_line" : 1,
            "start": 0,
            "end": 5,
            "numA":0,
            "numB":0
            }

	def _process_recognition(self, value, extras):
		print("PY: %s" % str(value._action))
		value.execute(extras)
