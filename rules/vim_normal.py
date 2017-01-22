import dragonfly
from dragonfly import *

def do_search(text):
	text = str(text)
	print("Searching for '%s'" % text)
	act = Key("slash") + Text(text)
	act.execute()

class VimNormalRules(MappingRule):
	def __init__(self):
		self.parent = None
		super(VimNormalRules, self).__init__()

	name = "vim_normal"
	mapping = {
		'insert':  Key("i"),
		'escape':  Key("escape"),
		'grab all [text]' : Key("g, g, V, G"),
		"enter|return" : Key("enter"),

		# Buffer management
		"save" : Key("escape,colon,w,enter"),
		"(quit | exit)" : Key("escape,colon,q,enter"),

		# History
		"(undo|scratch|whoops)": Key("u"),
		"redo": Key("c-r"),

		# Movement
		"pageup" : Key("pgup"),
		"pagedown": Key("pgdown"),
		"bottom" : Key("G"),
		"top" : Key("g,g"),
		"up" : Key ("up"),
		"down" : Key ("down"),
		"left" : Key("left"),
		"right" : Key("right"),
		"[goto] [the] end of [the] line" : Key("dollar"),
		"[goto] [the] (start|beginning) of [the] line" : Key("caret"),
		"go to line [number] <line_num>" : Key("escape,colon") + Text("%(line_num)d") + Key("enter"),
		# TODO: fix conflict using Compound
		# http://dragonfly.readthedocs.io/en/latest/rules.html#compoundrule-class
		#"append" : Key("a"),
		"append at [the] end of [the] line" : Key("A"),
		# TODO: fix conflict
		#"insert at [the] (start|beginning) of [the] line" : Key("I"),

		# Editing
		"delete" : Key("x"),
		"strike | delete line" : Key("d,d"),
		"select <total_line> line[s] above" : Key("escape,s-v,up:%(total_line)d"),
		"select <total_line> line[s] below" : Key("escape,s-v,down:%(total_line)d"),
		"copy <total_line> line[s] above" : Key("escape,V,up:%(total_line)d,y"),
		"copy <total_line> line[s] below" : Key("escape,V,down:%(total_line)d,y"),
		"cut <total_line> line[s] above" : Key("escape,V,up:%(total_line)d,d"),
		"cut <total_line> line[s] below" : Key("escape,V,down:%(total_line)d,d"),
		"paste": Key("p"),
		"copy" : Key("y"),
		"cut" : Key("d"),
		
		# Searching
		"(find | search for) <text>" : Function(do_search),
		"next" : Key("n"),
		"clear search" : Text(":nohl") + Key("enter")

		# Movements
		#"<n> up" : Text ("%(up)s"),
		}
	extras = [Dictation("text"), IntegerRef("total_line", 1,100), IntegerRef("line_num", 1, 9999)]
	defaults = {"text" : "", "total_line": 1, "line_num": 1}

	def _process_recognition(self, value, extras):
		#print "REC", str(self), "VALUE", str(value), "EXTRAS", str(extras)
		#print "action", value._action, "data", value._data
		action = value._action
		print("NORM: %s" % str(action))

		# Nasty hack
		if isinstance(action, dragonfly.actions.action_key.Key) and action._spec in ["i", "a", "A", "I", "o", "O"]:
			self.parent.handle_event("insert")

		value.execute(extras)
