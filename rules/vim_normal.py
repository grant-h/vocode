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
		'insert | insert mode':  Key("i"),
		'escape':  Key("escape"),
		'grab all [text]' : Key("g, g, V, G"),

		# Buffer management
		"save" : Key("escape,colon,w,enter"),
		"(quit | exit)" : Key("escape,colon,q,enter"),
                "window right" : Key("c-w,l"),
                "window up" : Key("c-w,k"),
                "window down" : Key("c-w,j"),
                "window left" : Key("c-w,h"),
                "next tab" : Key("g,t"),

		# History
		"(undo|scratch|whoops)": Key("u"),
                "<total_line> undo": Key("u:%(total_line)d"),
		"redo": Key("c-r"),
                "<total_line> redo": Key("c-r:%(total_line)d"),

		# Movement
                "bottom" : Key("G"),
                "[go] right <total_line> word[s]" : Key("w:%(total_line)d"),
                "[go] left <total_line> word[s]" : Key("b:%(total_line)d"),
                "goto [the] first character" : Key("0"),

		"top" : Key("g,g"),
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
		"zap word" : Key("d,w"),
		"zap <total_line> word[s]" : Key("d") + Text("%(total_line)d") + Key("w"),
		"strike | delete line" : Key("d,d"),
		"delete <total_line> line[s]" : Key("d") + Text("%(total_line)d") + Key("d"),
                "delete [u]till [the] end of [the] line" : Key("d,dollar,escape"),
                "delete all right" : Key("d,dollar,escape"),
                "delete all left" : Key("d,caret,escape"),
		"select <total_line> line[s] above" : Key("escape,s-v,up:%(total_line)d"),
		"select <total_line> line[s] below" : Key("escape,s-v,down:%(total_line)d"),
		"copy <total_line> line[s] above" : Key("escape,V,up:%(total_line)d,y"),
		"copy <total_line> line[s] below" : Key("escape,V,down:%(total_line)d,y"),
		"cut <total_line> line[s] above" : Key("escape,V,up:%(total_line)d,d"),
		"cut <total_line> line[s] below" : Key("escape,V,down:%(total_line)d,d"),
		"paste": Key("p"),
		"paste above": Key("P"),
		"copy" : Key("y"),
		"cut" : Key("d"),
                # Shifting/indentation
                "shift left" : Key("langle,langle"),
                "shift left <total_line> time[s]" : Key("langle:%(total_line)d,langle:%(total_line)d"),
                "shift right" : Key("rangle,rangle"),
                "shift right <total_line> time[s]" : Key("rangle:%(total_line)d,rangle:%(total_line)d"),
                "shift <total_line> line[s] left" : Key("langle") + Text("%(total_line)d") + Key("langle"),
                "shift <total_line> line[s] right" : Key("rangle") + Text("%(total_line)d") + Key("rangle"),
		
		# Searching
		"(find | search for) <text>" : Function(do_search),
		"next" : Key("n"),
		"clear search" : Text(":nohl") + Key("enter")
		}

	extras = [
            Dictation("text"),
            Dictation("var"),
            IntegerRef("total_line", 1, 100),
            IntegerRef("start", 1, 100),
            IntegerRef("end", 1, 100),
            IntegerRef("line_num", 1, 9999)
            ]
        defaults = {
            "text" : "",
            "total_line" : 1,
            "start": 0,
            "end": 5,
            "line_num" : 1
            }

	def _process_recognition(self, value, extras):
		#print "REC", str(self), "VALUE", str(value), "EXTRAS", str(extras)
		#print "action", value._action, "data", value._data
		action = value._action
		print("NORM: %s" % str(action))

		# Nasty hack
		if isinstance(action, dragonfly.actions.action_key.Key) and action._spec in ["i", "a", "A", "I", "o", "O"]:
			self.parent.handle_event("insert")

		value.execute(extras)
