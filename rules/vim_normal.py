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
		"quit" : Key("escape,colon,q,enter"),

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
		# TODO: fix conflict using Compound
		# http://dragonfly.readthedocs.io/en/latest/rules.html#compoundrule-class
		#"append" : Key("a"),
		"append at [the] end of [the] line" : Key("A"),
		# TODO: fix conflict
		#"insert at [the] (start|beginning) of [the] line" : Key("I"),

		# Editing
		"delete" : Key("x"),
		"strike | delete line" : Key("d,d"),

		# Searching
		"(find | search for) <text>" : Function(do_search),
		"next" : Key("n"),
		"clear search" : Text(":nohl") + Key("enter")

		# Movements
		#"<n> up" : Text ("%(up)s"),
		}
	extras = [Dictation("text")]
	defaults = {"text" : ""}

	def _process_recognition(self, value, extras):
		#print "REC", str(self), "VALUE", str(value), "EXTRAS", str(extras)
		#print "action", value._action, "data", value._data
		action = value._action
		print("NORM: %s" % str(action))

		# Nasty hack
		if isinstance(action, dragonfly.actions.action_key.Key) and action._spec in ["i", "a", "A", "I", "o", "O"]:
			self.parent.handle_event("insert")

		value.execute(extras)
