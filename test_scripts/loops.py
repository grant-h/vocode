#from dragonfly Dictation
import string
from dragonfly import *

# modes
# -1 - init (no mode)
# 0 - normal
# 1 - insert
# 2 - visual
mode = -1

grammar = Grammar("vim_example")

def speak(text):
	try:
		get_engine().speak(text)
		print("Saying '%s'" % text)
	except:
		print("Voice not ready")

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

def enter_insert():
	global mode

	if mode == 1:
		return

	print("INSERT")
	speak("insert mode")
	mode = 1
	Key("i").execute()

def enter_normal():
	global mode

	if mode == 0:
		return

	print("NORMAL")
	speak("normal mode")
	mode = 0
	Key("escape").execute()
	Key("escape").execute()

ex_rule = MappingRule(
		name="insert",
		mapping={
			  '(lock Dragon | deactivate)':   Playback([(["go", "to", "sleep"], 0.0)]),
			  "insert [mode]": Function(enter_insert),
			  "escape" : Function(enter_normal),
			  "up" : Key ("up"),
			  "up <total_line>" : Key("up:%(total_line)d"),
			  "down" : Key ("down"),
			  "down <total_line>" : Key("down:%(total_line)d"),
			  "left" : Key("left"),
			  "left <total_line>" : Key("left:%(total_line)d"),
			  "right" : Key("right"),
			  "right <total_line>" : Key("right:%(total_line)d"),
			  "delete" : Key("delete"),
			  "strike [that]"  : Key("d,d"),
			  "save" : Key("escape,colon,w,enter"),
			  "pageup" : Key("pgup"),
			  "pagedown": Key("pgdown"),
			  "quit" : Key("escape,colon,q,enter"),
			  "selectchar": Key("escape,v"),
			  "copy" : Key("y"),
			  "paste" : Key ("p"),
			  "selectline" : Key("escape, s-v"),#shift-v
			  "gotoline" : Key("escape,colon"),
			  "find" : Key("escape,slash"),
			  "next" : Key("n"),
			  "var camel <text>" : Function(fmtCamel),
			  "defun <text>" : Function(defun),
			  
			  "select <total_line> line" : Key("escape,s-v,down:%(total_line)d"),
			  # for loop
			  "for [from] <start> to <end>" : Text("for i in range(%(start)d, %(end)d):") + Key("enter,tab"),
			  # if statement
			  "if <var>" : Text("if %(var)s: ") + Key("enter,tab"),
			  # else statement
			  "else if <var>" : Text("elif %(var)s: ") + Key("enter,tab"),
			  #"if <var1> [is] less [than] <var2>" : Text("for i in range(%(start)d, %(end)d): "),
			  #"if <var1> [is] equal [to] <var2>" : Text("for i in range(%(start)d, %(end)d): "),
			  #"if <var1> [is] greater [than] <var2>" : Text("for i in range(%(start)d, %(end)d): "),
			  



			  #"speak test" : Function(speakTest),

			  #"for <var> in <lower> to <upper>" : Text("for %(var)s in range (%(lower)d, %(upper)d")
			  
			  #"if" : Text("if <text>:" + next)Bart you
			  #"<n> up" : Key ("up:%(n)d"),
			  #"<n> down" : Key ("down: %(n)d"),
			  #"<n> left" : Key ("left: %(n)d"),
			  #"<n> right" : Key ("right: %(n)d"),
			  #"(dictate|say) <text>" : Text("%(text)s"),
			  #"print a greeting for <name>" : Text("hello %(name)s")
			},
		extras = [Dictation("text"), IntegerRef("total_line", 1, 100), 
				 IntegerRef("start", 1, 100), IntegerRef("end", 1, 100), Dictation("var")],
				 

		defaults = {
					"total_line": 1,
					"start": 0,
					"end": 5
		}
	)

grammar.add_rule(ex_rule)

grammar.load()

print()
print(">>> Vocode v0.1 now starting")
speak("startup")
enter_normal()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
