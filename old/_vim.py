from dragonfly import *

# modes
# 0 - normal
# 1 - insert
# 2 - visual
mode = 0

grammar = Grammar("vim_example2")

ex_rule = MappingRule(
		name="our-mapping",
		mapping={
			 "(undo|scratch|whoops)": Key("u"),
			 "bottom" : Key("G"),
			 "top" : Key("g,g"),
			 "redo": Key("c-r"),
			 "selectall": Key("g,g,V,G"),	 
			 "enter" : Key("enter")

			}
	)

grammar.add_rule(ex_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

