#from dragonfly Dictation
from dragonfly import *


# modes
# 0 - normal
# 1 - insert
# 2 - visual
mode = 0

grammar = Grammar("vim_example")

ex_rule = MappingRule(
		name="insert",
		mapping={
			  "up" : Key ("up"),
			  "down" : Key ("down"),
			  "left" : Key("left"),
			  "right" : Key("right"),
			  "delete" : Key("delete"),
			  "strike" : Key("d,d"),
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
			  "next" : Key("n")
			  #"for <var> in <lower> to <upper>" : Text("for %(var)s in range (%(lower)d, %(upper)d")
			  
			  "if" : Text("if <text>:" + next)
			  #"<n> up" : Key ("up:%(n)d"),
			  #"<n> down" : Key ("down: %(n)d"),
			  #"<n> left" : Key ("left: %(n)d"),
			  #"<n> right" : Key ("right: %(n)d"),
			  #"(dictate|say) <text>" : Text("%(text)s"),
			  #"print a greeting for <name>" : Text("hello %(name)s")
			}
	)

grammar.add_rule(ex_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

